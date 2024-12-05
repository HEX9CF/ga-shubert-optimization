import numpy as np

# 目标函数
# ( Michaelwicz Z. 1996): Shubert 函数
def objective_function(x):
    r = 1

    for i in range(len(x)):
        sum = 0
        for j in range(5):
            sum += j * np.cos((j + 1) * x[i] + j)
        r *= sum

    return r