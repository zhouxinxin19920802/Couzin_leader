#-*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import math
import test.tool_methods as tm
import logging

#-*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import math
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='test.txt',
                    filemode='w',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
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

absolute_time = 30
# 任务值，在该任务值上以上才为有效值
task_value = 0

# case1的时间线
t_d_case1 = np.arange(0,50,0.1)
t_r_case1 = np.arange(50,100,0.1)
t_case1 = np.append(t_d_case1,t_r_case1)
# 时间值取反
t_case1_reverse = t_case1[::-1]



# case1
B1_case1 = 0.5
B2_case1= -0.5
k2_case1 = 25
y_t1_d= A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (t_d_case1 - x1_short)))
y_t1_r= A2 + (k2_case1 - A2) / (1 + np.exp(B2_case1 * (t_r_case1 - x2_short)))
y_t1 = np.append(y_t1_d,y_t1_r)

# y值左右
y_t1_reverse = y_t1[::-1]





# case2
B1_case2 = 0.5
B2_case2 = -0.5
k2_case2 = 30
y_t2_d= A1 + (k1 - A1) / (1 + np.exp(B1_case2 * (t_d_case1 - x1_short)))
y_t2_r= A2 + (k2_case2  - A2) / (1 + np.exp(B2_case2  * (t_r_case1 - x2_short)))
y_t2 = np.append(y_t2_d,y_t2_r)

# y值左右
y_t2_reverse = y_t2[::-1]


# case3
B1_case3 = 0.5
B2_case3 = -0.5
k2_case3 = 35
y_t3_d = A1 + (k1 - A1) / (1 + np.exp(B1_case3  * (t_d_case1 - x1_short)))
y_t3_r = A2 + (k2_case3 - A2) / (1 + np.exp(B2_case3 * (t_r_case1 - x2_short)))
y_t3 = np.append(y_t3_d,y_t3_r)

# y值左右
y_t3_reverse = y_t3[::-1]


# case4
B1_case4 = 0.5
B2_case4 = -0.5
k2_case4 = 40
y_t4_d = A1 + (k1 - A1) / (1 + np.exp(B1_case4  * (t_d_case1 - x1_short)))
y_t4_r= A2 + (k2_case4 - A2) / (1 + np.exp(B2_case4 * (t_r_case1 - x2_short)))
y_t4 = np.append(y_t4_d,y_t4_r)

# y值左右
y_t4_reverse = y_t4[::-1]

# case5
B1_case5 = 0.5
B2_case5 = -0.5
k2_case5 = 45
y_t5_d = A1 + (k1 - A1) / (1 + np.exp(B1_case5  * (t_d_case1 - x1_short)))
y_t5_r= A2 + (k2_case5 - A2) / (1 + np.exp(B2_case5 * (t_r_case1 - x2_short)))
y_t5 = np.append(y_t5_d,y_t5_r)

# y值左右
y_t5_reverse = y_t5[::-1]


# case6
B1_case6 = 0.5
B2_case6 = -0.5
k2_case6 = 50
y_t6_d = A1 + (k1 - A1) / (1 + np.exp(B1_case6  * (t_d_case1 - x1_short)))
y_t6_r= A2 + (k2_case6 - A2) / (1 + np.exp(B2_case6 * (t_r_case1 - x2_short)))
y_t6 = np.append(y_t6_d,y_t6_r)

# y值左右
y_t6_reverse = y_t6[::-1]


#############################
t_d_case2 = np.arange(0,100,0.1)
t_r_case2 = np.arange(100,200,0.1)
t_case2= np.append(t_d_case2,t_r_case2)
t_case2_reverse = t_case2[::-1]


# 调整x1 和 x2
x1_long = 50
x2_long = 140

# case7
B1_case7 = 0.5
B2_case7= -0.5
k2_case7 = 25
y_t7_d= A1 + (k1 - A1) / (1 + np.exp(B1_case7 * (t_d_case2 - x1_long)))
y_t7_r= A2 + (k2_case7 - A2) / (1 + np.exp(B2_case7 * (t_r_case2 - x2_long)))
y_t7 = np.append(y_t7_d,y_t7_r)

y_t7_reverse = y_t7[::-1]

# case8
B1_case8 = 0.5
B2_case8 = -0.5
k2_case8 = 30
y_t8_d= A1 + (k1 - A1) / (1 + np.exp(B1_case8 * (t_d_case2 - x1_long)))
y_t8_r= A2 + (k2_case8  - A2) / (1 + np.exp(B2_case8  * (t_r_case2 - x2_long)))
y_t8 = np.append(y_t8_d,y_t8_r)

y_t8_reverse = y_t8[::-1]


# case9
B1_case9 = 0.5
B2_case9 = -0.5
k2_case9 = 35
y_t9_d = A1 + (k1 - A1) / (1 + np.exp(B1_case9  * (t_d_case2 - x1_long)))
y_t9_r = A2 + (k2_case9 - A2) / (1 + np.exp(B2_case9 * (t_r_case2 - x2_long)))
y_t9 = np.append(y_t9_d,y_t9_r)

y_t9_reverse = y_t9[::-1]


# case10
B1_case10 = 0.5
B2_case10 = -0.5
k2_case10 = 40
y_t10_d = A1 + (k1 - A1) / (1 + np.exp(B1_case10  * (t_d_case2 - x1_long)))
y_t10_r = A2 + (k2_case10 - A2) / (1 + np.exp(B2_case10 * (t_r_case2 - x2_long)))
y_t10 = np.append(y_t10_d,y_t10_r)

y_t10_reverse = y_t10[::-1]



# case11
B1_case11 = 0.5
B2_case11 = -0.5
k2_case11 = 45
y_t11_d = A1 + (k1 - A1) / (1 + np.exp(B1_case11  * (t_d_case2 - x1_long)))
y_t11_r = A2 + (k2_case11 - A2) / (1 + np.exp(B2_case11 * (t_r_case2 - x2_long)))
y_t11 = np.append(y_t11_d,y_t11_r)

y_t11_reverse = y_t11[::-1]

# case12
B1_case12 = 0.5
B2_case12 = -0.5
k2_case12 = 50
y_t12_d = A1 + (k1 - A1) / (1 + np.exp(B1_case12  * (t_d_case2 - x1_long)))
y_t12_r= A2 + (k2_case12 - A2) / (1 + np.exp(B2_case12 * (t_r_case2 - x2_long)))
y_t12 = np.append(y_t12_d,y_t12_r)

y_t12_reverse = y_t12[::-1]

########################################################################################################################
# 改进韧性计算方方法
# 案例 1
from scipy import integrate

a1_d = integrate.quad(lambda x:(A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short)))),0,50)[0]
print("a1_d",a1_d)
a1_r = integrate.quad(lambda x:A2 + (k2_case1 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))),50,100)[0]
print("a1_r",a1_r)
#考虑任务性能，在任务性能以上有效性能，在任务性能以下时为
a1_d_test = integrate.quad(lambda x:(A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short)))) if (A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short))))> task_value else 0,0,50)[0]
print("a1_d_test",a1_d_test)
a1_r_test= integrate.quad(lambda x:A2 + (k2_case1 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))) if A2 + (k2_case1 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))) > task_value else 0,50,100)[0]
print("a1_r_test",a1_r_test)


sigma_test = (a1_d_test + a1_r_test)/(integrate.quad(lambda x:50,0,100)[0])
sigma1 = (a1_d + a1_r)/(integrate.quad(lambda x:50,0,100)[0])
print("sigma_test",sigma_test,"sigma1",sigma1)
rho1 = 25 / 50
delta1 = 20 / 50
delta1_improved = delta1


# delta1_improved =
zeta1 = 1
# 恢复的稳态值时间
t_ss1,min_var1 = tm.calculate(t_case1, y_t1)
# 毁伤前稳态时间
t_ss1_reverse,min_var1_reverse = tm.calculate(t_case1_reverse, y_t1_reverse)

tau1 = t_ss1/100
resilience1 = sigma1 * rho1 * (delta1 + zeta1 + 1 - pow(tau1,rho1 - delta1))
resilience1_improved = sigma1 * rho1 * (delta1_improved + zeta1 + 1 - pow(tau1,rho1 - delta1)) * tm.time_amend(t_ss1 - t_ss1_reverse,absolute_time)

print("t_ss1:{}\t,t_ss1_reverse:{}\t".format(t_ss1,t_ss1_reverse))

# print("resilience1:\t",resilience1,"sigma1:\t",sigma1,"tau1:\t",tau1)
print("resilience1:{}\t,sigma1:{}\t,tau1:{}\t".format(resilience1, sigma1, tau1))
print("improved_resilience1:{}\t".format(resilience1_improved))
#
#
#
# 案例2
a2_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case2 * (x - x1_short))),0,50)[0]
a2_r = integrate.quad(lambda x:A2 + (k2_case2 - A2) / (1 + np.exp(B2_case2 * (x - x2_short))),50,100)[0]
sigma2 = (a2_d + a2_r)/(integrate.quad(lambda x:50,0,100)[0])

rho2 = k2_case2 / 50
delta2 = 20 / 50
zeta2 = 1
t_ss2,min_var2 = tm.calculate(t_case1, y_t2 )

# 毁伤前稳态时间
t_ss2_reverse,min_var2_reverse = tm.calculate(t_case1_reverse, y_t2_reverse)

tau2 = t_ss2/100
resilience2 = sigma2 * rho2 * (delta2 + zeta2 + 1 - pow(tau2,rho2 - delta2))
resilience2_improved = sigma2 * rho2 * (delta1_improved + zeta2 + 1 - pow(tau2,rho2 - delta2)) * tm.time_amend(t_ss2 - t_ss2_reverse,absolute_time)


print("t_ss2:{}\t,t_ss2_reverse:{}\t".format(t_ss2,t_ss2_reverse))

# print("resilience2:\t",resilience2,"sigma2:\t",sigma2,"tau2:\t",tau2)
print("resilience2:{}\t,sigma2:{}\t,tau2:{}\t".format(resilience2, sigma2, tau2))
print("improved_resilience2:{}\t".format(resilience2_improved))

# 案例 3
a3_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short))),0,50)[0]
a3_r = integrate.quad(lambda x:A2 + (k2_case3 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))),50,100)[0]
sigma3 = (a3_d + a3_r)/(integrate.quad(lambda x:50,0,100)[0])
rho3 = k2_case3 / 50
delta3 = 20 / 50
zeta3 = 1
t_ss3,min_var3 = tm.calculate(t_case1, y_t3)
# 毁伤前稳态时间
t_ss3_reverse,min_var3_reverse = tm.calculate(t_case1_reverse, y_t3_reverse)
tau3 = t_ss3/100
resilience3 = sigma3 * rho3 * (delta3 + zeta3 + 1 - pow(tau3,rho3 - delta3))
resilience3_improved = sigma3 * rho3 * (delta1_improved + zeta3 + 1 - pow(tau3,rho3 - delta3)) * tm.time_amend(t_ss3 - t_ss3_reverse,absolute_time)

print("t_ss3:{}\t,t_ss3_reverse:{}\t".format(t_ss3,t_ss3_reverse))
# print("resilience3:\t",resilience3,"sigma3:\t",sigma3,"tau3:\t",tau3)
print("resilience3:{}\t,sigma3:{}\t,tau3:{}\t".format(resilience3, sigma3, tau3))
print("improved_resilience3:{}\t".format(resilience3_improved))

# 案例 4
a4_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short))),0,50)[0]
a4_r = integrate.quad(lambda x:A2 + (k2_case4 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))),50,100)[0]
sigma4 = (a4_d + a4_r)/(integrate.quad(lambda x:50,0,100)[0])
rho4 = k2_case4 / 50
delta4 = 20 / 50
zeta4 = 1
t_ss4,min_var4 = tm.calculate(t_case1, y_t4)
# 毁伤前稳态时间
t_ss4_reverse,min_var4_reverse = tm.calculate(t_case1_reverse, y_t4_reverse)
tau4 = t_ss4/100
resilience4 = sigma4 * rho4 * (delta4 + zeta4 + 1 - pow(tau4,rho4 - delta4))
resilience4_improved = sigma4 * rho4 * (delta1_improved + zeta4 + 1 - pow(tau4,rho4 - delta4)) * tm.time_amend(t_ss4 - t_ss4_reverse,absolute_time)
print("t_ss4:{}\t,t_ss4_reverse:{}\t".format(t_ss4,t_ss4_reverse))
# print("resilience4:\t",resilience4,"sigma4:\t",sigma4,"tau4:\t",tau4)
print("resilience4:{}\t,sigma4:{}\t,tau4:{}\t".format(resilience4, sigma4, tau4))
print("improved_resilience4:{}\t".format(resilience4_improved))


# 案例 5
a5_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short))),0,50)[0]
a5_r = integrate.quad(lambda x:A2 + (k2_case5 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))),50,100)[0]
sigma5 = (a5_d + a5_r)/(integrate.quad(lambda x:50,0,100)[0])

rho5 = k2_case5 / 50
delta5 = 20 / 50
zeta5 = 1
t_ss5,min_var5 = tm.calculate(t_case1, y_t5)
# 毁伤前稳态时间
t_ss5_reverse,min_var5_reverse = tm.calculate(t_case1_reverse, y_t5_reverse)
tau5 = t_ss5/100
resilience5 = sigma5 * rho5 * (delta5 + zeta5 + 1 - pow(tau5,rho5 - delta5))
resilience5_improved = sigma5 * rho5 * (delta1_improved + zeta5 + 1 - pow(tau5,rho5 - delta5)) * tm.time_amend(t_ss5 - t_ss5_reverse,absolute_time)
print("t_ss5:{}\t,t_ss5_reverse:{}\t".format(t_ss5,t_ss5_reverse))
# print("resilience5:\t",resilience5,"sigma5:\t",sigma5,"tau5:\t",tau5)
print("resilience5:{}\t,sigma5:{}\t,tau5:{}\t".format(resilience5, sigma5, tau5))
print("improved_resilience5:{}\t".format(resilience5_improved))


# 案例 6
a6_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short))) ,0,50)[0]
a6_r = integrate.quad(lambda x:A2 + (k2_case6 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))),50,100)[0]
sigma6 = (a6_d + a6_r)/(integrate.quad(lambda x:50,0,100)[0])
rho6 = k2_case6 / 50
delta6 = 20 / 50
zeta6 = 1
t_ss6,min_var6 = tm.calculate(t_case1, y_t6)
# 毁伤前稳态时间
t_ss6_reverse,min_var6_reverse = tm.calculate(t_case1_reverse, y_t6_reverse)

tau6 = t_ss6/100
resilience6 = sigma6 * rho6 * (delta6 + zeta6 + 1 - pow(tau6,rho6 - delta6))
resilience6_improved = sigma6 * rho6 * (delta1_improved + zeta6 + 1 - pow(tau6,rho6 - delta6)) * tm.time_amend(t_ss6 - t_ss6_reverse,absolute_time)

print("t_ss6:{}\t,t_ss6_reverse:{}\t".format(t_ss6,t_ss6_reverse))
# print("resilience6:\t",resilience6,"sigma6:\t",sigma6,"tau6:\t",tau6)
print("resilience6:{}\t,sigma6:{}\t,tau6:{}\t".format(resilience6, sigma6, tau6))

print("resilience_re:{}\t,amend:{}\t".format(sigma6 * rho6 * (delta1_improved + zeta6 + 1 - pow(tau6,rho6 - delta6)),tm.time_amend(t_ss6 - t_ss6_reverse,absolute_time)))
print("improved_resilience6:{}\t".format(resilience6_improved))
print("###############################################################################################################")

# 案例 7
a7_d =      integrate.quad(lambda x:(A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))))  if (A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))))> task_value else 0,0,100)[0]
a7_r =      integrate.quad(lambda x:(A2 + (k2_case7 - A2) / (1 + np.exp(B2_case1 * (x - x2_long)))) if (A2 + (k2_case7 - A2) / (1 + np.exp(B2_case1 * (x - x2_long)))) > task_value else 0 ,100,200)[0]
sigma7 = (a7_d + a7_r)/(integrate.quad(lambda x:50,0,200)[0])
rho7 = 25 / 50
delta7 = 20 / 50
zeta7 = 1

# 恢复的稳态值时间
t_ss7,min_var = tm.calculate(t_case2, y_t7)
# 毁伤前稳态时间
t_ss7_reverse,min_var7_reverse = tm.calculate(t_case2_reverse, y_t7_reverse)

tau7 = t_ss7/200
resilience7 = sigma7 * rho7 * (delta7 + zeta7 + 1 - pow(tau7,rho7 - delta7))
resilience7_improved = sigma7 * rho7 * (delta1_improved + zeta7 + 1 - pow(tau7,rho7 - delta7)) * tm.time_amend(t_ss7 - t_ss7_reverse,absolute_time)

print("t_ss7:{}\t,t_ss7_reverse:{}\t".format(t_ss7,t_ss7_reverse))
# print("resilience7:\t",resilience7,"sigma7:\t",sigma7,"tau7:\t",tau7)
print("resilience7:{}\t,sigma7:{}\t,tau7:{}\t".format(resilience7, sigma7, tau7))
print("improved_resilience7:{}\t".format(resilience7_improved))




# 案例 8
a8_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))),0,100)[0]
a8_r = integrate.quad(lambda x:A2 + (k2_case8 - A2) / (1 + np.exp(B2_case1 * (x - x2_long))),100,200)[0]
sigma8 = (a8_d + a8_r)/(integrate.quad(lambda x:50,0,200)[0])
rho8 = k2_case8 / 50
delta8 = 20 / 50
zeta8 = 1
t_ss8,min_var8 = tm.calculate(t_case2, y_t8)

# 毁伤前稳态时间
t_ss8_reverse,min_var8_reverse = tm.calculate(t_case2_reverse, y_t8_reverse)
tau8 = t_ss8/200
resilience8 = sigma8 * rho8 * (delta8 + zeta8 + 1 - pow(tau8,rho8 - delta8))
resilience8_improved = sigma8 * rho8 * (delta1_improved + zeta8 + 1 - pow(tau8,rho8 - delta8)) * tm.time_amend(t_ss8 - t_ss8_reverse,absolute_time)

print("t_ss8:{}\t,t_ss8_reverse:{}\t".format(t_ss8,t_ss8_reverse))
# print("resilience8:\t",resilience8,"sigma8:\t",sigma8,"tau8:\t",tau8)
print("resilience8:{}\t,sigma8:{}\t,tau8:{}\t".format(resilience8, sigma8, tau8))
print("improved_resilience8:{}\t".format(resilience8_improved))





# 案例 9
a9_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case9 * (x - x1_long))),0,100)[0]
a9_r = integrate.quad(lambda x:A2 + (k2_case9 - A2) / (1 + np.exp(B2_case9 * (x - x2_long))),100,200)[0]
sigma9 = (a9_d + a9_r)/(integrate.quad(lambda x:50,0,200)[0])
rho9 = k2_case9 / 50
delta9 = 20 / 50
zeta9 = 1
t_ss9,min_var9 = tm.calculate(t_case2, y_t9)
# 毁伤前稳态时间
t_ss9_reverse,min_var9_reverse = tm.calculate(t_case2_reverse, y_t9_reverse)
tau9 = t_ss9/200
resilience9 = sigma9 * rho9 * (delta9 + zeta9 + 1 - pow(tau9,rho9 - delta9))
resilience9_improved = sigma9 * rho9 * (delta1_improved + zeta9 + 1 - pow(tau9,rho9 - delta9)) * tm.time_amend(t_ss9 - t_ss9_reverse,absolute_time)

print("t_ss9:{}\t,t_ss9_reverse:{}\t".format(t_ss9,t_ss9_reverse))
# print("resilience9:\t",resilience9,"sigma9:\t",sigma9,"tau9:\t",tau9)
print("resilience9:{}\t,sigma9:{}\t,tau9:{}\t".format(resilience9, sigma9, tau9))
print("improved_resilience9:{}\t".format(resilience9_improved))



# 案例 20
a10_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))),0,100)[0]
a10_r = integrate.quad(lambda x:A2 + (k2_case10 - A2) / (1 + np.exp(B2_case1 * (x - x2_long))),100,200)[0]
sigma10 = (a10_d + a10_r)/(integrate.quad(lambda x:50,0,200)[0])

rho10 = k2_case10 / 50
delta10 = 20 / 50
zeta10 = 1
t_ss10,min_var10 = tm.calculate(t_case2, y_t10)

# 毁伤前稳态时间
t_ss10_reverse,min_var10_reverse = tm.calculate(t_case2_reverse, y_t10_reverse)

tau10 = t_ss10/200
resilience10 = sigma10 * rho10 * (delta10 + zeta10 + 1 - pow(tau10,rho10 - delta10))
resilience10_improved = sigma10 * rho10 * (delta1_improved + zeta10 + 1 - pow(tau10,rho10 - delta10)) * tm.time_amend(t_ss10 - t_ss10_reverse,absolute_time)

print("t_ss10:{}\t,t_ss10_reverse:{}\t".format(t_ss10,t_ss10_reverse))
# print("resilience10:\t",resilience10,"sigma10:\t",sigma10,"tau10:\t",tau10)
print("resilience10:{}\t,sigma10:{}\t,tau10:{}\t".format(resilience10, sigma10, tau10))
print("improved_resilience10:{}\t".format(resilience10_improved))


# 案例 11
a11_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))),0,100)[0]
a11_r = integrate.quad(lambda x:A2 + (k2_case11 - A2) / (1 + np.exp(B2_case1 * (x - x2_long))),100,200)[0]
sigma11 = (a11_d + a11_r)/(integrate.quad(lambda x:50,0,200)[0])

rho11 = k2_case11/ 50
delta11 = 20 / 50
zeta11 = 1
t_ss11,min_var11 = tm.calculate(t_case2, y_t11)

# 毁伤前稳态时间
t_ss11_reverse,min_var11_reverse = tm.calculate(t_case2_reverse, y_t11_reverse)

tau11 = t_ss11/200
resilience11 = sigma11 * rho11 * (delta11 + zeta11 + 1 - pow(tau11,rho11 - delta11))
resilience11_improved = sigma11 * rho11 * (delta1_improved + zeta11 + 1 - pow(tau11,rho11 - delta11)) * tm.time_amend(t_ss11 - t_ss11_reverse,absolute_time)


print("t_ss11:{}\t,t_ss11_reverse:{}\t".format(t_ss11,t_ss11_reverse))
# print("resilience11:\t",resilience11,"sigma11:\t",sigma11,"tau11:\t",tau11)
print("resilience11:{}\t,sigma11:{}\t,tau11:{}\t".format(resilience11, sigma11, tau11))
print("improved_resilience11:{}\t".format(resilience11_improved))



# 案例 12
a12_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))),0,100)[0]
a12_r = integrate.quad(lambda x:A2 + (k2_case12 - A2) / (1 + np.exp(B2_case1 * (x - x2_long))),100,200)[0]
sigma12 = (a12_d + a12_r)/(integrate.quad(lambda x:50,0,200)[0])
rho12 = k2_case12/ 50
delta12 = 20 / 50
zeta12 = 1
t_ss12,min_var12 = tm.calculate(t_case2, y_t12)
# 毁伤前稳态时间
t_ss12_reverse,min_var12_reverse = tm.calculate(t_case2_reverse, y_t12_reverse)

tau12 = t_ss12/200
resilience12 = sigma12 * rho12 * (delta12 + zeta12 + 1 - pow(tau12,rho12 - delta12))
resilience12_improved = sigma12 * rho12 * (delta1_improved + zeta12 + 1 - pow(tau12,rho12 - delta12)) * tm.time_amend(t_ss12 - t_ss12_reverse,absolute_time)

print("t_ss12:{}\t,t_ss12_reverse:{}\t".format(t_ss12,t_ss12_reverse))
# print("resilience12:\t",resilience12,"sigma12:\t",sigma12,"tau12:\t",tau12)
print("resilience12:{}\t,sigma12:{}\t,tau12:{}\t".format(resilience12, sigma12, tau12))
print("improved_resilience12:{}\t".format(resilience12_improved ))


#
# plt.subplot2grid((3,2),(0,0),colspan=2)

#
# plt.plot(t_case1,y_t1,marker="d",color="c",ls="-",lw=0.005,label="case1 k2=25")
# plt.plot(t_case1,y_t2,marker="d",color="g",ls="-",lw=0.005,label="case2 k2=30")
# plt.plot(t_case1,y_t3,marker="d",color="b",ls="-",lw=0.005,label="case3 k2=35")
# plt.plot(t_case1,y_t4,marker="d",color="m",ls="-",lw=0.005,label="case4 k2=40")
# plt.plot(t_case1,y_t5,marker="d",color="y",ls="-",lw=0.005,label="case5 k2=45")
# plt.plot(t_case1,y_t6,marker="d",color="k",ls="-",lw=0.005,label="case6 k2=50")
# # case 2
# plt.plot(t_case2,y_t7,marker="d",color="r",ls="-",lw=0.005,label="case7 k2=25")
# plt.plot(t_case2,y_t8,marker="d",color="g",ls="-",lw=0.005,label="case8 k2=30")
# plt.plot(t_case2,y_t9,marker="d",color="b",ls="-",lw=0.005,label="case9 k2=35")
# plt.plot(t_case2,y_t10,marker="d",color="m",ls="-",lw=0.005,label="case10 k2=40")
# plt.plot(t_case2,y_t11,marker="d",color="y",ls="-",lw=0.005,label="case11 k2=45")
# plt.plot(t_case2,y_t12,marker="d",color="k",ls="-",lw=0.005,label="case12 k2=50")


plt.plot(t_case1,y_t1,marker="d",color="c",ls="-",lw=0.005,label="case1 k2=25")
plt.plot(t_case1,y_t2,marker="d",color="g",ls="-",lw=0.005,label="case2 k2=30")
plt.plot(t_case1,y_t3,marker="d",color="b",ls="-",lw=0.005,label="case3 k2=35")
plt.plot(t_case1,y_t4,marker="d",color="m",ls="-",lw=0.005,label="case4 k2=40")
plt.plot(t_case1,y_t5,marker="d",color="y",ls="-",lw=0.005,label="case5 k2=45")
plt.plot(t_case1,y_t6,marker="d",color="k",ls="-",lw=0.005,label="case6 k2=50")
# case 2
plt.plot(t_case2,y_t7,marker="d",color="r",ls="-",label="case7 k2=25")
plt.plot(t_case2,y_t8,marker="d",color="brown",lw=0.005,ls="-",label="case8 k2=30")
plt.plot(t_case2,y_t9,marker="d",color="salmon",lw=0.005,ls="-",label="case9 k2=35")
plt.plot(t_case2,y_t10,marker="d",color="deepskyblue",lw=0.005,ls="-",label="case10 k2=40")
plt.plot(t_case2,y_t11,marker="d",color="orchid",lw=0.005,ls="-",label="case11 k2=45")
plt.plot(t_case2,y_t12,marker="d",color="pink",lw=0.005,ls="-",label="case12 k2=50")

ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")


# plt.plot(t_case2,np.ones(len(t_case2))*task_value,marker="d",linewidth=0.005)

plt.legend(fontsize=20,loc="lower center",ncol=3)
plt.xticks(np.arange(0,210,50),fontsize=20)
plt.yticks(np.arange(0,70,10),fontsize=20)


# # 图2中，红色为1-6
# plt.subplot2grid((3,2),(1,0),colspan=2)
#
# case1_mark_num = [25,30,35,40,45,50]
# cas1_resilience_cons =[resilience1,resilience2,resilience3,resilience4,resilience5,resilience6]
# cas2_resilience_cons =[resilience7,resilience8,resilience9,resilience10,resilience11,resilience12]

# plt.plot(case1_mark_num,cas1_resilience_cons,marker="d",color="r",lw=0.01,label="resilience_case1")
#
# plt.scatter(case1_mark_num,cas1_resilience_cons,c="r",s=20,label="resilience_case1")
# plt.scatter(case1_mark_num,cas2_resilience_cons,c="b",s=20,label="resilience_case2")
# plt.xticks(np.arange(20,55,5),fontsize=20)
# plt.yticks(np.arange(0,1.5,0.2),fontsize=20)
# plt.legend(fontsize=15)

# 第三张图
# plt.subplot2grid((3,2),(2,0),colspan=2)
#
# cas1_resilience_cons_improved =[resilience1_improved,resilience2_improved,resilience3_improved,resilience4_improved,resilience5_improved,resilience6_improved]
# cas2_resilience_cons_improved =[resilience7_improved,resilience8_improved,resilience9_improved,resilience10_improved,resilience11_improved,resilience12_improved]

# plt.plot(case1_mark_num,cas1_resilience_cons,marker="d",color="r",lw=0.01,label="resilience_case1")

# plt.scatter(case1_mark_num,cas1_resilience_cons_improved,c="r",s=20,label="resilience_case1")
# plt.scatter(case1_mark_num,cas2_resilience_cons_improved,c="b",s=20,label="resilience_case2")
# plt.xticks(np.arange(20,55,5),fontsize=20)
# plt.yticks(np.arange(0,1.5,0.2),fontsize=20)



plt.show()

