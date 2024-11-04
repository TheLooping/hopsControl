'''
Author: TheLooping 100526118+TheLooping@users.noreply.github.com
Date: 2024-11-01 10:06:09
LastEditors: TheLooping 100526118+TheLooping@users.noreply.github.com
LastEditTime: 2024-11-04 17:21:50
FilePath: \hopsControl\g_x.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import matplotlib.pyplot as plt

# 定义sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 定义g(x)函数
def g(x, epsilon):
    return np.where(np.abs(x) <= epsilon, 
                    0, 
                    (2 * sigmoid(x*100) - 1))

# 设置x的范围
x = np.linspace(-0.1, 0.1, 101)

# 设置epsilon的值
epsilon = 0.01  # 可以根据需要调整

# 计算g(x)的值
y = g(x, epsilon)

# 绘制图像
plt.plot(x, y, label=f'g(x) with epsilon={epsilon}')
plt.title(f'Graph of g(x) with epsilon={epsilon}')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.axhline(0, color='black',linewidth=0.5)  # x轴
plt.axvline(0, color='black',linewidth=0.5)  # y轴
plt.grid(True)
plt.legend()
plt.savefig('g_x.png')