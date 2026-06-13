def bayesian_inference(p_fault, p_alarm_given_fault, p_alarm_given_normal):
    """
    贝叶斯逆向推断引擎

    输入参数：
    p_fault: 先验概率 - 芯片天然出故障的概率 P(Fault)
    p_alarm_given_fault: 敏感度 - 芯片真坏了，引发报警的概率 P(Alarm|Fault)
    p_alarm_given_normal: 误报率 - 芯片是好的，但仪器抽风报警的概率 P(Alarm|Normal)

    期望返回：
    后验概率 - 听到报警声后，芯片确实坏了的概率 P(Fault|Alarm)
    """

    # ==========================================
    # ⚠️ 【极限真空默写区】开始
    # 步骤 1: 算出芯片是好的概率 p_normal = 1.0 - 芯片坏的概率
    p_normal = 1.0 - p_fault
    # 步骤 2: 算出“真坏了且报警”的联合概率 prob_true_positive
    #         (公式: 坏的概率 * 坏了引发报警的概率)
    prob_true_positive = p_fault * p_alarm_given_fault
    # 步骤 3: 算出“好好的却误报”的联合概率 prob_false_positive
    #         (公式: 好的概率 * 好的却误报的概率)
    prob_false_postive = p_normal * p_alarm_given_normal
    # 步骤 4: 算出不管好坏、总共报警的概率 p_alarm_total (这就是考研必考的【全概率公式】)
    #         (公式: 步骤 2 算出的结果 + 步骤 3 算出的结果)
    p_alarm_total = prob_true_positive + prob_false_postive
    # 步骤 5: 算出最终的贝叶斯后验概率 posterior_prob
    #         (公式: “真坏了且报警”的概率 / 总报警概率)
    posterior_prob = prob_true_positive / p_alarm_total
    return posterior_prob
    # 步骤 6: return posterior_prob
    # ==========================================

    # ==========================================
    # ⚠️ 【极限真空默写区】结束
    # ==========================================


# ------------------------------------------
# 测试调用区（击碎人类直觉）
# ------------------------------------------
# 行业底蕴：天然次品率只有 1% (极其关键！)
prior_fault = 0.01

# 仪器性能：真坏了能查出 99%
sensitivity = 0.99

# 仪器性能：好好的误报率为 5%
false_alarm = 0.05

result = bayesian_inference(prior_fault, sensitivity, false_alarm)

print("🎯 贝叶斯数学引擎推断结果:")
print(f"在仪器准确率为 99% 的情况下，听到报警声...")
print(f"这块芯片【确实坏了】的真实概率仅为: {result * 100:.2f}%")