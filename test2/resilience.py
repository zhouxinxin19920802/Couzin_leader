##-*- coding:utf-8 -*-
import logging
import math
import numpy as np
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='test.txt',
                    filemode='w',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
# K1:期望水平，A1:最小性能水平, B1:变形斜率，x1:变形位置参数
A1 = 20
K1 = 50
B1 = 0.5
x1 = 25
A2 = 20
K2 = 40
B2 = 0.5
x2 = 70
x = np.arange(0,70,2)
data = []
for item in x:
    y = A1 + (K1 - A1)/(1 + math.exp(B1 * (item - x1)))
    data.append(y)

x_a= np.arange(70,120,2)
data1 = []
for item1 in x_a:
    y1 = A2 + (K2 - A2)/(1 + math.exp(-B2 * (item1 - x2)))
    data1.append(y1)

x_t = np.append(x,x_a)
data_t = data + data1

print("data:%s",str(data))

plt.plot(x_t,data_t,marker="d",color="r")
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.legend()
plt.show()


