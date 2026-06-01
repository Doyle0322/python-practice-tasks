import random

def verify_law_of_large_numbers(num_trials):
    """
    输入参数：
    num_trials: 掷骰子的总次数 (模拟的平行宇宙数量)

    期望返回：
    掷出数字 '6' 的最终频率 (float类型)
    """
    # 计数器：记录掷出 6 的次数
    count_six = 0

    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 开启一个循环，执行 num_trials 次
    # 步骤 2: 在每次循环中，用 random.randint(1, 6) 掷一次骰子
    # 步骤 3: 检查如果掷出的结果是 6，就把 count_six 加 1
    # 步骤 4: 循环彻底结束后，计算最终的频率 (count_six / num_trials)
    # 步骤 5: 将计算出的频率 return 出去
    # ==========================================
    for _ in range(num_trials):
        toll = random.randint(1,6)
        if toll == 6:
            count_six += 1
    result = count_six / num_trials
    return result
    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（感受算力的降维打击）
# ------------------------------------------
# 我们分别测试 10次、1000次、和 100万次
trials_list = [10, 1000, 1000000]

for trials in trials_list:
    result_freq = verify_law_of_large_numbers(trials)
    print(f"🎲 掷骰子 {trials} 次，出现 6 的频率是: {result_freq:.4f}")

print(f"🎯 考研理论概率期望值: 0.1667")