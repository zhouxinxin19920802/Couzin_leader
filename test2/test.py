##-*- coding:utf-8 -*-
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt

# B1 = 0.5
# x1 = 25
# A1 = 20
# K1 = 50
# z =  (K1 - A1)/(1 + math.exp(B1 * (70 - x1)))
# print(z)

# a = 1/(1 + math.sqrt(-0.25 * -14))
# cons = 0.675 * 0.75 * (0.2 + a + 1 - math.pow(a,(0.75 - 0.2)))
# print(cons)

# a = (5*1 + 5*0.2 + 20*0.75)/20
# # print(a)
# b = 0.75
# c = 0.2
# d = 20/20
# e = 1/(1 + math.exp(-0.25 * -14))
# r = a * b * (c + e + 1 - math.pow(d,b-c))
# print(r)
##########################
# # 方案一
# # 破坏前
# y_D = 16
# # 破坏后
# y_min = 4
#
# #恢复后
# y_R  = 11
# # 总性能占比
# a = (5*16 + 7*4 + 13*11)/(25*16)
#
# # 最低/正常
# b = y_min/y_D
#
# # 恢复时间因子
# c = 12 /25
#
# # 恢复后占比
# d = y_R / y_D
#
# # 易损因子
# e = 1/(math.exp(-0.25*(1-15)))
#
# cons = a * d * (b+e+1 - math.pow(c,(d-b)))
# print(cons)

# 方案二
# 破坏前
y_D = 16
# 破坏后
y_min = 4

# #恢复后
# y_R  = 16
# # 总性能占比
# a = (4*12 + 8 * 16)/(20*16)
#
# # 最低/正常
# b = y_min/y_D
#
# # 恢复时间因子
# c = 12/ 20
#
# # 恢复后占比
# d = y_R / y_D
#
# # 易损因子
# e = 1
#
# cons = a * d * (b+e+1 - math.pow(c,(d-b)))
# print(cons)

from scipy import integrate
# 尺度扩大一倍，面积占比一样
# A1 = 20
# k1 = 50
# x1_case1 = 25
# x2_case1 = 70
#
# # K2 是需要改变的
# A2 = 20
#
#
# # case1 时间
# t_d_case1 = np.arange(0,50,0.1)
# t_r_case1 = np.arange(50,100,0.1)
# t_case1 = np.append(t_d_case1,t_r_case1)
#
# # case1 函数曲线
# B1_case1 = 0.5
# B2_case1= -0.5
# k2_case1 = 25
# y_t1_d= A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (t_d_case1 - x1_case1)))
# y_t1_r= A2 + (k2_case1 - A2) / (1 + np.exp(B2_case1 * (t_r_case1 - x2_case1)))
# y_t1_case1 = np.append(y_t1_d,y_t1_r)
# print(y_t1_case1)

cons = np.ones(2)
print(cons)

