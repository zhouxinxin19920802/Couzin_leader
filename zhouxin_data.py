# cons_10 = [0.6438,0.4452,0.2622,0.1088]
# cons_20 = [0.4426,0.2697,0.14384,0.07798]
# cons_30 = [0.3208, 0.1772,0.09893,0.05773]
# cons_50 = [0.3208, 0.1772,0.09893,0.05773]
# cons_60 = [0.06705,0.02935,	0.02172, 0.01325]
# cons_70 = [0.02750,	0.01216, 0.010463, 0.006675]

import logging

# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FuncFormatter, MultipleLocator

logging.basicConfig(
    level=logging.DEBUG,  # 控制台打印的日志级别
    filename="backtrack_edge_method.py.txt",
    filemode="w",  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
    # a是追加模式，默认如果不写的话，就是追加模式
    format="%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s"
    # 日志格式
)

# 此图主要分析的是不同失效比例下无人集群韧性变化

# 横坐标是失效比例，纵坐标表示的韧性


x = [0.1, 0.2, 0.3, 0.5, 0.6, 0.7]
# cons_20 = [0.6438, 0.4426, 0.3208, 0.1116, 0.06705, 0.02750]
# cons_50 = [0.4452, 0.2697, 0.1772, 0.04477, 0.02935, 0.01216]
# cons_100 = [0.2622, 0.14384, 0.09893, 0.03833, 0.02172, 0.010463]
# cons_200 = [0.1088, 0.07798, 0.05773, 0.02516, 0.01325, 0.006675]
# cons_300 = [0.1088, 0.07798, 0.05773, 0.02516, 0.01325, 0.006675]

cons_20_random = [1.1182, 0.81686, 0.62139, 0.21369, 0.109849, 0.060304]
cons_50_random = [1.034706, 0.69067, 0.43947, 0.1309, 0.06853, 0.02562]
cons_100_random = [0.98646, 0.42424, 0.355504, 0.08347, 0.04566, 0.01974]
cons_200_random = [0.6729, 0.3433, 0.15637, 0.07168, 0.03652, 0.01758]


cons_20_degree = [1.10759, 0.84526, 0.59244, 0.21864, 0.12100, 0.041021]
cons_50_degree = [1.0727, 0.7886, 0.44411, 0.0966, 0.04978, 0.0224]
cons_100_degree = [0.84485, 0.11378, 0.04185, 0.04544, 0.058687, 0.037885]
cons_200_degree = [0.1056, 0.025495, 0.044730, 0.0694, 0.0809, 0.04996]

fig = plt.figure()
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_major_locator(MultipleLocator(0.1))


# 设置副刻度的个数
# ax.xaxis.set_minor_locator(AutoMinorLocator(4))


ax.plot(x, cons_20_random, color="blue", label="swarm_size=20", marker="o", lw=1, linestyle="-")
ax.plot(x, cons_50_random, color="black", label="swarm_size=50", marker="v", lw=1, linestyle="-")
ax.plot(x, cons_100_random, color="red", label="swarm_size=100", marker="p", lw=1, linestyle="-")
ax.plot(x, cons_200_random, color="gold", label="swarm_size=200", marker="D", lw=1, linestyle="-")
#
# ax.plot(x, cons_20_degree, color="blue", label="swarm_size=20", marker="o", lw=1, linestyle="--")
# ax.plot(x, cons_50_degree, color="black", label="swarm_size=50", marker="v", lw=1, linestyle="--")
# ax.plot(x, cons_100_degree, color="red", label="swarm_size=100", marker="p", lw=1, linestyle="--")
# ax.plot(x, cons_200_degree, color="gold", label="swarm_size=200", marker="D", lw=1, linestyle="--")


ax.set_xlabel("Failure proportion")
ax.set_ylabel("resilience")

ax.legend()


ax.set_xlim(0, 1)
# ax.set_ylim(0,2)


plt.show()
