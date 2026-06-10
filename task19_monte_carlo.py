import random


def estimate_pi_monte_carlo(num_darts=1000000):
    """
    蒙特卡洛引擎：暴力估算圆周率

    输入参数：
    num_darts: 投掷的飞镖总数 (默认扔 100 万次)

    期望返回：
    估算出的 Pi 值 (float)
    """
    # 记录落在圆圈内部的飞镖数量
    inside_circle_count = 0

    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 开启一个执行 num_darts 次的 for 循环
    # 步骤 2: 在循环内，用 random.uniform(-1, 1) 生成一个随机的 x 坐标
    # 步骤 3: 在循环内，用 random.uniform(-1, 1) 生成一个随机的 y 坐标
    # 步骤 4: 判断飞镖是否在圆内：如果 x 的平方加上 y 的平方 <= 1
    # 步骤 5: 如果在圆内，将 inside_circle_count 加上 1
    # 步骤 6: 循环彻底结束后，利用公式计算 Pi： 4 * (圆内数量 / 总数量)
    # 步骤 7: return 计算出的 Pi 值
    # ==========================================
    for i in range(num_darts):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y** 2 <= 1:
            inside_circle_count+=1
    pi = 4*(inside_circle_count/num_darts)
    return pi

    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（算力全开）
# ------------------------------------------
# 狂暴模式：扔 100 万根飞镖
estimated_pi = estimate_pi_monte_carlo(1000000)

print("🎯 蒙特卡洛算力验证结果:")
print(f"真正的 Pi 值约为: 3.1415926...")
print(f"代码暴力蒙出的 Pi 值: {estimated_pi}")