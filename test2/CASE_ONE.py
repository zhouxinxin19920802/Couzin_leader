#-*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import math


A1 = 20
k1 = 50
x1 = 25

A2 = 20
k2 = 40
x2 = 70

t_d = np.arange(0,50,0.1)
t_r = np.arange(50,100,0.1)
t = np.append(t_d,t_r)

# case1
B1_case1 = 0.5
B2_case1= -0.5
y_t1_d= A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (t_d - x1))) + np.random.normal(0,2,len(t_d));
y_t1_r= A2 + (k2 - A2) / (1 + np.exp(B2_case1 * (t_r - x2))) + np.random.normal(0,2,len(t_r));
y_t1 = np.append(y_t1_d,y_t1_r)

y_t4_d= A1 + (k1 - A1) / (1 + np.exp(B1_case1 * (t_d - x1)))
y_t4_r= A2 + (k2 - A2) / (1 + np.exp(B2_case1 * (t_r - x2)))
y_t4 = np.append(y_t4_d,y_t4_r)
print(len(t_d))
print(len(y_t1_d))


# case2
B1_case2 = 0.5
B2_case2 = -0.7
y_t2_d= A1 + (k1 - A1) / (1 + np.exp(B1_case2 * (t_d - x1)))
y_t2_r= A2 + (k2 - A2) / (1 + np.exp(B2_case2  * (t_r - x2)))
y_t2 = np.append(y_t2_d,y_t2_r)



# case3
B1_case3 = 0.5
B2_case3 = -0.3
y_t3_d = A1 + (k1 - A1) / (1 + np.exp(B1_case3  * (t_d - x1)))
y_t3_r= A2 + (k2 - A2) / (1 + np.exp(B2_case3 * (t_r - x2)))
y_t3 = np.append(y_t3_d,y_t3_r)







plt.plot(t,y_t1,lw = '2.5',color="r",label="case1")
plt.plot(t,y_t4,marker="d",color="r",lw=0.01,ls="-",label="case1_smooth")
# plt.plot(t,y_t1,marker="d",color="g",ls="-",lw=0.01,label="case1")
plt.plot(t,y_t2,marker="d",color="g",ls="-",lw=0.01,label="case2")
plt.plot(t,y_t3,marker="d",color="b",ls="-",lw=0.01,label="case3")

plt.xticks(np.arange(0,100,10),fontsize=25)
plt.yticks(np.arange(0,80,10),fontsize=25)
# plt.xlim(0,4)
# plt.ylim(0,3)
plt.legend(fontsize=25)
plt.show()
