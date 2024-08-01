import os

# 指定要扫描的目录路径
path = 'G:\\'

def delete_empty_folder(folder_path):
    # 如果该目录为空，则删除该目录
    if len(os.listdir(folder_path)) == 0:
        print(f"Deleting {folder_path}...")
        os.rmdir(folder_path)

# 开始扫描指定路径及其子目录
for root, dirs, files in os.walk(path, topdown=False):
    for dir in dirs:
        full_dir_path = os.path.join(root, dir)
        delete_empty_folder(full_dir_path)