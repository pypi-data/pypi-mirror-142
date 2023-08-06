import torch as tc
import torch.nn as nn
import torch.nn.functional as F

import sys

sys.path.append(r'cvmodule\Segment\troch_model')

import loss


def criterion(inputs, target, loss_weight=None, num_classes=2, dice=True, ignore_idx=-100):
    """损失函数"""
    losses = {}
    for name, pred in inputs.items():
        # 忽略target中值为255的像素，255的像素是目标边缘或者padding填充
        loss = nn.functional.cross_entropy(pred, target, ignore_index=ignore_idx, weight=loss_weight)
        if dice:
            dice_target = loss.build_target(target, num_classes, ignore_idx)
            loss += loss.dice_loss(pred, dice_target, multi_classes=True, ignore_idx=ignore_idx)
        losses[name] = loss
    if len(losses) == 1:
        return losses['out']
    return losses['out'] + 0.5 * losses['aux']


def evaluate(model, data_loader, device, num_classes):
    """模型的验证环节，返回测试集的dice值"""
    model.eval()
    dice = loss.DiceCoefficient(num_classes=num_classes, ignore_idx=255)

    with tc.no_grad():
        for image, target in data_loader:
            image, target = image.to(device), target.to(device)
            outputs = model(image)
            pred = outputs['out']

            dice.update(pred, target)

        dice.reduce_from_all_process()
    return dice.value.item()


def train_one_epoch(model,
                    optimizer,
                    data_loader,
                    device,
                    epoch,
                    num_classes,
                    lr_scheduler,
                    print_freq=10,
                    scaler=None):
    model.train()
    loss_weight = None
    if num_classes == 2:
        loss_weight = tc.as_tensor([1.0, 2.0], device=device)  # 如果只有两类，需要注意背景的损失
    for image, target in data_loader:
        image, target = image.to(device), target(device)
        with tc.cuda.amp.autocast(enabled=scaler is not None):
            outputs = model(image)
            loss = criterion(outputs, target, loss_weight, num_classes, ignore_idx=255)

        optimizer.zero_grad()  # 梯度回传
        if scaler is not None:
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
        else:
            loss.backward()
            optimizer.step()

        lr_scheduler.step()
        lr = optimizer.param_groups[0]['lr']
    return


def create_lr_scheduler(optimizer, num_step, epochs, warmup=True, warmup_epochs=1, warmup_factor=1e-3):
    def inter(x):
        """
        根据step数返回一个学习率倍率因子，
        在训练开始之前，pytorch会提前调用一次lr_scheduler.step()方法
        """
        if warmup and x <= (warmup_epochs * num_step):
            alpha = float(x) / (warmup_epochs * num_step)
            return warmup_factor * (1 - alpha) + alpha  # warmup过程中lr倍率因子从warmup_factor -> 1
        return (1 - (x - warmup_epochs * num_step) / ((epochs - warmup_epochs) * num_step)) ** 0.9

    assert num_step > 0 and epochs > 0
    if warmup is False:
        warmup_epochs = 0
    return tc.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=inter)
