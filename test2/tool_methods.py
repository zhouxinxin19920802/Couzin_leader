# -*- coding:utf-8 -*-
import logging
import math
import matplotlib.pyplot as plt

logging.basicConfig(
    level=logging.INFO,  # 控制台打印的日志级别
    filename="test.txt",
    # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
    filemode="w",
    # a是追加模式，默认如果不写的话，就是追加模式
    format="%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s"
    # 日志格式
)

a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = [2, -3, 2.5, -4, 3, 3.2, 3.1, 3.15, 3.11, 3.12]


def calculate(a1, a2):
    """
    Parameters
    ----------
    a1 : list
        横坐标，因为时间轴不一定是像0,1,2,3,4,5
    a2 : list
        纵坐标，y值

    Returns
    -------
    a1[min_id] : list
        min_id对应的index值, a1[min_id]对应稳态时间值
    min_var : float
        对应的方差
    """
    min_id = 0
    min_var = float("Inf")

    for i in range(0, len(a2) - 1):
        # logging.info("i:%s", str(i))
        var = 0
        total_sum = 0
        for j in range(i, len(a2)):
            total_sum = total_sum + a2[j]
        mean = total_sum / (len(a2) - i)
        for j in range(i, len(a2)):
            var = var + pow((a2[j] - mean), 2)
        logging.info(
            "i:%s,var:%s,num:%s,value:%s", str(i), str(var), str(pow(len(a2) - i, 2)), str(var / pow(len(a2) - i, 2))
        )
        var = var / pow(len(a2) - i, 2)

        if var < min_var:
            min_var = var
            min_id = i
        if min_var < 0.0001:
            return a1[min_id], min_var
    return a1[min_id], min_var


def time_amend(real_time, absolute_time):
    omega = 0.6
    time_factor = math.pow(omega, real_time / absolute_time)
    return time_factor


# id, min_var = calculate(a1, a2)
# print("id:", id, "value", a1[id], "min_var:", min_var)
# plt.plot(a1, a2)
# plt.show()
