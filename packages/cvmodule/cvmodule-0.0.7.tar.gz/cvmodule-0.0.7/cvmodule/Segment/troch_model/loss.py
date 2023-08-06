import torch as tc
import torch.nn as nn
import torch.nn.functional as F


# 分割模型常用的损失函数

class DiceCoefficient:
    def __init__(self, num_classes=2, ignore_idx=-100):
        self.cumulative_dice = None
        self.num_classes = num_classes
        self.ignore_idx = ignore_idx
        self.count = None

    def update(self, pred, target):
        if self.cumulative_dice is None:
            self.cumulative_dice = tc.zeros(1, dtype=pred.dtype, device=pred.device)
        if self.count is None:
            self.count = tc.zeros(1, dtype=perd.dtype, device=pred.device)

        pred = F.one_hot(pred.argmax(dim=1), self.num_classes).permute(0, 3, 1, 2).float()
        dice_target = build_target(target, self.num_classes, self.ignore_idx)
        # 不计算背景的损失
        self.cumulative_dice += multi_classes_dice_coeff(pred[:, 1:], dice_target[:, 1:], ignore_idx=self.ignore_idx)
        self.count += 1

    @property
    def value(self):
        if self.count == 0:
            return 0
        return self.cumulative_dice / self.count

    def reset(self):
        """重置处理"""
        if self.cumulative_dice is not None:
            self.cumulative_dice.zero_()
        if self.count is not None:
            self.count.zero_()

    def reduce_from_all_process(self):
        if not tc.distributions.is_available():
            return
        if not tc.distributions.is_initialized():
            return
        tc.distributed.barrier()
        tc.distributed.all_reduce(self.cumulative_dice)
        tc.distributed.all_reduce(self.count)
        return


def build_target(target, num_classes, ignore_idx=-100):
    """将标签制作为 one_hot 的形式，有多个channel"""
    dice_target = target.clone()
    if ignore_idx >= 0:
        ignore_mask = tc.eq(target, ignore_idx)  # 与target中的元素进行对比，如果target中的元素有等于ignore_idx, 对应位置为True
        dice_target[ignore_mask] = 0
        # [N, H, W] -> [N, H, W, C]
        dice_target = nn.functional.one_hot(dice_target, num_classes).float()
        dice_target[ignore_mask] = ignore_idx
    else:
        dice_target = nn.functional.one_hot(dice_target, num_classes).float()
    return dice_target.permute(0, 3, 1, 2)


def dice_coeff(pred, target, ignore_idx=-100, epsilon=1e-6):
    # 计算图像的 dice 损失
    loss = 0.0
    batch_size = pred.shape[0]
    for i in range(batch_size):
        pred_i = pred[i].reshape(-1)
        target_i = target[i].reshape(-1)
        if ignore_idx >= 0:
            roi_mask = tc.ne(target_i, ignore_idx)
            pred_i = pred_i[roi_mask]
            target_i = target_i[roi_mask]
        inter = tc.dot(pred_i, target_i)  # 交集重合的部分才有 1 的存在
        sets_sum = tc.sum(pred_i) + tc.sum(target_i)  # 并集
        if sets_sum == 0:
            sets_sum = 2 * inter
        loss += (2 * inter + epsilon) / (sets_sum + epsilon)  # 计算 dice 值
    return loss / batch_size


def multi_classes_dice_coeff(pred, target, ignore_idx=-100, epsilon=1e-6):
    dice = 0.0
    for channel in range(x.shape[1]):  # 如果存在多个通道，需要根据不同的channel分别计算dice
        dice += dice_coeff(pred[:, channel, ...], target[:, channel, ...], ignore_idx, epsilon)
    return dice / x.shape[1]


def dice_loss(pred, target, multi_classes=False, ignore_idx=-100):
    pred = nn.functional.softmax(pred, dim=1)  # 计算 softmax
    calc_fun = multi_classes_dice_coeff if multi_classes else dice_coeff  # 根据类别的数量，选择使用哪个计算dice损失
    return 1 - calc_fun(pred, target, ignore_idx=ignore_idx)


if __name__ == "__main__":
    sample = tc.ones(size=(1, 4, 4, 3), dtype=tc.float)
    print(nn.functional.softmax(sample, dim=1))
    # res = build_target(sample, 3, -1)
    # print(res)
