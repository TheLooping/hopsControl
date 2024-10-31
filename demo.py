import numpy as np
import matplotlib.pyplot as plt

# 示例数据
x = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 3, 5, 7, 11])  # 左侧 y 轴的数据
y2 = np.array([10, 20, 30, 40, 50])  # 右侧 y 轴的数据

# 创建图形
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制左侧散点图
ax1.scatter(x, y1, color='red', marker='o', alpha=0.5, label='数据集1')
ax1.set_xlabel('X 轴')
ax1.set_ylabel('左侧 Y 轴', color='red')
ax1.tick_params(axis='y', labelcolor='red')

# 在左侧 y 轴上添加文本标签
for i in range(len(x)):
    ax1.text(x[i], y1[i], f'{y1[i]}', fontsize=8, ha='center', va='bottom')

# 创建右侧 y 轴
ax2 = ax1.twinx()
ax2.scatter(x, y2, color='blue', marker='x', alpha=0.5, label='数据集2')
ax2.set_ylabel('右侧 Y 轴', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# 在右侧 y 轴上添加文本标签
for i in range(len(x)):
    ax2.text(x[i], y2[i], f'{y2[i]}', fontsize=8, ha='center', va='bottom')

# 设置标题
plt.title('左右两个坐标轴的散点图')

# 显示图形
plt.savefig('dual_axis_scatter_plot.png')  # 保存图像
