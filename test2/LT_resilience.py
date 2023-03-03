#-*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import math
import matplotlib.ticker as ticker
from calendar import month_name, day_name
from matplotlib.ticker import FormatStrFormatter
# fontstyle = dict(fontsize=18,weight ="black")
# fig1,ax1 = plt.subplots()
# t = np.arange(0.05,20,0.01)
# s1 = np.exp(t)
# ax1.plot(t,s1,c="b",ls="-")
# ax1.set_xlabel("x",fontsize = 30)
# ax1.set_ylabel("y",fontsize = 30)
# ax1.set_xticks(np.arange(0,11,1))
# ax1.set_xticklabels(np.arange(0,11,1),fontsize =30)
# ax2 = ax1.twinx()
# s2 = np.cos(t**2)
# ax2.plot(t,s2,c="r",ls=":")
# ax2.set_ylabel("cosn",color="r",fontsize = 30)
# plt.show()

from matplotlib.ticker import AutoMinorLocator,MultipleLocator,FuncFormatter

# x = np.linspace(0.5,3.5,100)
# y = np.sin(x)
#
# fig = plt.figure(figsize=(8,8))
# ax = fig.add_subplot(111)
#
# ax.xaxis.set_major_locator(MultipleLocator(1.0))
# ax.yaxis.set_major_locator(MultipleLocator(1.0))
#
#
# ax.xaxis.set_minor_locator(AutoMinorLocator(4.0))
# ax.yaxis.set_minor_locator(AutoMinorLocator(4.0))
#
#
#
# def minor_tick(x,pos):
#     if not x%1.0:
#         return ""
#     return "%.2f" % x
#
# ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))
#
#
# ax.tick_params("y",which  = 'major', length=30, width = 2.0,labelsize  =30 ,color = 'r')
# ax.tick_params("x",which  = 'major', length=30, width = 2.0,labelsize  =30 ,color = 'r')
# ax.tick_params("x",which  = 'minor', length=50, width =1.0, labelsize  =30 ,labelcolor='0.25')
# ax.tick_params("y",which  = 'minor', length=50, width =1.0, labelsize  =30 ,labelcolor='0.25')
#
#
#
# ax.set_xlim(0,4)
# ax.set_ylim(0,2)
#
# ax.plot(x,y,c=(0.25,0.25,1.00), lw =2, zorder=20)
# ax.grid(linestyle="-",linewidth = 0.5,color="r",zorder=0)
#
# plt.show()


# fig = plt.figure(facecolor=(1.0,1.0,0.9412))
#
# ax = fig.add_axes([0.1,0.1,1,1])
#
# for ticklabel in ax.xaxis.get_ticklabels():
#     ticklabel.set_color('slateblue')
#     ticklabel.set_fontsize(30)
#     ticklabel.set_rotation(30)
#
#
# for tickline in ax.xaxis.get_ticklines():
#     tickline.set_color('slateblue')
#     tickline.set_markersize(30)
#     tickline.set_markeredgewidth(2)
#
# plt.show()
#
# fig = plt.figure()
# ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
# x = np.arange(1, 8, 1)
# y = 2 * x
#
# ax.plot(x, y, ls="-", lw=2, color="orange", marker="o", ms=20, mfc="c", mec='c')
# ax.yaxis.set_major_formatter(FormatStrFormatter(r"$\yen%1.1f$"))
#
# ax.tick_params("y", length=50, width=1.0, labelsize=30, labelcolor='0.25')
#
# ax.tick_params("x", length=50, width=1.0, labelsize=30, labelcolor='0.25')
#
#
# plt.xticks(x, day_name[0:7], rotation=20, fontsize=30)
#
# ax.set_xlim(0, 8)
# ax.set_ylim(0, 18)
# plt.show()

# plt.axis([3, 7, -0.5, 3])
# plt.plot(4+np.arange(3), [0, 1, 0], color='blue', linewidth=4, linestyle="-")
# plt.tick_params(length=20, width=1.0, labelsize=30, labelcolor='0.25')
# plt.show()

# from calendar import day_name
# from matplotlib.ticker import FormatStrFormatter
#
# fig = plt.figure()
#
# ax = fig.add_axes([0.2,0.2,0.7,0.7])
#
# ax.spines['bottom'].set_position(("outward",20))
#

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from matplotlib.spines import Spine

import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)
# 设置有边框和头部边框颜色为空right、top、bottom、left
ax.spines['right'].set_color('r')
ax.spines['top'].set_color('r')

plt.show()