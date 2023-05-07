# -*- coding: utf-8 -*-
# @Author  : zhouxin
# @Time    : 2023/5/6 10:38
# @File    : Congcong_method.py
# @annotation    :

import numpy as np
import test2.tool_methods as tm

# K1 期望性能，
# 通用
k1 = 50

# A1 和 A2 是相等的，A1是抵抗阶段最小值， A2是恢复阶段的最小值
# x1_short - 抵抗阶段拐点， x2_short - 恢复阶段拐点
x1_short = 25
x2_short = 70

# A1 最小性能
A1 = 20
# A2 是恢复阶段的最小性能
A2 = 20


# 对于每一个case,其分为两部分，抵抗阶段的性能曲线，恢复阶段的性能曲线

# case1的时间线
t_d_case1 = np.arange(0, 50, 0.1)
t_r_case1 = np.arange(50, 100, 0.1)
t_case1 = np.append(t_d_case1, t_r_case1)
# 时间值取反
t_case1_reverse = t_case1[::-1]


# case1
B1_case1 = 0.5
B2_case1 = -0.5
k2_case1 = 25
y_t1_d = A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (t_d_case1 - x1_short)))
y_t1_r = A2 + (k2_case1 - A2) / (1 + np.exp(B2_case1 * (t_r_case1 - x2_short)))
y_t1 = np.append(y_t1_d, y_t1_r)

# y值左右
y_t1_reverse = y_t1[::-1]


# case2
B1_case2 = 0.5
B2_case2 = -0.5
k2_case2 = 30
y_t2_d = A1 + (k1 - A1) / (1 + np.exp(B1_case2 * (t_d_case1 - x1_short)))
y_t2_r = A2 + (k2_case2 - A2) / (1 + np.exp(B2_case2 * (t_r_case1 - x2_short)))
y_t2 = np.append(y_t2_d, y_t2_r)

# y值左右
y_t2_reverse = y_t2[::-1]


# case3
B1_case3 = 0.5
B2_case3 = -0.5
k2_case3 = 35
y_t3_d = A1 + (k1 - A1) / (1 + np.exp(B1_case3 * (t_d_case1 - x1_short)))
y_t3_r = A2 + (k2_case3 - A2) / (1 + np.exp(B2_case3 * (t_r_case1 - x2_short)))
y_t3 = np.append(y_t3_d, y_t3_r)

# y值左右
y_t3_reverse = y_t3[::-1]


# case4
B1_case4 = 0.5
B2_case4 = -0.5
k2_case4 = 40
y_t4_d = A1 + (k1 - A1) / (1 + np.exp(B1_case4 * (t_d_case1 - x1_short)))
y_t4_r = A2 + (k2_case4 - A2) / (1 + np.exp(B2_case4 * (t_r_case1 - x2_short)))
y_t4 = np.append(y_t4_d, y_t4_r)

# y值左右
y_t4_reverse = y_t4[::-1]

# case5
B1_case5 = 0.5
B2_case5 = -0.5
k2_case5 = 45
y_t5_d = A1 + (k1 - A1) / (1 + np.exp(B1_case5 * (t_d_case1 - x1_short)))
y_t5_r = A2 + (k2_case5 - A2) / (1 + np.exp(B2_case5 * (t_r_case1 - x2_short)))
y_t5 = np.append(y_t5_d, y_t5_r)

# y值左右
y_t5_reverse = y_t5[::-1]


# case6
B1_case6 = 0.5
B2_case6 = -0.5
k2_case6 = 50
y_t6_d = A1 + (k1 - A1) / (1 + np.exp(B1_case6 * (t_d_case1 - x1_short)))
y_t6_r = A2 + (k2_case6 - A2) / (1 + np.exp(B2_case6 * (t_r_case1 - x2_short)))
y_t6 = np.append(y_t6_d, y_t6_r)

# y值左右
y_t6_reverse = y_t6[::-1]


#############################
t_d_case2 = np.arange(0, 100, 0.1)
t_r_case2 = np.arange(100, 200, 0.1)
t_case2 = np.append(t_d_case2, t_r_case2)
t_case2_reverse = t_case2[::-1]


# 调整x1 和 x2
x1_long = 50
x2_long = 140

# case7
B1_case7 = 0.5
B2_case7 = -0.5
k2_case7 = 25
y_t7_d = A1 + (k1 - A1) / (1 + np.exp(B1_case7 * (t_d_case2 - x1_long)))
y_t7_r = A2 + (k2_case7 - A2) / (1 + np.exp(B2_case7 * (t_r_case2 - x2_long)))
y_t7 = np.append(y_t7_d, y_t7_r)

y_t7_reverse = y_t7[::-1]

# case8
B1_case8 = 0.5
B2_case8 = -0.5
k2_case8 = 30
y_t8_d = A1 + (k1 - A1) / (1 + np.exp(B1_case8 * (t_d_case2 - x1_long)))
y_t8_r = A2 + (k2_case8 - A2) / (1 + np.exp(B2_case8 * (t_r_case2 - x2_long)))
y_t8 = np.append(y_t8_d, y_t8_r)

y_t8_reverse = y_t8[::-1]


# case9
B1_case9 = 0.5
B2_case9 = -0.5
k2_case9 = 35
y_t9_d = A1 + (k1 - A1) / (1 + np.exp(B1_case9 * (t_d_case2 - x1_long)))
y_t9_r = A2 + (k2_case9 - A2) / (1 + np.exp(B2_case9 * (t_r_case2 - x2_long)))
y_t9 = np.append(y_t9_d, y_t9_r)

y_t9_reverse = y_t9[::-1]


# case10
B1_case10 = 0.5
B2_case10 = -0.5
k2_case10 = 40
y_t10_d = A1 + (k1 - A1) / (1 + np.exp(B1_case10 * (t_d_case2 - x1_long)))
y_t10_r = A2 + (k2_case10 - A2) / (1 + np.exp(B2_case10 * (t_r_case2 - x2_long)))
y_t10 = np.append(y_t10_d, y_t10_r)

y_t10_reverse = y_t10[::-1]


# case11
B1_case11 = 0.5
B2_case11 = -0.5
k2_case11 = 45
y_t11_d = A1 + (k1 - A1) / (1 + np.exp(B1_case11 * (t_d_case2 - x1_long)))
y_t11_r = A2 + (k2_case11 - A2) / (1 + np.exp(B2_case11 * (t_r_case2 - x2_long)))
y_t11 = np.append(y_t11_d, y_t11_r)

y_t11_reverse = y_t11[::-1]

# case12
B1_case12 = 0.5
B2_case12 = -0.5
k2_case12 = 50
y_t12_d = A1 + (k1 - A1) / (1 + np.exp(B1_case12 * (t_d_case2 - x1_long)))
y_t12_r = A2 + (k2_case12 - A2) / (1 + np.exp(B2_case12 * (t_r_case2 - x2_long)))
y_t12 = np.append(y_t12_d, y_t12_r)

y_t12_reverse = y_t12[::-1]


# 然后复现出Cheng的方法

from scipy import integrate
import math


omega = 0.6

# 绝对时间
# 指的是绝对时间
B = 30


###################################################

# 抵抗阶段和恢复阶段比例
alpha = 0.5
y_min = 20
y_o = 50


# Case 1
# 恢复的稳态值时间
t_ss1, min_var1 = tm.calculate(t_case1, y_t2)
# 毁伤前稳态时间
t_ss1_reverse, min_var1_reverse = tm.calculate(t_case1_reverse, y_t1_reverse)

# 抵抗期间的参数
delta_d_1 = integrate.quad(lambda x: (A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short)))), 0, 50)[0] / (50 * 50)
sigma_d_1 = 20 / 50
# 抵抗阶段B放在前面
rho_d_1 = math.pow(omega, B / (50 - t_ss1_reverse))

# 恢复期间参数
delta_r_1 = integrate.quad(lambda x: A2 + (k2_case1 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))), 50, 100)[0] / (
    50 * 50
)

# 在每个案例中需要修改
sigma_r_1 = 25 / 50
# 恢复阶段B放在后面
rho_r_1 = math.pow(omega, (t_ss1 - 50) / B)

print(
    "delta_d_1:{},sigma_d_1:{},rho_d_1:{},---,delta_r_1:{},sigma_r_1:{},rho_r_1:{}".format(
        delta_d_1, sigma_d_1, rho_d_1, delta_r_1, sigma_r_1, rho_r_1
    )
)

# 韧性R
R_1 = alpha * delta_d_1 * sigma_d_1 * rho_d_1 + (1 - alpha) * delta_r_1 * sigma_r_1 * rho_r_1
print("R_value_1:{}".format(R_1))

# Case 2
# 恢复的稳态值时间
# 在case1 - case6中，t_case1和t_case1_reverse是基本的时间线，不能动, x1_short

t_ss2, min_var2 = tm.calculate(t_case1, y_t2)
# 毁伤前稳态时间
t_ss2_reverse, min_var2_reverse = tm.calculate(t_case1_reverse, y_t2_reverse)

# 抵抗期间的参数
delta_d_2 = integrate.quad(lambda x: (A1 + (k1 - A1) / (1 + np.exp(B1_case2 * (x - x1_short)))), 0, 50)[0] / (50 * 50)
sigma_d_2 = 20 / 50
# 抵抗阶段B放在前面
rho_d_2 = math.pow(omega, B / (50 - t_ss2_reverse))

# 恢复期间参数,这个k2_case2是恢复后的稳定水平需要修改
delta_r_2 = integrate.quad(lambda x: A2 + (k2_case2 - A2) / (1 + np.exp(B2_case2 * (x - x2_short))), 50, 100)[0] / (
    50 * 50
)

# 在每个案例中需要修改
sigma_r_2 = k2_case2 / 50
# 恢复阶段B放在后面
rho_r_2 = math.pow(omega, (t_ss2 - 50) / B)

print(
    "delta_d_2:{},sigma_d_2:{},rho_d_2:{},---,delta_r_2:{},sigma_r_2:{},rho_r_2:{}".format(
        delta_d_2, sigma_d_2, rho_d_2, delta_r_2, sigma_r_2, rho_r_2
    )
)

# 韧性R
R_2 = alpha * delta_d_2 * sigma_d_2 * rho_d_2 + (1 - alpha) * delta_r_2 * sigma_r_2 * rho_r_2
print("R_value_2:{}".format(R_2))

# Case3
# 恢复的稳态值时间
# 在case1 - case6中，t_case1和t_case1_reverse是基本的时间线，不能动, x1_short和x2_short需要更改

t_ss3, min_var3 = tm.calculate(t_case1, y_t3)
# 毁伤前稳态时间
t_ss3_reverse, min_var3_reverse = tm.calculate(t_case1_reverse, y_t3_reverse)

# 抵抗期间的参数
delta_d_3 = integrate.quad(lambda x: (A1 + (k1 - A1) / (1 + np.exp(B1_case3 * (x - x1_short)))), 0, 50)[0] / (50 * 50)
sigma_d_3 = 20 / 50
# 抵抗阶段B放在前面
rho_d_3 = math.pow(omega, B / (50 - t_ss3_reverse))

# 恢复期间参数,这个k2_case2是恢复后的稳定水平需要修改
delta_r_3 = integrate.quad(lambda x: A2 + (k2_case3 - A2) / (1 + np.exp(B2_case3 * (x - x2_short))), 50, 100)[0] / (
    50 * 50
)

# 在每个案例中需要修改
sigma_r_3 = k2_case3 / 50
# 恢复阶段B放在后面
rho_r_3 = math.pow(omega, (t_ss3 - 50) / B)

print(
    "delta_d_3:{},sigma_d_3:{},rho_d_3:{},---,delta_r_3:{},sigma_r_3:{},rho_r_3:{}".format(
        delta_d_3, sigma_d_3, rho_d_3, delta_r_3, sigma_r_3, rho_r_3
    )
)

# 韧性R
R_3 = alpha * delta_d_3 * sigma_d_3 * rho_d_3 + (1 - alpha) * delta_r_3 * sigma_r_3 * rho_r_3
print("R_value_3:{}".format(R_3))

# Case4
# 在case1 - case6中，t_case1和t_case1_reverse是基本的时间线，不能动, x1_short和x2_short需要更改

t_ss4, min_var4 = tm.calculate(t_case1, y_t4)
# 毁伤前稳态时间
t_ss4_reverse, min_var4_reverse = tm.calculate(t_case1_reverse, y_t4_reverse)

# 抵抗期间的参数
delta_d_4 = integrate.quad(lambda x: (A1 + (k1 - A1) / (1 + np.exp(B1_case4 * (x - x1_short)))), 0, 50)[0] / (50 * 50)
sigma_d_4 = 20 / 50
# 抵抗阶段B放在前面
rho_d_4 = math.pow(omega, B / (50 - t_ss4_reverse))

# 恢复期间参数,这个k2_case4是恢复后的稳定水平需要修改
delta_r_4 = integrate.quad(lambda x: A2 + (k2_case4 - A2) / (1 + np.exp(B2_case4 * (x - x2_short))), 50, 100)[0] / (
    50 * 50
)

# 在每个案例中需要修改
sigma_r_4 = k2_case4 / 50
# 恢复阶段B放在后面
rho_r_4 = math.pow(omega, (t_ss4 - 50) / B)

print(
    "delta_d_4:{},sigma_d_4:{},rho_d_4:{},---,delta_r_4:{},sigma_r_4:{},rho_r_4:{}".format(
        delta_d_4, sigma_d_4, rho_d_4, delta_r_4, sigma_r_4, rho_r_4
    )
)

# 韧性R
R_4 = alpha * delta_d_4 * sigma_d_4 * rho_d_4 + (1 - alpha) * delta_r_4 * sigma_r_4 * rho_r_4
print("R_value_4:{}".format(R_4))

# Case5
t_ss5, min_var5 = tm.calculate(t_case1, y_t5)
# 毁伤前稳态时间
t_ss5_reverse, min_var5_reverse = tm.calculate(t_case1_reverse, y_t5_reverse)

# 抵抗期间的参数
delta_d_5 = integrate.quad(lambda x: (A1 + (k1 - A1) / (1 + np.exp(B1_case5 * (x - x1_short)))), 0, 50)[0] / (50 * 50)
sigma_d_5 = 20 / 50
# 抵抗阶段B放在前面
rho_d_5 = math.pow(omega, B / (50 - t_ss5_reverse))

# 恢复期间参数,这个k2_case4是恢复后的稳定水平需要修改
delta_r_5 = integrate.quad(lambda x: A2 + (k2_case5 - A2) / (1 + np.exp(B2_case5 * (x - x2_short))), 50, 100)[0] / (
    50 * 50
)

# 在每个案例中需要修改
sigma_r_5 = k2_case5 / 50
# 恢复阶段B放在后面
rho_r_5 = math.pow(omega, (t_ss5 - 50) / B)

print(
    "delta_d_5:{},sigma_d_5:{},rho_d_5:{},---,delta_r_5:{},sigma_r_5:{},rho_r_5:{}".format(
        delta_d_5, sigma_d_5, rho_d_5, delta_r_5, sigma_r_5, rho_r_5
    )
)

# 韧性R
R_5 = alpha * delta_d_5 * sigma_d_5 * rho_d_5 + (1 - alpha) * delta_r_5 * sigma_r_5 * rho_r_5
print("R_value_5:{}".format(R_5))

# Case 6
t_ss6, min_var6 = tm.calculate(t_case1, y_t6)
# 毁伤前稳态时间
t_ss6_reverse, min_var6_reverse = tm.calculate(t_case1_reverse, y_t6_reverse)

# 抵抗期间的参数
delta_d_6 = integrate.quad(lambda x: (A1 + (k1 - A1) / (1 + np.exp(B1_case6 * (x - x1_short)))), 0, 50)[0] / (50 * 50)
sigma_d_6 = 20 / 50
# 抵抗阶段B放在前面
rho_d_6 = math.pow(omega, B / (50 - t_ss6_reverse))

# 恢复期间参数,这个k2_case4是恢复后的稳定水平需要修改
delta_r_6 = integrate.quad(lambda x: A2 + (k2_case6 - A2) / (1 + np.exp(B2_case6 * (x - x2_short))), 50, 100)[0] / (
    50 * 50
)

# 在每个案例中需要修改
sigma_r_6 = k2_case6 / 50
# 恢复阶段B放在后面
rho_r_6 = math.pow(omega, (t_ss6 - 50) / B)

print(
    "delta_d_6:{},sigma_d_6:{},rho_d_6:{},---,delta_r_6:{},sigma_r_6:{},rho_r_6:{}".format(
        delta_d_6, sigma_d_6, rho_d_6, delta_r_6, sigma_r_6, rho_r_6
    )
)

# 韧性R
R_6 = alpha * delta_d_6 * sigma_d_6 * rho_d_6 + (1 - alpha) * delta_r_6 * sigma_r_6 * rho_r_6
print("R_value_6:{}".format(R_6))


# Case 7-12
# Case 7 - 12 需要调整时间轴，时间需要由t_case1，t_case1_reverse调整为t_case2, t_case2_reverse
# Case 7
t_ss7, min_var7 = tm.calculate(t_case2, y_t7)
# 毁伤前稳态时间
t_ss7_reverse, min_var7_reverse = tm.calculate(t_case2_reverse, y_t7_reverse)

# 抵抗期间的参数
# x1_short和x2_shrot,需要改成x1_long和x2_long，另外积分的范围也得改变，前部分改为0-100，后半部分改成100-200
delta_d_7 = integrate.quad(lambda x: (A1 + (k1 - A1) / (1 + np.exp(B1_case7 * (x - x1_long)))), 0, 100)[0] / (100 * 50)
sigma_d_7 = 20 / 50
# 抵抗阶段B放在前面，时间拉长了，时间需要更改，50需要改成100
rho_d_7 = math.pow(omega, B / (100 - t_ss7_reverse))

# 恢复期间参数,这个k2_case4是恢复后的稳定水平需要修改，同样50-100，需要改成100-200, x2_short需要改成x2_long
delta_r_7 = integrate.quad(lambda x: A2 + (k2_case7 - A2) / (1 + np.exp(B2_case7 * (x - x2_long))), 100, 200)[0] / (
    100 * 50
)

# 在每个案例中需要修改
sigma_r_7 = k2_case7 / 50
# 恢复阶段B放在后面,时间由50改为100
rho_r_7 = math.pow(omega, (t_ss7 - 100) / B)

print(
    "delta_d_7:{},sigma_d_7:{},rho_d_7:{},---,delta_r_7:{},sigma_r_7:{},rho_r_7:{}".format(
        delta_d_7, sigma_d_7, rho_d_7, delta_r_7, sigma_r_7, rho_r_7
    )
)

# 韧性R
R_7 = alpha * delta_d_7 * sigma_d_7 * rho_d_7 + (1 - alpha) * delta_r_7 * sigma_r_7 * rho_r_7
print("R_value_6:{}".format(R_7))

# Case8
t_ss8, min_var8 = tm.calculate(t_case2, y_t8)
# 毁伤前稳态时间
t_ss8_reverse, min_var8_reverse = tm.calculate(t_case2_reverse, y_t8_reverse)

# 抵抗期间的参数
# x1_short和x2_shrot,需要改成x1_long和x2_long，另外积分的范围也得改变，前部分改为0-100，后半部分改成100-200
delta_d_8 = integrate.quad(lambda x: (A1 + (k1 - A1) / (1 + np.exp(B1_case8 * (x - x1_long)))), 0, 100)[0] / (100 * 50)
sigma_d_8 = 20 / 50
# 抵抗阶段B放在前面，时间拉长了，时间需要更改，50需要改成100
rho_d_8 = math.pow(omega, B / (100 - t_ss8_reverse))

# 恢复期间参数,这个k2_case4是恢复后的稳定水平需要修改，同样50-100，需要改成100-200, x2_short需要改成x2_long
delta_r_8 = integrate.quad(lambda x: A2 + (k2_case8 - A2) / (1 + np.exp(B2_case8 * (x - x2_long))), 100, 200)[0] / (
    100 * 50
)

# 在每个案例中需要修改
sigma_r_8 = k2_case8 / 50
# 恢复阶段B放在后面,时间由50改为100
rho_r_8 = math.pow(omega, (t_ss8 - 100) / B)

print(
    "delta_d_8:{},sigma_d_8:{},rho_d_8:{},---,delta_r_8:{},sigma_r_8:{},rho_r_8:{}".format(
        delta_d_8, sigma_d_8, rho_d_8, delta_r_8, sigma_r_8, rho_r_8
    )
)

# 韧性R
R_8 = alpha * delta_d_8 * sigma_d_8 * rho_d_8 + (1 - alpha) * delta_r_8 * sigma_r_8 * rho_r_8
print("R_value_8:{}".format(R_8))

# Case9
t_ss9, min_var9 = tm.calculate(t_case2, y_t9)
# 毁伤前稳态时间
t_ss9_reverse, min_var9_reverse = tm.calculate(t_case2_reverse, y_t9_reverse)

# 抵抗期间的参数
# x1_short和x2_shrot,需要改成x1_long和x2_long，另外积分的范围也得改变，前部分改为0-100，后半部分改成100-200
delta_d_9 = integrate.quad(lambda x: (A1 + (k1 - A1) / (1 + np.exp(B1_case9 * (x - x1_long)))), 0, 100)[0] / (100 * 50)
sigma_d_9 = 20 / 50
# 抵抗阶段B放在前面，时间拉长了，时间需要更改，50需要改成100
rho_d_9 = math.pow(omega, B / (100 - t_ss9_reverse))

# 恢复期间参数,这个k2_case4是恢复后的稳定水平需要修改，同样50-100，需要改成100-200, x2_short需要改成x2_long
delta_r_9 = integrate.quad(lambda x: A2 + (k2_case9 - A2) / (1 + np.exp(B2_case9 * (x - x2_long))), 100, 200)[0] / (
    100 * 50
)

# 在每个案例中需要修改
sigma_r_9 = k2_case9 / 50
# 恢复阶段B放在后面,时间由50改为100
rho_r_9 = math.pow(omega, (t_ss9 - 100) / B)

print(
    "delta_d_9:{},sigma_d_9:{},rho_d_9:{},---,delta_r_9:{},sigma_r_9:{},rho_r_9:{}".format(
        delta_d_9, sigma_d_9, rho_d_9, delta_r_9, sigma_r_9, rho_r_9
    )
)

# 韧性R
R_9 = alpha * delta_d_9 * sigma_d_9 * rho_d_9 + (1 - alpha) * delta_r_9 * sigma_r_9 * rho_r_9
print("R_value_9:{}".format(R_9))

# Case10
t_ss10, min_var10 = tm.calculate(t_case2, y_t10)
# 毁伤前稳态时间
t_ss10_reverse, min_var10_reverse = tm.calculate(t_case2_reverse, y_t10_reverse)

# 抵抗期间的参数
# x1_short和x2_shrot,需要改成x1_long和x2_long，另外积分的范围也得改变，前部分改为0-100，后半部分改成100-200
delta_d_10 = integrate.quad(lambda x: (A1 + (k1 - A1) / (1 + np.exp(B1_case10 * (x - x1_long)))), 0, 100)[0] / (100 * 50)
sigma_d_10 = 20 / 50
# 抵抗阶段B放在前面，时间拉长了，时间需要更改，50需要改成100
rho_d_10 = math.pow(omega, B / (100 - t_ss10_reverse))

# 恢复期间参数,这个k2_case4是恢复后的稳定水平需要修改，同样50-100，需要改成100-200, x2_short需要改成x2_long
delta_r_10 = integrate.quad(lambda x: A2 + (k2_case10 - A2) / (1 + np.exp(B2_case10 * (x - x2_long))), 100, 200)[0] / (
    100 * 50
)

# 在每个案例中需要修改
sigma_r_10 = k2_case10 / 50
# 恢复阶段B放在后面,时间由50改为100
rho_r_10 = math.pow(omega, (t_ss10 - 100) / B)

print(
    "delta_d_10:{},sigma_d_10:{},rho_d_10:{},---,delta_r_10:{},sigma_r_10:{},rho_r_10:{}".format(
        delta_d_10, sigma_d_10, rho_d_10, delta_r_10, sigma_r_10, rho_r_10
    )
)

# 韧性R
R_10 = alpha * delta_d_10 * sigma_d_10 * rho_d_10 + (1 - alpha) * delta_r_10 * sigma_r_10 * rho_r_10
print("R_value_10:{}".format(R_10))

