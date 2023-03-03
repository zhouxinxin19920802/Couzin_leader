#-*- coding:utf-8 -*-

from scipy import integrate
import math
# def f(x):
#     return x**2
# cons = integrate.quad(f,0,2)
# print(cons)
import math

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline
# x = np.array([1,   2,  3,  4,   5,  6,  7])
# y = np.array([1.5, 2.5,2.2,2.9, 4.2,3.8,4.5])
# x_smooth = np.linspace(x.min(), x.max(), 300)  # np.linspace 等差数列,从x.min()到x.max()生成300个数，便于后续插值
# y_smooth = make_interp_spline(x, y)(x_smooth)
# plt.plot(x_smooth, y_smooth,color="r",label="smooth")
# plt.plot(x, y,color="b")
# plt.xticks(fontsize=25)
# plt.yticks(fontsize=25)
# plt.legend(fontsize=25)
# plt.show()

# case1
# a = 0.5
# b = 0.5
#
# c = 0.8
# B = 2
#
# a0_d = (0.5*1/2+0.5*1)/(2*0.5)
# a1_d = 1/2
# a2_d = math.pow(c,B/0.5)
#
# b0_r = (1.5*1/2+1.5*1)/(1.5*2)
# b1_r = 1
# b2_r = math.pow(c,1.5/B)
#
# print(a*a0_d*a1_d*a2_d + b*b0_r*b1_r*b2_r)
#
# # case4
#
# e0_d = (1*1/2+1*1)/(1*2)
# e1_d = 1/2
# e2_d = math.pow(c,B/1)
#
# f0_r = (1.5*1/2+1.5*1)/(1.5*2)
# f1_r = 1
# f2_r = math.pow(c,B/1.5)
# print(a*e0_d*e1_d*e2_d + b*f0_r*f1_r*f2_r)

# 范式
# y_d = 2
# y_min = 1
# y_r = 2
#
# t_d = 1
# t_r = 2
# t_s = 3
#
# c = 0.8
# B = 2
#
# alfa = 0.5
# beta = 0.5
#
# h_d0 = ((y_d - y_min)*(t_r-t_d)/2 + (t_r-t_d)*y_min)/((t_r-t_d) * y_d)
# h_d1 = y_min / y_d
# h_d2 = math.pow(c,B/(t_r-t_d))
#
#
# i_d0 = ((y_d - y_min)*(t_s - t_r)/2 + (t_s - t_r)*y_min)/((t_s - t_r) * y_d)
# i_d1 = y_r / y_d
# i_d2 = math.pow(c,(t_s - t_r)/B)
#
# cons = alfa * h_d0 * h_d1 * h_d2 + beta * i_d0 * i_d1 * i_d2
# print(cons)

sigma_d = integrate.quad(lambda x:2-pow(x-1,2),1,2)
print(sigma_d )
