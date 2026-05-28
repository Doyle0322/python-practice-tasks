# 模拟从 config.txt 读出来的脏数据，注意第二行是坏的（没有等号）！
dirty_lines = [
    "batch_size=16",
    "model_nameResNet",  # ⚠️ 坏数据
    "epochs=50"
]


def load_config_safe(lines):
    config_dict = {}

    for line in lines:
        clean_line = line.strip()
        try:
            parts = clean_line.split('=')
            key = parts[0]
            value = parts[1]
            config_dict[key] = value
        except:
            print(f'跳过损坏的数据: {clean_line}')
        # ==========================================
        # ⚠️ 【实战默写区】开始
        # 目标：尝试进行 '=' 切割并存入字典。
        # 要求：必须使用 try...except 结构包裹危险动作！
        # 如果报错，不许崩溃，打印警告: f"跳过损坏的数据: {clean_line}"
        # ==========================================

        # ==========================================
        # ⚠️ 【实战默写区】结束
        # ==========================================

    return config_dict


# 测试调用
final_dict = load_config_safe(dirty_lines)
print("✅ 最终安全加载的字典:", final_dict)