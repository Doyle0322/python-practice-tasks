import os

def make_new_name(prefix, index, ext):
    new_name = f"{prefix}_{index:03d}{ext}"
    return new_name

def get_rename_plan(folder_path, prefix="img"):
    files = os.listdir(folder_path)
    index = 1
    rename_plan = []

    for file_name in files:
        if file_name.endswith((".jpg", ".png", ".jpeg")):
            ext = os.path.splitext(file_name)[1]
            new_name = make_new_name(prefix, index, ext)

            rename_plan.append((file_name, new_name))

            index += 1

    return rename_plan

folder_path = r"D:\test_images"
plan = get_rename_plan(folder_path)

print(plan)