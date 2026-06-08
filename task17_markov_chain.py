import random

# 芯片状态转移矩阵 (马尔可夫链的灵魂)
transition_matrix = {
    "正常": {"正常": 0.8, "退化": 0.2, "故障": 0.0},
    "退化": {"正常": 0.1, "退化": 0.6, "故障": 0.3},
    "故障": {"正常": 0.0, "退化": 0.0, "故障": 1.0}
}


def get_next_state(current_state, matrix):
    """
    输入参数：
    current_state: 当前状态 (字符串)
    matrix: 状态转移矩阵 (嵌套字典)

    期望返回：
    下一个状态 (字符串)
    """
    # 拿到当前状态下，所有可能的去向和对应概率
    # 比如当前是"正常"，这里拿到的就是 {"正常": 0.8, "退化": 0.2, "故障": 0.0}
    possible_transitions = matrix[current_state]

    # 摇骰子：生成一个 0.0 到 1.0 之间的随机浮点数
    rand_val = random.random()

    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 初始化一个累加概率变量 cumulative_prob = 0.0
    # 步骤 2: 遍历 possible_transitions 字典的 key(下一个状态) 和 value(概率)
    # 步骤 3: 在循环里，把当前的概率(value)累加到 cumulative_prob 上
    # 步骤 4: 如果生成的 rand_val 严格小于 cumulative_prob，说明随机数落在了这个区间！
    # 步骤 5: 立刻 return 当前的 key
    # ==========================================
    cumulative_prob = 0.0
    for key, value in possible_transitions.items():
        cumulative_prob += value
        if rand_val < cumulative_prob:
            return key
    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（模拟 10 天的系统老化过程）
# ------------------------------------------
current = "正常"
print(f"第 0 天系统状态: {current}")

for day in range(1, 11):
    current = get_next_state(current, transition_matrix)
    print(f"第 {day} 天系统状态: {current}")
    if current == "故障":
        print("⚠️ 系统已发生不可逆故障，停止模拟。")
        break