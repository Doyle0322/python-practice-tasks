# 准备一个空字典，用来装我们提取出来的参数
config_dict = {}


# 1. 补全语法：用读取模式 ('r') 打开 config.txt
with open('config.txt', 'r', encoding='utf-8') as f:
    # 将文件里的所有行一次性读出来，变成一个列表
    lines = f.readlines()

    # 遍历列表里的每一行数据 (例如: "batch_size=16\n")
    for line in lines:
        # 2. 清洗数据：剥掉这一行末尾恶心的换行符 \n 和多余空格
        clean_line = line.strip()

        # 3. 切割数据：以 '=' 为菜刀，把这行切成两半
        # parts 最终会变成一个列表，比如 ['batch_size', '16']
        parts = clean_line.split('=')

        # 把切出来的名字（左边）和值（右边）存进字典
        key = parts[0]  # 等号左边的是 key
        value = parts[1]  # 等号右边的是 value
        config_dict[key] = value #

print("✅ 成功加载外部配置：")
print(config_dict)