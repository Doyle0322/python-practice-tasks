import os

# 模拟你 Task04 和 Task05 统计出的成果
file_counts = {'jpg': 120, 'png': 30, 'txt': 5}
total_images = 150

# 准备生成报告的文件名
report_name = "dataset_report.txt"

# 1. 补全语法：用写入模式 ('w') 打开 report_name
with open(report_name,'w' , encoding='utf-8') as f:
    f.write("=== AI 数据集清洗报告 ===\n")

    # 2. 补全 f-string：写入总图片数量，并换行
    f.write(f"有效图片总数: {total_images}\n")
    f.write("------------------------\n")

    # 遍历字典写入详情
    for ext, count in file_counts.items():
        # 3. 补全 f-string：生成类似 "后缀 jpg 数量: 120" 的格式，并必须换行！
        f.write(f"后缀{ext} 数量{count}\n")

print("✅ 报告已成功生成至本地硬盘！")