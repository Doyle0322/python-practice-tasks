# 功能：批量预览或执行图片的重命名
# 学习点：函数、默认参数。os.listdir / os.path.join / os.path.splitext/
import os

def make_new_name(prefix, index, ext):
    new_name = f"{prefix}_{index:03d}{ext}"
    return new_name

def rename_images(folder_path, prefix="img", execute=False):
    files = os.listdir(folder_path)
    index = 1

    for file_name in files:
        if file_name.endswith((".jpg", ".png", ".jpeg")):
            ext = os.path.splitext(file_name)[1]
            new_name = make_new_name(prefix, index, ext)

            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)

            if execute:
                os.rename(old_path, new_path)
                print(f"已重命名：{file_name} -> {new_name}")
            else:
                print(f"预览：{file_name} -> {new_name}")

            index += 1

folder_path = r"D:\test_images"

rename_images(folder_path, prefix="img", execute=False)