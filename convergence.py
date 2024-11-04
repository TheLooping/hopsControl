'''
Author: TheLooping 100526118+TheLooping@users.noreply.github.com
Date: 2024-11-01 00:56:32
LastEditors: TheLooping 100526118+TheLooping@users.noreply.github.com
LastEditTime: 2024-11-04 17:44:21
FilePath: \hopsControl\convergence.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import matplotlib.pyplot as plt
from g_x import g  # 从模块中导入函数

    # 定义 cos_1 函数
def cos_1(x):
    if x == 0:
        return 0
    else:
        return np.cos(1/x)


    # 定义 f_converge 函数
def f_converge(x, a):
    if x < 0.02:
        return cos_1(x) * a * x * 0.1
    return cos_1(x) * a * x

def converge_times(a, epsilon, alpha=1):
    # 设置初始点
    initial_point = 0.09
    xi = initial_point
    times = 0
    xi_values = []  # 用于存储每次迭代的 xi 值

    while abs(xi) > epsilon:
        r = 2 * np.random.rand() - 1
        xi = abs(xi + xi * alpha * r)  # 下一次迭代
        yi = abs(f_converge(xi, a))
        # if xi > 0.015:
        #     continue
        xi = yi
        xi_values.append(yi)
        times += 1  
        if abs(r) > g(xi, epsilon):
            break  

    return times, xi_values

# 绘制图像
def plot_convergence(a):
    plt.close('all')  # 关闭所有图形
    # 生成 x 值
    x_values = np.linspace(-0.7, 0.7, 14001)  # 在 -1 到 1 之间生成 1000 个点
    y_values = np.array([f_converge(x, a) for x in x_values])  # 计算对应的 y 值

    # 绘制图像
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label=f'f_converge(x, {a})', color='blue')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.title('Graph of f_converge')
    plt.xlabel('x')
    plt.ylabel('f_converge(x, a)')
    plt.ylim(-1.5, 1.5)  # 根据需要调整 y 轴范围
    plt.legend()
    plt.grid()
    plt.savefig('f_converge.png')

