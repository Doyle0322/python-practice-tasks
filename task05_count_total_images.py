import os

def count_image_types(folder_path):
    files = os.listdir(folder_path)

    file_count = {}

    for file_name in files:
        if file_name.endswith((".jpg", ".png", ".jpeg")):

            ext = os.path.splitext(file_name)[1]

            if ext in file_count:
                file_count[ext] += 1
            else:
                file_count[ext] = 1

    total_images =sum(file_count.values())

    return file_count, total_images

folder_path = r"D:\test_images"

result, total = count_image_types(folder_path)

print(result)
print(f"总图片数：{total}")