import os
# ------------------------------------------
# 你的专属加工车间
# ------------------------------------------
def load_config(file_path):
    """
    这是一个专业的说明文档 (Docstring)
    功能: 读取外部配置文件，返回参数字典
    """
    config_dict = {}

    # ==========================================
    # ⚠️ 【实战默写区】开始
    # 请在这里默写 with open() 读取逻辑、循环遍历、
    # strip() 清洗以及 split('=') 切割的代码。
    # 你的变量必须叫 file_path，而不是写死 'config.txt'！
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            clean_lines = line.strip()
            parts = clean_lines.split('=')
            key = parts[0]
            value = parts[1]
            config_dict[key] = value
    # ==========================================
    # ⚠️ 【实战默写区】结束
    # ==========================================

    # 车间交货
    return config_dict
# ------------------------------------------
# 外界调用区（模拟大模型主程序）
# ------------------------------------------
# 直接调用你的黑盒，传入文件名，拿到成品字典
final_config = load_config('config.txt')

print("✅ 黑盒封装调用成功！")
print("拿到的配置参数为:", final_config)