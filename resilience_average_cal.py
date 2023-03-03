# coding: utf-8
import os


data = []
# 打开
for line in open("resilence.txt", "r", encoding="utf-8"):
    line = line.strip("\n")
    data.append(float(line))


resilience_aveage = sum(data) / len(data)

f = open("resilence_average.txt", "w")
f.write(str(resilience_aveage))
f.close()

print(resilience_aveage)
