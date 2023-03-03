
# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator,MultipleLocator,FuncFormatter

import logging
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='backtrack_edge_method.py.txt',
                    filemode='w',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )

# 此图主要分析的是不同失效比例下无人集群韧性变化
# 横坐标是失效比例，纵坐标表示的韧性


x = [0.1,0.2,0.3,0.5,0.6,0.7]
data = [0.6438, 0.4426, 0.3208,0.1116, 0.06705,0.0275]

fig = plt.figure()
ax = fig.add_axes([0.2,0.2,0.7,0.7])

ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_major_locator(MultipleLocator(0.1))



# 设置副刻度的个数
# ax.xaxis.set_minor_locator(AutoMinorLocator(4))


ax.plot(x, data, color="blue",label="resilience",marker="o")
ax.set_xlabel("failure rate")
ax.set_ylabel("resilience")

ax.legend()


ax.set_xlim(0,1)
# ax.set_ylim(0,2)


plt.show()
