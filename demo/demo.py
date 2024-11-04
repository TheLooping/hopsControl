import numpy as np
import matplotlib.pyplot as plt

# 设置 x 的范围
x = np.linspace(0.4, 0.9, 101)  # 从一个小正数到 0.9 的范围

# 计算 y
y = np.log(0.0001) / np.log(x)  # 使用换底公式

# 绘制图像
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = log(0.0001) / log(x)', color='blue')
plt.title('Graph of y = log(0.0001) / log(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

# 保存图像
plt.savefig('log_graph.png', dpi=300)  # 保存为 300 dpi 的 PNG 文件
