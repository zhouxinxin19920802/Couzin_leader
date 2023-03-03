#-*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import math
import tool_methods
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



# case1的时间线
t_d_case1 = np.arange(0,50,0.1)
t_r_case1 = np.arange(50,100,0.1)
t_case1 = np.append(t_d_case1,t_r_case1)


# case1
B1_case1 = 0.5
B2_case1= -0.5
k2_case1 = 25
y_t1_d= A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (t_d_case1 - x1_short)))
y_t1_r= A2 + (k2_case1 - A2) / (1 + np.exp(B2_case1 * (t_r_case1 - x2_short)))
y_t1 = np.append(y_t1_d,y_t1_r)

logging.info("stable_value:%s",str(A2 + (k2_case1 - A2) / (1 + np.exp(B2_case1 * (73.20000000000033- x2_short)))))



# case2
B1_case2 = 0.5
B2_case2 = -0.5
k2_case2 = 30
y_t2_d= A1 + (k1 - A1) / (1 + np.exp(B1_case2 * (t_d_case1 - x1_short)))
y_t2_r= A2 + (k2_case2  - A2) / (1 + np.exp(B2_case2  * (t_r_case1 - x2_short)))
y_t2 = np.append(y_t2_d,y_t2_r)



# case3
B1_case3 = 0.5
B2_case3 = -0.5
k2_case3 = 35
y_t3_d = A1 + (k1 - A1) / (1 + np.exp(B1_case3  * (t_d_case1 - x1_short)))
y_t3_r = A2 + (k2_case3 - A2) / (1 + np.exp(B2_case3 * (t_r_case1 - x2_short)))
y_t3 = np.append(y_t3_d,y_t3_r)

# case4
B1_case4 = 0.5
B2_case4 = -0.5
k2_case4 = 40
y_t4_d = A1 + (k1 - A1) / (1 + np.exp(B1_case4  * (t_d_case1 - x1_short)))
y_t4_r= A2 + (k2_case4 - A2) / (1 + np.exp(B2_case4 * (t_r_case1 - x2_short)))
y_t4 = np.append(y_t4_d,y_t4_r)

# case5
B1_case5 = 0.5
B2_case5 = -0.5
k2_case5 = 45
y_t5_d = A1 + (k1 - A1) / (1 + np.exp(B1_case5  * (t_d_case1 - x1_short)))
y_t5_r= A2 + (k2_case5 - A2) / (1 + np.exp(B2_case5 * (t_r_case1 - x2_short)))
y_t5 = np.append(y_t5_d,y_t5_r)

# case6
B1_case6 = 0.5
B2_case6 = -0.5
k2_case6 = 50
y_t6_d = A1 + (k1 - A1) / (1 + np.exp(B1_case6  * (t_d_case1 - x1_short)))
y_t6_r= A2 + (k2_case6 - A2) / (1 + np.exp(B2_case6 * (t_r_case1 - x2_short)))
y_t6 = np.append(y_t6_d,y_t6_r)


#############################
t_d_case2 = np.arange(0,100,0.1)
t_r_case2 = np.arange(100,200,0.1)
t_case2= np.append(t_d_case2,t_r_case2)
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

# case8
B1_case8 = 0.5
B2_case8 = -0.5
k2_case8 = 30
y_t8_d= A1 + (k1 - A1) / (1 + np.exp(B1_case8 * (t_d_case2 - x1_long)))
y_t8_r= A2 + (k2_case8  - A2) / (1 + np.exp(B2_case8  * (t_r_case2 - x2_long)))
y_t8 = np.append(y_t8_d,y_t8_r)


# case9
B1_case9 = 0.5
B2_case9 = -0.5
k2_case9 = 35
y_t9_d = A1 + (k1 - A1) / (1 + np.exp(B1_case9  * (t_d_case2 - x1_long)))
y_t9_r = A2 + (k2_case9 - A2) / (1 + np.exp(B2_case9 * (t_r_case2 - x2_long)))
y_t9 = np.append(y_t9_d,y_t9_r)

# case10
B1_case10 = 0.5
B2_case10 = -0.5
k2_case10 = 40
y_t10_d = A1 + (k1 - A1) / (1 + np.exp(B1_case10  * (t_d_case2 - x1_long)))
y_t10_r = A2 + (k2_case10 - A2) / (1 + np.exp(B2_case10 * (t_r_case2 - x2_long)))
y_t10 = np.append(y_t10_d,y_t10_r)

# case11
B1_case11 = 0.5
B2_case11 = -0.5
k2_case11 = 45
y_t11_d = A1 + (k1 - A1) / (1 + np.exp(B1_case11  * (t_d_case2 - x1_long)))
y_t11_r = A2 + (k2_case11 - A2) / (1 + np.exp(B2_case11 * (t_r_case2 - x2_long)))
y_t11 = np.append(y_t11_d,y_t11_r)

# case12
B1_case12 = 0.5
B2_case12 = -0.5
k2_case12 = 50
y_t12_d = A1 + (k1 - A1) / (1 + np.exp(B1_case12  * (t_d_case2 - x1_long)))
y_t12_r= A2 + (k2_case12 - A2) / (1 + np.exp(B2_case12 * (t_r_case2 - x2_long)))
y_t12 = np.append(y_t12_d,y_t12_r)


##############################################################################
#  韧性计算  #
########################### Tran方法 ##########################################

# 案例 1
from scipy import integrate
a1_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short))),0,50)[0]
a1_r = integrate.quad(lambda x:A2 + (k2_case1 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))),50,100)[0]
sigma1 = (a1_d + a1_r)/(integrate.quad(lambda x:50,0,100)[0])
rho1 = 25 / 50
delta1 = 20 / 50
zeta1 = 1
t_ss1,min_var1 = tool_methods.calculate(t_case1, y_t1)
tau1 = t_ss1/100
resilience1 = sigma1 * rho1 * (delta1 + zeta1 + 1 - pow(tau1,rho1 - delta1))

print("resilience1:",resilience1,"sigma1:",sigma1,"tau1:",tau1)

# 案例 7
a7_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))),0,100)[0]
a7_r = integrate.quad(lambda x:A2 + (k2_case7 - A2) / (1 + np.exp(B2_case1 * (x - x2_long))),100,200)[0]
sigma7 = (a7_d + a7_r)/(integrate.quad(lambda x:50,0,200)[0])
rho7 = 25 / 50
delta7 = 20 / 50
zeta7 = 1
t_ss7,min_var = tool_methods.calculate(t_case2, y_t7)
tau7 = t_ss7/200
resilience7 = sigma7 * rho7 * (delta7 + zeta7 + 1 - pow(tau7,rho7 - delta7))
print("resilience7:",resilience7,"sigma7:",sigma7,"tau7:",tau7)

print("###############################################################################################################")

# 案例2
a2_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case2 * (x - x1_short))),0,50)[0]
a2_r = integrate.quad(lambda x:A2 + (k2_case2 - A2) / (1 + np.exp(B2_case2 * (x - x2_short))),50,100)[0]
sigma2 = (a2_d + a2_r)/(integrate.quad(lambda x:50,0,100)[0])

rho2 = k2_case2 / 50
delta2 = 20 / 50
zeta2 = 1
t_ss2,min_var2 = tool_methods.calculate(t_case1, y_t2 )
tau2 = t_ss2/100
resilience2 = sigma2 * rho2 * (delta2 + zeta2 + 1 - pow(tau2,rho2 - delta2))
print("resilience2:",resilience2,"sigma2:",sigma2,"tau2:",tau2)

# 案例 8
a8_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))),0,100)[0]
a8_r = integrate.quad(lambda x:A2 + (k2_case8 - A2) / (1 + np.exp(B2_case1 * (x - x2_long))),100,200)[0]
sigma8 = (a8_d + a8_r)/(integrate.quad(lambda x:50,0,200)[0])
rho8 = k2_case8 / 50
delta8 = 20 / 50
zeta8 = 1
t_ss8,min_var8 = tool_methods.calculate(t_case2, y_t8)
tau8 = t_ss8/200
resilience8 = sigma8 * rho8 * (delta8 + zeta8 + 1 - pow(tau8,rho8 - delta8))
print("resilience8:",resilience8,"sigma8:",sigma8,"tau8:",tau8)

print("###############################################################################################################")

# 案例 3
a3_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short))),0,50)[0]
a3_r = integrate.quad(lambda x:A2 + (k2_case3 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))),50,100)[0]
sigma3 = (a3_d + a3_r)/(integrate.quad(lambda x:50,0,100)[0])
rho3 = k2_case3 / 50
delta3 = 20 / 50
zeta3 = 1
t_ss3,min_var3 = tool_methods.calculate(t_case1, y_t3)
tau3 = t_ss3/100
resilience3 = sigma3 * rho3 * (delta3 + zeta3 + 1 - pow(tau3,rho3 - delta3))
print("resilience3:",resilience3,"sigma3:",sigma3,"tau3:",tau3 )


# 案例 9
a9_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case9 * (x - x1_long))),0,100)[0]
a9_r = integrate.quad(lambda x:A2 + (k2_case9 - A2) / (1 + np.exp(B2_case9 * (x - x2_long))),100,200)[0]
sigma9 = (a9_d + a9_r)/(integrate.quad(lambda x:50,0,200)[0])
rho9 = k2_case9 / 50
delta9 = 20 / 50
zeta9 = 1
t_ss9,min_var9 = tool_methods.calculate(t_case2, y_t9)
tau9 = t_ss9/200
resilience9 = sigma9 * rho9 * (delta9 + zeta9 + 1 - pow(tau9,rho9 - delta9))
print("resilience9:",resilience9,"sigma9:",sigma9,"tau:",tau9)

print("###############################################################################################################")
# 案例 4
a4_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short))),0,50)[0]
a4_r = integrate.quad(lambda x:A2 + (k2_case4 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))),50,100)[0]
sigma4 = (a4_d + a4_r)/(integrate.quad(lambda x:50,0,100)[0])
rho4 = k2_case4 / 50
delta4 = 20 / 50
zeta4 = 1
t_ss4,min_var4 = tool_methods.calculate(t_case1, y_t4)
tau4 = t_ss4/100
resilience4 = sigma4 * rho4 * (delta4 + zeta4 + 1 - pow(tau4,rho4 - delta4))
print("resilience4:",resilience4,"sigma4:",sigma4,"tau4:",tau4)


# 案例 20
a10_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))),0,100)[0]
a10_r = integrate.quad(lambda x:A2 + (k2_case10 - A2) / (1 + np.exp(B2_case1 * (x - x2_long))),100,200)[0]
sigma10 = (a10_d + a10_r)/(integrate.quad(lambda x:50,0,200)[0])

rho10 = k2_case10 / 50
delta10 = 20 / 50
zeta10 = 1
t_ss10,min_var10 = tool_methods.calculate(t_case2, y_t10)
tau10 = t_ss10/200
resilience10 = sigma10 * rho10 * (delta10 + zeta10 + 1 - pow(tau10,rho10 - delta10))
print("resilience10:",resilience10,"sigma10:",sigma10,"tau10:",tau10)
print("###############################################################################################################")
# 案例 5
a5_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short))),0,50)[0]
a5_r = integrate.quad(lambda x:A2 + (k2_case5 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))),50,100)[0]
sigma5 = (a5_d + a5_r)/(integrate.quad(lambda x:50,0,100)[0])

rho5 = k2_case5 / 50
delta5 = 20 / 50
zeta5 = 1
t_ss5,min_var5 = tool_methods.calculate(t_case1, y_t5)
tau5 = t_ss5/100
resilience5 = sigma5 * rho5 * (delta5 + zeta5 + 1 - pow(tau5,rho5 - delta5))
print("resilience5:",resilience5,"sigma5:",sigma5,"tau5:",tau5)


# 案例 11
a11_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))),0,100)[0]
a11_r = integrate.quad(lambda x:A2 + (k2_case11 - A2) / (1 + np.exp(B2_case1 * (x - x2_long))),100,200)[0]
sigma11 = (a11_d + a11_r)/(integrate.quad(lambda x:50,0,200)[0])

rho11 = k2_case11/ 50
delta11 = 20 / 50
zeta11 = 1
t_ss11,min_var11 = tool_methods.calculate(t_case2, y_t11)
tau11 = t_ss11/200
resilience11 = sigma11 * rho11 * (delta11 + zeta11 + 1 - pow(tau11,rho11 - delta11))
print("resilience11:",resilience11,"sigma11:",sigma11,"tau11:",tau11)

print("###############################################################################################################")
# 案例 6
a6_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_short))),0,50)[0]
a6_r = integrate.quad(lambda x:A2 + (k2_case6 - A2) / (1 + np.exp(B2_case1 * (x - x2_short))),50,100)[0]
sigma6 = (a6_d + a6_r)/(integrate.quad(lambda x:50,0,100)[0])
rho6 = k2_case6 / 50
delta6 = 20 / 50
zeta6 = 1
t_ss6,min_var6 = tool_methods.calculate(t_case1, y_t6)
tau6 = t_ss6/100
resilience6 = sigma6 * rho6 * (delta6 + zeta6 + 1 - pow(tau6,rho6 - delta6))
print("resilience6:",resilience6,"sigma6:",sigma6,"tau6:",tau6)


# 案例 12
a12_d = integrate.quad(lambda x:A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (x - x1_long))),0,100)[0]
a12_r = integrate.quad(lambda x:A2 + (k2_case12 - A2) / (1 + np.exp(B2_case1 * (x - x2_long))),100,200)[0]
sigma12 = (a12_d + a12_r)/(integrate.quad(lambda x:50,0,200)[0])
rho12 = k2_case12/ 50
delta12 = 20 / 50
zeta12 = 1
t_ss12,min_var12 = tool_methods.calculate(t_case2, y_t12)
tau12 = t_ss12/200
resilience12 = sigma12 * rho12 * (delta12 + zeta12 + 1 - pow(tau12,rho12 - delta12))
print("resilience12:",resilience12,"sigma12:",sigma12,"tau12:",tau12)


plt.subplot2grid((2,2),(0,0),colspan=2)


plt.plot(t_case1,y_t1,marker="d",color="c",ls="-",lw=0.01,label="case1")
plt.plot(t_case1,y_t2,marker="d",color="g",ls="-",lw=0.01,label="case2")
plt.plot(t_case1,y_t3,marker="d",color="b",ls="-",lw=0.01,label="case3")
plt.plot(t_case1,y_t4,marker="d",color="m",ls="-",lw=0.01,label="case4")
plt.plot(t_case1,y_t5,marker="d",color="y",ls="-",lw=0.01,label="case5")
plt.plot(t_case1,y_t6,marker="d",color="k",ls="-",lw=0.01,label="case6")
# case 2
plt.plot(t_case2,y_t7,marker="d",color="r",ls="-",lw=0.01,label="case7")
plt.plot(t_case2,y_t8,marker="d",color="g",ls="-",lw=0.01,label="case8")
plt.plot(t_case2,y_t9,marker="d",color="b",ls="-",lw=0.01,label="case9")
plt.plot(t_case2,y_t10,marker="d",color="m",ls="-",lw=0.01,label="case10")
plt.plot(t_case2,y_t11,marker="d",color="y",ls="-",lw=0.01,label="case11")
plt.plot(t_case2,y_t12,marker="d",color="yellowgreen",ls="-",lw=0.01,label="case12")

plt.legend(fontsize=15)
plt.xticks(np.arange(0,210,10),fontsize=20)
plt.yticks(np.arange(0,80,10),fontsize=20)


plt.subplot2grid((2,2),(1,0),colspan=2)

case1_mark_num = [25,30,35,40,45,50]
cas1_resilience_cons =[resilience1,resilience2,resilience3,resilience4,resilience5,resilience6]
cas2_resilience_cons =[resilience7,resilience8,resilience9,resilience10,resilience11,resilience12]

# plt.plot(case1_mark_num,cas1_resilience_cons,marker="d",color="r",lw=0.01,label="resilience_case1")

plt.scatter(case1_mark_num,cas1_resilience_cons,c="r",s=20,label="resilience_case1")
plt.scatter(case1_mark_num,cas2_resilience_cons,c="b",s=20,label="resilience_case2")
plt.xticks(np.arange(20,55,5),fontsize=20)
plt.yticks(np.arange(0,1.5,0.2),fontsize=20)


plt.legend(fontsize=15)
plt.show()



