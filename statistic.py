import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from convergence import converge_times  # 从模块中导入函数

class DynamicArray:
    def __init__(self):
        self.array = []

    def set_value(self, index, value):
        if index >= len(self.array):
            self.array.extend([0] * (index + 1 - len(self.array)))
        self.array[index] = value

    def get_value(self, index):
        if index < len(self.array):
            return self.array[index]
        else:
            return 0

    def increment_value(self, index):
        if index >= len(self.array):
            self.array.extend([0] * (index + 1 - len(self.array)))
        self.array[index] += 1
    
    def __repr__(self):
        return str(self.array)
    
    def multiply_all(self, factor):
        self.array = [x * factor for x in self.array]

def run_convergence_trials(N, a, epsilon, alpha=1):
    times_list = []
    xi_data = []
    hops_data = []

    plt.title('xi - hops distribution')
    plt.grid(True)    

    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.set_xlabel('hops')
    ax1.set_ylabel('Forwarding parameter xi')

    max_hops = 1
    total_hops = DynamicArray()

    for _ in range(N):
        times, xi_values = converge_times(a, epsilon, alpha)
        max_hops = max(max_hops, times)

        for index, xi in enumerate(xi_values):
            xi_data.append(xi)
            hops_data.append(index + 1)  # hops 为索引 + 1

        times_list.append(times)
        total_hops.increment_value(times - 1)

    # 将 xi 和 hops 数据转换为 DataFrame
    df = pd.DataFrame({'xi': xi_data, 'hops': hops_data})
    ax1.scatter(df['hops'], df['xi'], color='red', marker='+', alpha=0.1)

    ax2 = ax1.twinx()
    ax2.set_ylabel('Path Length CDF')
    total_hops.multiply_all(1/N)

    # cdf = np.cumsum(total_hops.array)
    cdf = total_hops.array

    ax2.plot(range(1, max_hops + 1), cdf, color='black', marker='x', alpha=0.5)
    for i, value in enumerate(cdf):
        ax2.text(i + 1, cdf[i], f'{value * 100:.2f}%', fontsize=8, ha='center', va='bottom')

    mean_times = np.mean(times_list)
    variance_times = np.var(times_list)

    plt.savefig('xi_hops_distribution.png')  # 保存图像


    # 计算 -log(xi)
    # df['log_xi'] = -np.log(df['xi'])
    # 定义组间隔 d
    d = 0.01

    # 分组
    df['group'] = (df['xi'] // d).astype(int)

    # 统计每组内各 hop 的频次
    freq_table = df.groupby(['group', 'hops']).size().unstack(fill_value=0)

    # 计算每组的总频次
    total_counts = freq_table.sum(axis=1)

    # 计算占比
    proportion_table = freq_table.div(total_counts, axis=0)



    # 打印频次和占比表
    # print("频次表:")
    # new_column = [
    #     f"({np.exp(-(i + 1)):.2e}, {np.exp(-i):.2e})" if freq_table.loc[i].sum() > 0 else ""
    #     for i in freq_table.index
    # ]
    # freq_table.insert(0, 'Range', new_column)
    # freq_table.index.name = None
    # freq_table.columns.name = None
    # freq_table.columns.values[0] = ""

    # print(freq_table)

    # print("\n占比表:")
    # freq_table.index.name = None
    # freq_table.columns.name = None
    # print(proportion_table)

    # 绘制第二张堆积柱形图
    plt.figure(figsize=(10, 6))

    # 绘制比例图/频次图
    # plot_freq = False
    plot_freq = True
    

    if plot_freq:
        # 确保 bottom_values 是 numpy 数组
        bottom_values = np.zeros(len(freq_table.index))

        # 循环绘制每一列
        for column in freq_table.columns:
            plt.bar(freq_table.index, freq_table[column].values, bottom=bottom_values, label=str(column))
            bottom_values += freq_table[column].values  # 更新底部位置
    else:
        # 确保 bottom_values 是 numpy 数组
        bottom_values = np.zeros(len(proportion_table.index))

        # 循环绘制每一列
        for column in proportion_table.columns:
            plt.bar(proportion_table.index, proportion_table[column].values, bottom=bottom_values, label=str(column))
            bottom_values += proportion_table[column].values  # 更新底部位置

    # 添加标签和标题
    plt.xlabel(r'$x\_range\ (e^{-(x+1)},\ e^{-x})$')
    plt.ylabel('Proportion')
    plt.title('Stacked Bar Chart of Proportions')
    # plt.xticks(rotation=45)  # 旋转 x 轴标签以提高可读性
    plt.legend(title='Hop', loc='upper left', bbox_to_anchor=(1, 1))


    # 保存第二张图
    plt.savefig('stacked_bar_chart.png', bbox_inches='tight')
    plt.close()  # 关闭图像以释放内存

    return mean_times, variance_times

# 示例调用
N = 10000  # 运行次数
a = 0.8
epsilon = 0.01
alpha = 0.22

mean_result, variance_result = run_convergence_trials(N, a, epsilon, alpha)
print(f'均值: {mean_result}, 方差: {variance_result}')
