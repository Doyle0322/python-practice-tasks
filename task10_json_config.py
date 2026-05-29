import json


def load_json_config(file_path):
    """
    高级配置读取器：带防弹衣的 JSON 解析车间
    """
    # ==========================================
    # ⚠️ 【实战默写区】开始
    # 步骤 1: 穿上高阶防弹衣 (try)
    # 步骤 2: 在 try 里面，用 with open 读取 file_path，用 json.load() 拿到字典，并 return 结果
    # 步骤 3: 拦截报错 (except Exception as e)，打印包含 e 的警告供词
    # 步骤 4: 警告完之后，必须 return {} （一个空字典），保证车间有兜底交货！
    # ==========================================
    try:
        with open (file_path, 'r',encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(e)
        return {}



    # ==========================================
    # ⚠️ 【实战默写区】结束
    # ==========================================


# 1. 正常测试（前提是你本地有 config.json 这个文件）
final_dict = load_json_config('config.json')
print("✅ JSON 拿到的字典是:", final_dict)

# 2. 轰炸测试（故意传一个不存在的文件名，看你的防弹衣能不能触发查无此人罪）
bad_dict = load_json_config('confg_bad.json')
print("🛡️ 防弹兜底结果是:", bad_dict)