import numpy as np
import matplotlib.pyplot as plt

# 模拟参数
num_trials = 10000  # 总试验次数
Pf = 0.7  # 固定的Pf值
max_hops_list = [4, 6, 8, 10]  # 不同的最大跳数
frequencies = {max_hops: [] for max_hops in max_hops_list}

# 进行模拟
for max_hops in max_hops_list:
    for _ in range(num_trials):
        rounds_count = 0
        while np.random.rand() < Pf:  # 事件A发生
            rounds_count += 1
            if rounds_count >= max_hops:  # 达到最大跳数
                rounds_count = max_hops  # 将跳数设置为最大值
                break
        frequencies[max_hops].append(rounds_count)

# 绘制图形
plt.figure(figsize=(10, 6))
for max_hops, counts in frequencies.items():
    # 计算每轮的频次分布
    actual_max_rounds = max_hops  # 这里最大值为当前的max_hops
    freq_distribution = np.bincount(counts, minlength=actual_max_rounds + 1)[0:]  # 从0开始
    plt.plot(range(0, actual_max_rounds + 1), freq_distribution / num_trials, marker='o', label=f'TTL={max_hops}')

plt.title('Frequency Distribution of Hops (Pf=0.7 with Max Hops Constraints)')
plt.xlabel('Hops')
plt.ylabel('Frequency (Normalized)')
xticks = range(0, max(max_hops_list) + 1, 1)
plt.xticks(xticks)

plt.legend()
plt.savefig('event_a_frequency_distribution_fixed_pf.png')  # 保存图像
