import os

def make_new_name(prefix, index, ext):
    new_name = f"{prefix}_{index:03d}{ext}"
    return new_name

def preview_rename_images(folder_path, prefix="img"):
    index = 1
    files = os.listdir(folder_path)

    for file_name in files:
        if file_name.endswith((".jpg", ".png", ".jpeg")):
            ext = os.path.splitext(file_name)[1]
            new_name = make_new_name(prefix ,index ,ext)
            print(f"{file_name}-------->{new_name}")
            index += 1

folder_path = r"D:\test_images"
preview_rename_images(folder_path)
