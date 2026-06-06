import math


def standard_normal_pdf(x):
    """
    内置引擎：昨天写的标准正态分布概率密度函数 (mu=0, sigma=1)
    """
    coefficient = 1 / math.sqrt(2 * math.pi)
    exponent = - (x ** 2) / 2
    return coefficient * math.exp(exponent)


def calculate_probability_area(a, b, num_steps=100000):
    """
    微积分引擎：计算曲线从 a 到 b 下方的面积 (即概率)

    输入参数：
    a: 积分下限 (起始点)
    b: 积分上限 (终点)
    num_steps: 切分的矩形数量 (切得越多越精确，默认 10 万刀)
    """
    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 计算每一个小矩形的底边宽度 dx。 (公式：总长度除以切分数量)
    # 步骤 2: 初始化一个变量 total_area = 0.0，用来疯狂装入累加的面积
    # 步骤 3: 开启一个执行 num_steps 次的 for 循环
    #         (提示：用 for i in range(num_steps):)
    # 步骤 4: 在循环内，算出当前矩形左边那条线所在的坐标 current_x
    #         (公式：起点 a 加上 i 个 dx)
    # 步骤 5: 在循环内，调用上面的 standard_normal_pdf(current_x) 算出矩形的高度
    # 步骤 6: 算出当前小矩形的面积 (高度 * 宽度 dx)，并累加到 total_area 中
    # 步骤 7: 循环结束后，return total_area
    # ==========================================
    dx = (b-a)/num_steps
    total_area = 0
    for i in range(num_steps):
        current_x = a + i * dx
        total_area += standard_normal_pdf(current_x) * dx
    return total_area
    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（验证极其经典的 68-95-99.7 法则）
# ------------------------------------------
# 求标准正态分布在 [-1, 1] 之间的概率
prob_1_sigma = calculate_probability_area(-1, 1)

print("🎯 考研数学真题代码验证结果:")
print(f"数据落在正负 1 倍标准差之间的概率为: {prob_1_sigma * 100:.2f}%")
# 预期输出应该极度逼近 68.27%