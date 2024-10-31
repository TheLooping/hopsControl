import numpy as np
    # 定义 cos_1 函数
def cos_1(x):
    if x == 0:
        return 0
    else:
        return np.cos(1/x)

    # 定义 f_converge 函数
def f_converge(x, a):
    return cos_1(x) * a * x

def converge_times(a, epsilon, alpha=1):

    # 设置初始点
    initial_point = 0.7
    xi = initial_point
    times = 0
    xi_values = []  # 用于存储每次迭代的 xi 值

    while abs(xi) > epsilon:
        times += 1        
        yi = f_converge(xi, a)
        r = np.random.rand()
        xi = abs(yi + xi * alpha * r)  # 下一次迭代
        xi_values.append(xi)


    return times, xi_values

# 示例调用
# result, xi_values = converge_times(a=0.1, epsilon=0.001, alpha=0.5)
# print(result)
# print(xi_values)
