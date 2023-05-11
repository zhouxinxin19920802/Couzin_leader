# -*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import math

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

step = 0.001

# 性能曲线都分为4个阶段,破坏前稳定阶段，抵抗阶段，恢复阶段，
# case1
x1_before = np.arange(0, 1, step)
x1_resist = np.arange(1, 2, step)
x1_recover = np.arange(2, 3, step)
x1_after = np.arange(3, 4, step)

# 横坐标合并
x1 = np.append(x1_before, x1_resist)
x1 = np.append(x1, x1_recover)
x1 = np.append(x1, x1_after)

# 纵坐标合并
y1_before = 2 * np.ones(len(x1_before))
y1_resist = 2 - pow(x1_resist - 1, 2)
y1_recover = 1 + pow(x1_recover - 2, 2)
y1_after = 2 * np.ones(len(x1_after))

y1 = np.append(y1_before, y1_resist)
y1 = np.append(y1, y1_recover)
y1 = np.append(y1, y1_after)

# case2
x2_before = np.arange(0, 1, step)
x2_resist = np.arange(1, 2, step)
x2_recover = np.arange(2, 3, step)
x2_after = np.arange(3, 4, step)

x2 = np.append(x2_before, x2_resist)
x2 = np.append(x2, x2_recover)
x2 = np.append(x2, x2_after)


y2_before = 2 * np.ones(len(x2_before))
y2_resist = 3 - x2_resist
y2_recover = x2_recover - 1
y2_after = 2 * np.ones(len(x2_after))

y2 = np.append(y2_before, y2_resist)
y2 = np.append(y2, y2_recover)
y2 = np.append(y2, y2_after)

# case3
x3_before = np.arange(0, 1, step)
x3_resist = np.arange(1, 2, step)
x3_recover = np.arange(2, 3, step)
x3_after = np.arange(3, 4, step)

x3 = np.append(x3_before, x3_resist)
x3 = np.append(x3, x3_recover)
x3 = np.append(x3, x3_after)


y3_before = 2 * np.ones(len(x3_before))
y3_resist = 1 + pow(x3_resist - 2, 2)
y3_recover = 2 - pow(x3_recover - 3, 2)
y3_after = 2 * np.ones(len(x3_after))

y3 = np.append(y3_before, y3_resist)
y3 = np.append(y3, y3_recover)
y3 = np.append(y3, y3_after)

# 波动因子的计算
# 导入滤波函数
from scipy.signal import savgol_filter as sg

# case1的波动因子
y1_sg = sg(y1, window_length=25, polyorder=2)
zeta1 = calculate_fluctuation(y1, y1_sg)

# case2的波动因子
y2_sg = sg(y2, window_length=25, polyorder=2)
zeta2 = calculate_fluctuation(y2, y2_sg)

# case3的波动因子
y3_sg = sg(y3, window_length=25, polyorder=2)
zeta3 = calculate_fluctuation(y3, y3_sg)


print("zeta1:{},zeta2:{},zeta3:{}".format(zeta1, zeta2, zeta3))
print("##############################")
# 积分计算求聪聪师兄韧性
from scipy import integrate

# 时间系数
a = 0.8
# 绝对时间尺度
B = 2

alpha_factor = 0.5
beta_factor = 1 - alpha_factor
#
# ########################################################################################
# case1:韧性
# 抗毁过程因子
delta1_d = integrate.quad(lambda x: 2 - pow(x - 1, 2), 1, 2)[0] / integrate.quad(lambda x: 2, 1, 2)[0]

# 抗毁状态因子，最小值比破坏前
sigma1_d = 1 / 2
# 抗毁时间因子
rho1_d = math.pow(a, B / 1)

# 抗毁过程因子
delta1_r = integrate.quad(lambda x: 1 + pow(x - 2, 2), 2, 3)[0] / integrate.quad(lambda x: 2, 2, 3)[0]
# 抗毁状态因子
sigma1_r = 2 / 2
# 抗毁时间因子
rho1_r = math.pow(a, 1 / B)
print(delta1_d, sigma1_d, rho1_d, delta1_r, sigma1_r, rho1_r)
print("case1:%s" % str(alpha_factor * delta1_d * sigma1_d * rho1_d + beta_factor * delta1_r * sigma1_r * rho1_r))
#
# ########################################################################################
# case2:韧性
# 抗毁过程因子
delta2_d = integrate.quad(lambda x: 3 - x, 1, 2)[0] / integrate.quad(lambda x: 2, 1, 2)[0]
# 抗毁状态因子
sigma2_d = 1 / 2
# 抗毁时间因子
rho2_d = math.pow(a, B / 1)

# 抗毁过程因子
delta2_r = integrate.quad(lambda x: x - 1, 2, 3)[0] / integrate.quad(lambda x: 2, 2, 3)[0]
# 抗毁状态因子
sigma2_r = 2 / 2
# 抗毁时间因子
rho2_r = math.pow(a, 1 / B)
print(delta2_d, sigma2_d, rho2_d, delta2_r, sigma2_r, rho2_r)
print("case2:", str(alpha_factor * delta2_d * sigma2_d * rho2_d + beta_factor * delta2_r * sigma2_r * rho2_r))
# ########################################################################################
# # case2:韧性
# # 抗毁过程因子
delta3_d = integrate.quad(lambda x: 1 + pow(x - 2, 2), 1, 2)[0] / integrate.quad(lambda x: 2, 1, 2)[0]
# 抗毁状态因子
sigma3_d = 1 / 2
# 抗毁时间因子
rho3_d = math.pow(a, B / 1)

# 抗毁过程因子
delta3_r = integrate.quad(lambda x: 2 - pow(x - 3, 2), 2, 3)[0] / integrate.quad(lambda x: 2, 2, 3)[0]
# 抗毁状态因子
sigma3_r = 2 / 2
# 抗毁时间因子
rho3_r = math.pow(a, 1 / B)
delta3_d = integrate.quad(lambda x: 1 + pow(x - 2, 2), 1, 2)[0] / integrate.quad(lambda x: 2, 1, 2)[0]
print(delta3_d, sigma3_d, rho3_d, delta3_r, sigma3_r, rho3_r)
print("case3:", str(alpha_factor * delta3_d * sigma3_d * rho3_d + beta_factor * delta3_r * sigma3_r * rho3_r))

# # Tran方法韧性
# performance_factor_1 = (integrate.quad(lambda x: 2, 0, 1)[0] + integrate.quad(lambda x: 2 - pow(x - 1, 2), 1, 2)[0] + \
#                     integrate.quad(lambda x: 1 + pow(x - 2, 2), 2, 3)[0] + integrate.quad(lambda x: 2, 3, 4)[0]) \
#                     /(integrate.quad(lambda x: 2, 0, 4)[0])
# print("performance_factor_1:{}".format(performance_factor_1))
#
# performance_factor_2 = (integrate.quad(lambda x: 2, 0, 1)[0] + integrate.quad(lambda x: 3 -x, 1, 2)[0] + \
#                     integrate.quad(lambda x: x - 1, 2, 3)[0] + integrate.quad(lambda x: 2, 3, 4)[0]) \
#                     /(integrate.quad(lambda x: 2, 0, 4)[0])
#
# print("performance_factor_2:{}".format(performance_factor_2))

# plt.plot(x1, y1, marker="d", markersize=0.5, markerfacecolor="none", color="r", ls="-", lw=0.01, label="case1")
# plt.plot(x2, y2, marker="d", markersize=0.5, markerfacecolor="none", color="g", ls="--", lw=0.01, label="case2")
# plt.plot(x3, y3, marker="d", markersize=0.5, markerfacecolor="none", color="b", ls="-", lw=0.01, label="case3")
#
# plt.axvspan(xmin=1, xmax=2, facecolor="y", alpha=0.3)
# plt.axvspan(xmin=2, xmax=3, facecolor="g", alpha=0.3)
#
# plt.xticks(np.arange(0, 4, 1))
# plt.yticks(np.arange(0, 5, 1))
# plt.xlim(0, 4)
# plt.ylim(0, 3)
# plt.legend()
# plt.xlabel("steps")
# plt.ylabel("performance")
#
#
# plt.grid(ls=":", lw=1, color="gray", alpha=0.5)
# plt.show()
