#-*- coding:utf-8 -*-



# cons1 = 1 * (5 + 0.75 * 20)/20 * (1 + 1 - pow(20/20, 0.75)) *pow(0.8,5/5)
# print(cons1)
#
# cons2 = 1 * (5 + 1 * 7)/20 * (1+1 - 13/20) * pow(0.8,8/5)
# print(cons2)
#
# # print(pow(0.8,8/5))
#
#
# # print(0.75*(5+5*0.2+0.75*20)/20*(0.2+1+1-pow(20/20, 0.75)))
# # print(1*(5+7*0.2+0.7*20)/20*(0.2+1+1-(13/20)))
#
# print(30/50*0.71*(0.2+1+1-pow(0.8,0.1))*pow(0.8,50/40))
# print(160/(50*9)*0.71*(160/(50*9)+1+1-pow(0.8,0))*pow(0.8,50/40))

import numpy as np
import matplotlib.pyplot as plt
import math


# x = np.arange(0,20,0.5)
# y = np.exp(-x)
#
#
# # y1 = pow(0.8,x)
# plt.plot(x,y,label="r",color="red")
# # plt.plot(x,y1,label="y1",color="black")
# plt.legend()
# plt.show()

#
# print(30/50*0.71*(20/50+1+1-pow(0.8,20/50)*pow(0.5,50/60)))
# print(160/(9*50)*0.71*(160/(9*50)+1+1-pow(0.8,0)*pow(0.5,50/60)))

# print(1400/2500*30/50)
#
# print((160/9*50+30*(30-160/9)/2)/2500)
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import  AutoMinorLocator, MultipleLocator, FuncFormatter
# # Generate some data to plot
# x = [1, 2, 3]
# y = [4, 5, 6]
#
# # Create a Line2D object
# line = Line2D(x, y,color="r")
#
# # Set the line width
# line.set_linewidth(2.5)
#
# # Add the line to the plot
# plt.gca().add_line(line)
#
#
#
# # Show the plot
# plt.show()


#
# x = range(0,5)
# y1 = [2,5,7,8,20]
#
# fig = plt.figure()
#
# ax = fig.gca()
#
# ax.add_line(Line2D(x, y1)) # 使用add_line方法将创建的Line2D添加到子图中(添加到ax坐标系中)
# #设置x,y的区间
# ax.set_xlim(0,4)
# ax.set_ylim(2, 11)
#
# ax.xaxis.set_major_locator(MultipleLocator(2.0))
# ax.yaxis.set_major_locator(MultipleLocator(2.0))
#
# ax.xaxis.set_minor_locator(AutoMinorLocator(4))
# ax.yaxis.set_minor_locator(AutoMinorLocator(4))
#
# ax.tick_params("y",which='major',length=15,width=2.0,colors="r")
# ax.tick_params("x",which='major',length=15,width=2.0,colors="r")





# plt.show()


import numpy as np
import matplotlib.pyplot as plt
#新建figure
# fig = plt.figure()
# #定义数据
# x = [1, 2, 3, 4, 5, 6, 7]
# y = [1, 7, 15, 24, 30, 50, 55]
#
# #新建区域ax1
# #figure的百分比,从figure 20%的位置开始绘制, 宽高是figure的80%
# left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# #获得绘制的句柄
# ax1 = fig.add_axes([left, bottom, width, height])
# ax1.plot(x, y, 'r')
# ax1.set_title('area1')
# #新增区域ax2,嵌套在ax1内，看一看图中图是什么样，这就是与subplot的区别
# left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
# #获得绘制的句柄
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(x,y, 'b')
# ax2.set_title('area2')
# plt.show()



# 导入matplotlib库
import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_node("jun")
G.add_node("zhan")
G.add_node("lv")
G.add_node("ying")
G.add_node("jia")
G.add_node("chang")
G.add_node("wangluo")
G.add_node("haishang")
G.add_node("kongzhong")
G.add_node("hangtian")
G.add_node("wurenjituan")
G.add_node("wurenjibudui")
G.add_node("xinxichi")


G.add_edge("jun","zhan")
G.add_edge("zhan","jun")

G.add_edge("zhan","chang")
G.add_edge("chang","zhan")

G.add_edge("zhan","lv")
G.add_edge("lv","zhan")

G.add_edge("chang","lv")
G.add_edge("lv","chang")

G.add_edge("chang","ying")
G.add_edge("ying","chang")

G.add_edge("chang","jia")
G.add_edge("jia","chang")

G.add_edge("lv","ying")
G.add_edge("ying","lv")

G.add_edge("ying","jia")
G.add_edge("jia","ying")


G.add_edge("xinxichi","jun")

G.add_edge("xinxichi","haishang")
G.add_edge("xinxichi","kongzhong")
G.add_edge("xinxichi","wangluo")
G.add_edge("xinxichi","hangtian")
G.add_edge("xinxichi","chang")
G.add_edge("xinxichi","zhan")

G.add_edge("kongzhong","wurenjituan")
G.add_edge("wurenjituan","wurenjibudui")

print(nx.average_shortest_path_length (G))
nx.draw(G)
plt.show()