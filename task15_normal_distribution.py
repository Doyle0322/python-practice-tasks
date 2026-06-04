import math


def calculate_normal_pdf(x, mu, sigma):
    """
    输入参数：
    x: 你想要查询的特定数值（比如想查零件尺寸为 0.5 时的概率密度）
    mu: 期望 (均值)
    sigma: 标准差

    期望返回：
    在 x 点的概率密度值 (float类型)
    """
    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 算出左边的系数 coefficient = 1 / (sigma * 根号下(2 * pi))
    # 步骤 2: 算出 e 头顶上的指数部分 exponent = - (x - mu)的平方 / (2 * sigma的平方)
    # 步骤 3: 算出最终结果 result = coefficient * math.exp(exponent)
    # 步骤 4: return result
    # ==========================================
    coefficient = 1/(sigma*math.sqrt(2*math.pi))
    exponent = -(x-mu)**2/(2*sigma**2)
    result = coefficient * math.exp(exponent)
    return result
    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（验证标准正态分布 N(0, 1)）
# ------------------------------------------
# 考研最高频考点：标准正态分布 (期望=0, 标准差=1)
# 理论上在 x=0 (最顶峰) 的概率密度大概是 0.3989

pdf_value = calculate_normal_pdf(x=0, mu=0, sigma=1)

print("🎯 考研数学真题代码验证结果:")
print(f"标准正态分布在 x=0 处的概率密度为: {pdf_value:.4f}")