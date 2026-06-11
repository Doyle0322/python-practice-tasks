import random


def simulate_lln(num_tosses=1000):
    """
    大数定律动态收敛引擎

    输入参数：
    num_tosses: 投掷骰子的总次数

    期望返回：
    包含每次投掷后“动态平均值”的列表 (List)
    """
    # 记录每一次的动态平均值 (心电图轨迹)
    running_averages = []
    # 记录当前掷出骰子的点数总和
    current_sum = 0

    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 开启 for 循环，变量为 i，从 1 跑到 num_tosses (包括 num_tosses)
    #         提示: for i in range(1, num_tosses + 1):
    # 步骤 2: 在循环内，掷一次骰子(1到6)，并把结果累加给 current_sum
    # 步骤 3: 算出【截止到当前第 i 次】的动态平均值 current_mean
    # 步骤 4: 把这个 current_mean 追加到 running_averages 列表里
    # 步骤 5: 循环结束后，return running_averages
    # ==========================================
    for i in range(1,num_tosses+1):
        current_sum += random.randint(1,6)
        current_mean = current_sum/i
        running_averages.append(current_mean)
    return running_averages
    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（验证收敛性）
# ------------------------------------------
tosses = 5000
averages_history = simulate_lln(tosses)

print("🎯 大数定律代码验证结果:")
print(f"前 5 次的剧烈震荡均值: {averages_history[:5]}")
print(f"最后 5 次的绝对收敛均值: {averages_history[-5:]}")
# 理论上，最后的均值会死死咬住 3.5000 不放！