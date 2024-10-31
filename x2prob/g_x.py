import numpy as np
import matplotlib.pyplot as plt

# 定义sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 定义g(x)函数
def g(x, epsilon):
    return np.where(np.abs(x) <= epsilon, 
                    0, 
                    2 * sigmoid(x*10) - 1)

# 设置x的范围
x = np.linspace(-1, 1, 100)

# 设置epsilon的值
epsilon = 0.05  # 你可以根据需要调整

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