import math


def find_mle_parameter(data):
    """
    最大似然估计引擎 (暴力搜索版)

    输入参数：
    data: 真实发生的物理数据列表
    """
    best_p = 0.0
    max_log_likelihood = -float('inf')  # 初始化为一个极小的负无穷大

    # 统计数据特征
    num_heads = sum(data)
    num_tails = len(data) - num_heads

    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 开启 for 循环，变量为 i，从 1 跑到 99
    # 步骤 2: 在循环内，算出当前的试探概率 p_guess = i / 100.0 (模拟 0.01 到 0.99)
    # 步骤 3: 计算当前 p_guess 下的对数似然度 (Log-Likelihood)
    #         提示: current_ll = num_heads * math.log(p_guess) + num_tails * math.log(1 - p_guess)
    # 步骤 4: 判断：如果 current_ll 严格大于 max_log_likelihood
    # 步骤 5: 如果大于，立刻更新 max_log_likelihood = current_ll
    # 步骤 6: 同时更新 best_p = p_guess (这就是目前最有可能的概率！)
    # 步骤 7: 彻底退出循环后，return best_p
    # ==========================================
    for i in range(1,100):
        p_guess = i / 100.0
        current_ll = num_heads * math.log(p_guess) + num_tails * math.log(1-p_guess)
        if current_ll > max_log_likelihood:
            max_log_likelihood = current_ll
            best_p = p_guess
    return  best_p
    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（算力全开）
# ------------------------------------------
# 现实中发生的观测数据：抛 100 次硬币，极其诡异地出现了 72次正面，28次反面
observed_data = [1] * 72 + [0] * 28

estimated_p = find_mle_parameter(observed_data)

print("🎯 最大似然估计 (MLE) 推断结果:")
print(f"既然 72正28反 这种极端情况发生了...")
print(f"那最合理的硬币偏心概率，被暴力锁定为: {estimated_p}")