import random
from threading import current_thread


def simulate_clt(sample_size, num_trials=10000):
    """
    中心极限定理模拟引擎

    输入参数：
    sample_size: 每次抽样的样本量 (比如每次掷 50 个骰子)
    num_trials: 模拟的总次数 (即平行宇宙的数量，默认 1万次)

    期望返回：
    包含 1万个“样本均值”的列表 (List)
    """
    # 准备一个空列表，用来装每个平行宇宙最后算出的平均值
    sample_means = []

    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 开启外层循环，执行 num_trials 次 (提示: for _ in range(...))
    # 步骤 2: 在外层循环里，初始化 current_sum = 0，用来累加当前宇宙里所有骰子的总点数
    # 步骤 3: 开启内层循环，执行 sample_size 次
    # 步骤 4: 在内层循环里，掷一次骰子 (1到6)，并把结果累加到 current_sum 里
    # 步骤 5: 内层循环彻底结束后 (注意缩进层级！)，算出这批骰子的均值: mean = current_sum / sample_size
    # 步骤 6: 把这个均值装进 sample_means 列表里 (提示: sample_means.append(mean))
    # 步骤 7: 外层循环也彻底结束后，return sample_means
    # ==========================================
    for i in range(num_trials):
        current_sum = 0
        for j in range(sample_size):
            current_sum += random.randint(1, 6)
        mean = current_sum / sample_size
        sample_means.append(mean)
    return sample_means
    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（验证极其微小的误差）
# ------------------------------------------
# 我们每次掷 50 个骰子，重复 1 万次
results = simulate_clt(sample_size=50, num_trials=10000)

# 计算这 1 万个平均值的“总平均值”
grand_mean = sum(results) / len(results)

print("🎯 考研数学真题代码验证结果:")
print(f"理论上 1 个骰子的数学期望应该是: 3.5")
print(f"中心极限定理 1 万次模拟算出的均值为: {grand_mean:.4f}")
# 如果代码写对，这个输出应该极其极其逼近 3.5000！