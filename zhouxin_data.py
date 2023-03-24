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


"""
#随机攻击
cons_20_random = [1.1182, 0.81686, 0.62139, 0.21369, 0.109849, 0.060304]
cons_50_random = [1.034706, 0.69067, 0.43947, 0.1309, 0.06853, 0.02562]
cons_100_random = [0.98646, 0.42424, 0.355504, 0.08347, 0.04566, 0.01974]
cons_200_random = [0.6729, 0.3433, 0.15637, 0.07168, 0.03652, 0.01758]

# 度攻击
cons_20_degree = [1.10759, 0.84526, 0.59244, 0.21864, 0.12100, 0.041021]
cons_50_degree = [1.0727, 0.7886, 0.44411, 0.0966, 0.04978, 0.0224]
cons_100_degree = [0.84485, 0.11378, 0.04185, 0.04544, 0.058687, 0.037885]
cons_200_degree = [0.1056, 0.025495, 0.044730, 0.0694, 0.0809, 0.04996]
"""

# 后方攻击
# cons_20_end = [1.14658, 1.067744, 1.04318, 0.834183, 0.779608, 0.64517]
# cons_50_end = [1.56183, 1.47867, 1.470069, 1.23687, 1.1134, 1.03347]
# cons_100_end = [1.75521, 1.61372, 1.52145, 1.306723, 0.86618, 0.619886]
# cons_200_end = [1.53135, 1.4484739, 1.3200320, 1.08039, 0.970549, 0.828908]

"""
# 左右方攻击
cons_20_right = [1.046836, 1.06226, 0.884405, 0.728042, 0.625974, 0.4980751]
cons_50_right = [1.6722, 1.26549, 0.94776, 0.726067, 0.5511449, 0.446050]
cons_100_right = [1.4431935, 1.1251742, 0.981699, 0.710858, 0.551819, 0.46580]
cons_200_right = [1.30130, 0.745027, 0.53126, 0.377420, 0.279011, 0.23425]

# 从中间攻击
cons_20_center = [1.048324, 0.97172, 0.764471, 0.487215, 0.18174, 0.07763]
cons_50_center = [1.2931, 0.967567, 0.49777, 0.088516, 0.018695, 0.027630]
cons_100_center = [0.27962, 0.103935, 0.0693996, 0.113851, 0.111426, 0.047221]
cons_200_center = [0.08871, 0.135957, 0.137689, 0.217273, 0.14293, 0.074806]


# 从前面攻击
cons_20_front = [1.13442, 0.532459, 0.451717, 0.171492, 0.143161, 0.11858]
cons_50_front = [0.26168, 0.064857, 0.0030927, 0.000086468, 0.0000724036, 0.000010676]
cons_100_front = [0.405097, 0.131065, 0.000920223, 0, 0, 0]
cons_200_front = [0.08871, 0.135957, 0.137689, 0.217273, 0.14293, 0.074806]


fig = plt.figure()
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_major_locator(MultipleLocator(0.1))


# 设置副刻度的个数
# ax.xaxis.set_minor_locator(AutoMinorLocator(4))


ax.plot(x, cons_20_front, color="blue", label="swarm_size=20", marker="o", lw=1, linestyle="-")
ax.plot(x, cons_50_front, color="black", label="swarm_size=50", marker="v", lw=1, linestyle="-")
ax.plot(x, cons_100_front, color="red", label="swarm_size=100", marker="p", lw=1, linestyle="-")
ax.plot(x, cons_200_front, color="gold", label="swarm_size=200", marker="D", lw=1, linestyle="-")
#
# ax.plot(x, cons_20_degree, color="blue", label="swarm_size=20", marker="o", lw=1, linestyle="--")
# ax.plot(x, cons_50_degree, color="black", label="swarm_size=50", marker="v", lw=1, linestyle="--")
# ax.plot(x, cons_100_degree, color="red", label="swarm_size=100", marker="p", lw=1, linestyle="--")
# ax.plot(x, cons_200_degree, color="gold", label="swarm_size=200", marker="D", lw=1, linestyle="--")
"""


fig = plt.figure()
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

###################################################################
# 随机运动攻击
"""
cons_random_movement = [0.765532,	0.40292,	0.186006,	0.044010,	0.0277273,	0.00630018]
ax.plot(x, cons_random_movement, color="blue", label="swarm_size=20", marker="o", lw=1, linestyle="-")
"""

""""

# 不同规模集群
cons_20_random_move = [1.1182, 0.81686, 0.62139, 0.21369, 0.109849, 0.060304]
cons_50_random_move = [1.034706, 0.69067, 0.43947, 0.1309, 0.06853, 0.02562]
cons_100_random_move = [0.98646, 0.42424, 0.355504, 0.08347, 0.04566, 0.01974]
cons_200_random_move = [0.6729, 0.3433, 0.15637, 0.07168, 0.03652, 0.01758]
"""
cons_20_random_move_degree = [0.760729, 0.38182, 0.18628, 0.04783, 0.024753, 0.0081522]
cons_50_random_move_degree = [0.901047, 0.27921, 0.1989878, 0.10842, 0.05712, 0.026358]
cons_100_random_move_degree = [0.143796, 0.10422, 0.098822, 0.075547, 0.050921, 0.0174766]
cons_200_random_move_degree = [0.041016, 0.061588, 0.0171035, 0.04459, 0.018804, 0.0114091]

ax.plot(x, cons_20_random_move_degree, color="blue", label="swarm_size=20", marker="o", lw=1, linestyle="-")
ax.plot(x, cons_50_random_move_degree, color="black", label="swarm_size=50", marker="v", lw=1, linestyle="-")
ax.plot(x, cons_100_random_move_degree, color="red", label="swarm_size=100", marker="p", lw=1, linestyle="-")
ax.plot(x, cons_200_random_move_degree, color="gold", label="swarm_size=200", marker="D", lw=1, linestyle="-")

ax.xaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_major_locator(MultipleLocator(0.1))

ax.set_xlabel("Failure proportion")
ax.set_ylabel("resilience")
ax.legend()


ax.set_xlim(0, 1)
# ax.set_ylim(0,2)


plt.show()
