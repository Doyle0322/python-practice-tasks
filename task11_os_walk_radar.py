import os


def scan_all_images(target_folder):
    """
    雷达扫描器：穿透所有子文件夹，找出所有 .jpg 和 .png 图片的完整路径
    """
    image_paths = []

    # ==========================================
    # ⚠️ 【实战默写区】开始
    # 目标 1: 启动 os.walk(target_folder) 雷达，用 for 循环接收它吐出的三个变量 (root, dirs, files)
    # 目标 2: 在当前层级，遍历所有物资 (for file in files)
    # 目标 3: 用你以前学过的 .endswith() 过滤出 .jpg 或 .png
    # 目标 4: 【极其关键】用 os.path.join() 把 root 和 file 拼成完整路径！
    # 目标 5: 将拼好的完整路径 append 到 image_paths 列表中
    # ==========================================
    for root,dirs,files in os.walk(target_folder):
        for file in files:
            if file.endswith(('.jpg','.png')):
                file_path = os.path.join(root,file)
                image_paths.append(file_path)
    # ==========================================
    # ⚠️ 【实战默写区】结束
    # ==========================================

    return image_paths


# ------------------------------------------
# 外界调用区
# ------------------------------------------
# 假设我们扫描当前的目录 (用 '.' 代表当前目录)
all_images = scan_all_images('.')

print(f"✅ 雷达扫描完毕，共发现 {len(all_images)} 张图片！")
if len(all_images) > 0:
    print("🎯 第一张图片的完整路径是:", all_images[0])