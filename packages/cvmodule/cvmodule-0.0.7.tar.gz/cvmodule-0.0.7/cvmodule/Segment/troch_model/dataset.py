import os
import pathlib
import cv2 as cv
import numpy as np
from PIL import Image

import torch as tc
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torch.utils.data import Dataset


def compute_mean_std(img_dir, mask_dir, channels=3):
    """归一化：计算图像的各个通道的均值、方差"""
    img_suffix = {'jpg', 'png', 'tiff', 'jpeg', 'JPG'}
    cumulative_mean = np.zeros(img_channels)
    cumulative_std = np.zeros(img_channels)
    cnt = 0  # 记录有多少张图像
    for file_path in os.listdir(img_dir):
        suffix = pathlib.Path(file_path).suffix[1:]
        name = pathlib.Path(file_path).stem
        if suffix in img_suffix:
            img = cv.imread(os.path.join(img_dir, file_path))
            if channels == 3:
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            else:
                img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            mask_path = os.path.join(mask_dir, name + '_mask.jpg')
            if not os.path.exists(mask_path):
                continue
            mask = cv.imread(mask_path)  # 读取图像的mask
            # 只计算目标区域的均值和方差
            img = img[mask == 255]  # 默认mask为黑白图，即分类的目标只有一个
            cumulative_mean += img.mean(axis=0)
            cumulative_std += img.std(axis=0)
            cnt += 1
    return cumulative_mean / cnt, cumulative_std / cnt


class DriveDataset(Dataset):
    def __init__(self):
        pass

    def __getitem__(self, item):
        pass

    def __len__(self):
        return len(self.img_list)

    @staticmethod
    def collate_fun(batch):
        return
