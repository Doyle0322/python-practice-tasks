import os

def count_file_types(folder_path):
    files = os.listdir(folder_path)

    file_count = {}

    for file_name in files:
        ext = os.path.splitext(file_name)[1]

        if ext in file_count:
            file_count[ext] += 1
        else:
            file_count[ext] = 1

    return file_count
folder_path = r"D:\test_images"

result = count_file_types(folder_path)

print(result)