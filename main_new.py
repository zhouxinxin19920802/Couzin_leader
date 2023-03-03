# -*- coding: utf-8 -*-
# @Author  : zhouxin
# @Time    : 2023/2/28 16:47
# @File    : main_new.py
# @annotation    : 改进了稳态值的获取方式

import logging
import math
import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter as sg

import test2.tool_methods as tm

logging.basicConfig(
    level=logging.INFO,  # 控制台打印的日志级别
    filename="test.txt",
    # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
    filemode="w",
    # a是追加模式，默认如果不写的话，就是追加模式
    format="%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s"
    # 日志格式
)


def get_min(data):
    # 获取最小值及最小值下标
    min_value = float("inf")
    id = 0
    for i in range(0, len(data)):
        if data[i] < min_value:
            min_value = data[i]
            id = i
    return id, min_value


def calculate_fluctuation(smooth_data_before, smooth_data_after):
    """
    此函数主要作用为计算波动因子

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


data = []
for line in open("shape_data.txt", "r", encoding="utf-8"):
    line = line.strip("\n")
    data.append(float(line))

times_stable = 0
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    times_stable = lines[0].strip("\n")


times_stable = int(float(times_stable))


time_period_before_disturblance = 50

times_start = 500 - time_period_before_disturblance


time_period = 300


# 获取的时间段为故障前50个step到稳态后的50个时间段
data_resilience = data[times_start : times_stable + time_period]


# sg滤波 window_length: 窗口长度，该值为正奇数，polyorder越大越平滑
# window_length值越小，则曲线越贴近真实曲线
# polyorder 用于拟合样本的多项式的阶数
data_resilience_sg = sg(data_resilience, window_length=25, polyorder=1)
data_after_destroy = data_resilience_sg[times_stable - times_start: times_stable - times_start + time_period]

# 通过MSER原则，获取稳态时间值
time_steps = [i for i in range(len(data_after_destroy))]
stable_id, min_var = tm.calculate(time_steps, data_after_destroy)

print("times_stable - times_start:", times_stable - times_start, "stable_id:", stable_id, " ", "min_var:", min_var)

"""
plt.plot(data_after_destroy, color="r", ls="--", label="smoothed")

plt.show()

"""
# 获取最小值
id, min_value = get_min(data_resilience_sg[time_period_before_disturblance:-time_period])
if min_value < 0:
    min_value = 0

print("times_stable:", times_stable - times_start)
print("id:", id + 50, " ", "min_value:", min_value)


# 韧性计算
# y_d 期望性能
y_d = 0
for i in range(time_period_before_disturblance):
    y_d = y_d + data_resilience_sg[i]
y_d = y_d / time_period_before_disturblance

# y_r 恢复后性能

y_r = 0
# print(len(data_resilience_sg))

# 获取恢复后的平均值和方差
meanvalue_after_destroy = np.mean(data_after_destroy)
var_after_destroy = np.var(data_after_destroy)

print("meanvalue_after_destroy:", meanvalue_after_destroy, " ", "var_after_destroy:", var_after_destroy)


y_r = meanvalue_after_destroy

print("min_value:", min_value, " y_r:", y_r)

# y_min 最低性能
y_min = min_value
# t_0 感兴趣时段起始时间
t_0 = 0
# t_d 遭受扰动时间
t_d = time_period_before_disturblance
# 开始恢复时间
t_r = id
# 恢复到稳态的时间
t_ss = times_stable
# 感兴趣时段结束时间
t_final = len(data_resilience_sg)

# 最低性能要求
y_m = 0


#  总性能因子
sigma = sum(data_resilience_sg) / (y_d * len(data_resilience_sg))

#  rho 恢复因子
rho = y_r / y_d

#  最低性能银子
delta = y_min / y_d

# 恢复时间因子
tau = (t_ss - times_start) / (t_final - t_0)

# 波动因子
zeta = calculate_fluctuation(data_resilience, data_resilience_sg)

# 设置绝对时间尺度因子B, 将B设置为50
delta_l = 0.8
B = 50

# 计算到稳态后较长的一段时间内，数据的平均值和方差


# 做一个判断，比较恢复后的水平和最小的水平y_r和y_min
r = 0
if y_r > y_min:
    r = rho * sigma * (delta + zeta + 1 - tau ** (rho - delta)) * (delta_l ** (len(data_resilience) / B))
else:
    r = 0
# print("rho:",rho," sigma:",sigma," delta:",delta, " zeta:",zeta," tau:",tau, " rho:",rho," delta:",delta)
# print("########################")


f = open("resilence.txt", "a+")
f.write(str(r) + "\n")
f.close()


print("resilience_value:", r)


plt.plot(data_resilience, label="raw")
plt.plot(data_resilience_sg, color="r", ls="--", label="smoothed")
plt.legend()
plt.xlabel("steps")
plt.ylabel("velocity")
# 标出性能最低点和稳态时间点
plt.annotate(
    "minimum_value",
    xy=(id + time_period_before_disturblance + 2, min_value),
    xytext=(id + time_period_before_disturblance + 2, min_value + 1),
    weight="bold",
    color="b",
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="black"),
)
plt.annotate(
    "stable_value",
    xy=(times_stable - times_start, data_resilience_sg[times_stable - times_start]),
    xytext=(times_stable - times_start, data_resilience_sg[times_stable - times_start] - 0.5),
    weight="bold",
    color="b",
    arrowprops=dict(arrowstyle="->", lw=2, connectionstyle="arc3", color="red"),
)

# 设置最低水平，蓝色线表示稳定值，红色线条表示稳定值
plt.axhline(y=min_value, c="r", ls="-.", lw=1)
plt.axhline(y=y_r, c="b", ls="-.", lw=1)
plt.show()
# plt.pause(0.1)
plt.title("Interference data")
