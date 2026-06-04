def calc_expectation_and_variance(prob_dist):
    """
    输入参数：
    prob_dist: 一个字典，Key是随机变量的值(x)，Value是对应的概率(p)

    期望返回：
    包含两个值的元组: (期望, 方差)
    """
    # ex 对应 E(X)
    ex = 0.0
    # ex2 对应 E(X^2)
    ex2 = 0.0

    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 使用 for x, p in prob_dist.items(): 遍历这个字典
    # 步骤 2: 在循环内，将 x * p 累加给 ex
    # 步骤 3: 在循环内，将 (x的平方) * p 累加给 ex2。 (提示: Python里平方是 x ** 2)
    # 步骤 4: 循环结束后，利用考研公式算出方差 variance = E(X^2) - [E(X)]^2
    # 步骤 5: return ex, variance
    # ==========================================
    for x,p in prob_dist.items():
        ex +=  x * p
        ex2 += (x **2)* p
    variance = ex2 - ex*ex
    return ex, variance
    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（验证我们的硬件寿命分布）
# ------------------------------------------
# 寿命分布律字典：2年(10%), 3年(20%), 4年(40%), 5年(30%)
chip_lifespan_dist = {2: 0.1, 3: 0.2, 4: 0.4, 5: 0.3}

expectation, variance = calc_expectation_and_variance(chip_lifespan_dist)

print("🎯 考研数学真题代码验证结果:")
print(f"该批次硬件的数学期望 E(X) = {expectation:.2f} 年")
print(f"该批次硬件的方差 D(X) = {variance:.2f}")