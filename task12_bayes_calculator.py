def calculate_bayes(p_prior_bad, p_alarm_given_bad, p_alarm_given_good):
    """
    输入参数：
    p_prior_bad: 芯片次品的先天概率 P(Bad)
    p_alarm_given_bad: 芯片真的坏了，机器报警的概率 P(Alarm|Bad)
    p_alarm_given_good: 芯片是好的，机器却瞎报警的概率 P(Alarm|Good)

    期望返回：
    机器报警时，芯片真正损坏的后验概率 P(Bad|Alarm)
    """
    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 算出芯片是好芯片的先天概率 p_prior_good
    # 步骤 2: 算出分子 —— 芯片真坏且报警的组合概率 p_joint_bad_alarm
    # 步骤 3: 算出分母 —— 机器报警的总全概率 p_total_alarm（真坏报警 + 好芯片误报）
    # 步骤 4: 算出后验概率 p_posterior_bad_given_alarm（分子除以分母）
    # 步骤 5: 将最终的后验概率 return 出去
    # ==========================================
    p_prior_good = 1 - p_prior_bad
    p_joint_bad_alarm = p_alarm_given_bad * p_prior_bad
    p_total_alarm =  p_prior_good * p_alarm_given_good + p_prior_bad * p_alarm_given_bad
    p_posterior_bad_given_alarm =  p_joint_bad_alarm /  p_total_alarm
    return p_posterior_bad_given_alarm
    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（验证我们刚才手算的 16.1% 芯片案例）
# ------------------------------------------
result = calculate_bayes(0.01, 0.95, 0.05)

print(f"🎯 考研数学真题代码验证结果:")
print(f"当仪器报警时，该芯片真正损坏的概率为: {result:.4f}")
# 预期输出应该非常接近 0.1610