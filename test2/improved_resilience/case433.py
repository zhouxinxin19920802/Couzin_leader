# -*- coding: utf-8 -*-
# @Author  : zhouxin
# @Time    : 2023/5/10 17:05
# @File    : case433.py
# @annotation    :


import math
import numpy as np
from scipy.signal import savgol_filter as sg

step = 0.1

x1_before = np.arange(0, 30, step)
x1_resist = np.arange(30, 50, step)
x1_recover = np.arange(50, 80, step)
x1_after = np.arange(80, 100, step)

# Case1
y1_before = 50 * x1_before
y1_resist = 70 - 2 / 3 * x1_resist
y1_recover = 1 / 3 * x1_recover + 10 / 3
y1_after = 30 * x1_after

# 横坐标合并
x1 = np.append(x1_before, x1_resist)
x1 = np.append(x1, x1_recover)
x1 = np.append(x1, x1_after)

# 纵坐标合并
y1 = np.append(y1_before, y1_resist)
y1 = np.append(y1, y1_recover)
y1 = np.append(y1, y1_after)

def calculate_fluctuation(smooth_data_before, smooth_data_after):
    """
    此函数主要作用为计算波动因子。

    Args:
        smooth_data_before(list) : 滤波前的数据
        smooth_data_after(list) : 滤波后的数据
    Return:
        波动因子
    """
    p_s = 0
    # 平滑前和平滑后数据差的平方和
    p_n = 0
    for item in smooth_data_after:
        p_s = p_s + item**2
    for i in range(len(smooth_data_after)):
        p_n = p_n + (smooth_data_before[i] - smooth_data_after[i]) ** 2
    snr_db = 10 * math.log((p_s / p_n), 10)
    zeta = 1 / (1 + math.exp(-0.25 * (snr_db - 15)))
    return zeta

y1_sg = sg(y1, window_length=25, polyorder=1)

# 波动因子

zeta = calculate_fluctuation(y1, y1_sg)

print(zeta)
