#-*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import math



step = 0.001

# case1
x1_before = np.arange(0,1,step)
x1_resist = np.arange(1,2,step)
x1_recover = np.arange(2,3,step)
x1_after = np.arange(3,4,step)

x1 = np.append(x1_before,x1_resist)
x1 = np.append(x1,x1_recover)
x1 = np.append(x1,x1_after)


y1_before = 2*np.ones(len(x1_before))
y1_resist = 2-pow(x1_resist-1,2)
y1_recover = 1 + pow(x1_recover-2,2)
y1_after = 2*np.ones(len(x1_after))

y1 = np.append(y1_before,y1_resist)
y1 = np.append(y1, y1_recover)
y1 = np.append(y1,y1_after)

# case2
x2_before = np.arange(0,1,step)
x2_resist = np.arange(1,2,step)
x2_recover = np.arange(2,3,step)
x2_after = np.arange(3,4,step)

x2 = np.append(x2_before,x2_resist)
x2 = np.append(x2,x2_recover)
x2 = np.append(x2,x2_after)


y2_before = 2*np.ones(len(x2_before))
y2_resist = 3 - x2_resist
y2_recover = x2_recover - 1
y2_after = 2*np.ones(len(x2_after))

y2 = np.append(y2_before,y2_resist)
y2 = np.append(y2, y2_recover)
y2 = np.append(y2,y2_after)

# case3
x3_before = np.arange(0,1,step)
x3_resist = np.arange(1,2,step)
x3_recover = np.arange(2,3,step)
x3_after = np.arange(3,4,step)

x3= np.append(x3_before,x3_resist)
x3 = np.append(x3,x3_recover)
x3 = np.append(x3,x3_after)


y3_before = 2*np.ones(len(x3_before))
y3_resist = 1+pow(x3_resist-2,2)
y3_recover = 2 - pow(x3_recover-3,2)
y3_after = 2*np.ones(len(x3_after))

y3 = np.append(y3_before,y3_resist)
y3 = np.append(y3, y3_recover)
y3 = np.append(y3,y3_after)



plt.plot(x1,y1,marker="d",color="r",ls="-",lw=0.2,label="case1")
plt.plot(x2,y2,marker="d",color="g",ls="--",lw=0.2,label="case2")
plt.plot(x3,y3,marker="d",color="b",ls="-",lw=0.2,label="case3")

plt.axvspan(xmin=1,xmax=2,facecolor='y',alpha=0.3)
plt.axvspan(xmin=2,xmax=3,facecolor='g',alpha=0.3)

plt.xticks(np.arange(0,4,1),fontsize=25)
plt.yticks(np.arange(0,5,1),fontsize=25)
plt.xlim(0,4)
plt.ylim(0,3)
plt.legend(fontsize=25)

print("resilience calculation:")
# 积分计算求聪聪师兄韧性
from scipy import integrate

# 时间系数
a = 0.5
# 绝对时间尺度
B = 2

alpha_factor = 0.5
absolute_time = 2




beta_factor = 1 - alpha_factor

########################################################################################
# case1:韧性
# 抗毁过程因子
delta1_d = integrate.quad(lambda x:2-pow(x-1,2),1,2)[0]/integrate.quad(lambda x:2,1,2)[0]
# 抗毁状态因子
sigma1_d = 1/2
# # 抗毁时间因子
# rho1_d = math.pow(a,1/B)

# 抗毁过程因子
delta1_r = integrate.quad(lambda x:1+pow(x-2,2),2,3)[0]/integrate.quad(lambda x:2,2,3)[0]
# 抗毁状态因子
sigma1_r = 1/2
# # 抗毁时间因子
# rho1_r = math.pow(a,1/B)

# 绝对时间尺度因子
absolute_time_factor1 = math.exp((2 if absolute_time>B else absolute_time)/B - 1 )
cons1 = (alpha_factor * delta1_d * sigma1_d + beta_factor * delta1_r * sigma1_r) * absolute_time_factor1

print("case1:%s"%str(cons1))

########################################################################################
# case2:韧性
# 抗毁过程因子
delta2_d = integrate.quad(lambda x:3 - x,1,2)[0]/integrate.quad(lambda x:2,1,2)[0]
# 抗毁状态因子
sigma2_d = 1/2
# # 抗毁时间因子
# rho2_d = math.pow(a,B/1)

# 抗毁过程因子
delta2_r = integrate.quad(lambda x:x - 1,2,3)[0]/integrate.quad(lambda x:2,2,3)[0]
# 抗毁状态因子
sigma2_r = 1/2
# 抗毁时间因子
# rho2_r = math.pow(a,1/B)
absolute_time_factor2 = math.exp((2 if absolute_time>B else absolute_time)/B - 1)
cons2 = (alpha_factor * delta2_d * sigma2_d + beta_factor * delta2_r * sigma2_r) * absolute_time_factor2


print("case2:%s"%str(cons2))
########################################################################################
# case3:韧性
# 抗毁过程因子
delta3_d = integrate.quad(lambda x:1+pow(x-2,2),1,2)[0]/integrate.quad(lambda x:2,1,2)[0]
# 抗毁状态因子
sigma3_d = 1/2
# # 抗毁时间因子
# rho3_d = math.pow(a,B/1)

# 抗毁过程因子
delta3_r = integrate.quad(lambda x: 2 - pow(x-3,2),2,3)[0]/integrate.quad(lambda x:2,2,3)[0]
# 抗毁状态因子
sigma3_r = 1/2
# # 抗毁时间因子
# rho3_r = math.pow(a,1/B)
absolute_time_factor3 = math.exp((2 if absolute_time>B else absolute_time)/B - 1)
cons3 = (alpha_factor * delta3_d * sigma3_d + beta_factor * delta3_r * sigma3_r) * absolute_time_factor3

print("case3:%s"%cons3)


plt.grid(ls=":",lw=1,color="gray",alpha=0.5)
plt.show()


