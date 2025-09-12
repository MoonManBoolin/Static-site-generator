import os
import pathlib
import shutil

def copy_contents_helper(source_dir, target_dir):
    if not os.path.exists(source_dir):
        return
    contents = os.listdir(source_dir)
    for item in contents:
        source_item_path = os.path.join(source_dir, item)
        target_item_path = os.path.join(target_dir, item)
        if os.path.isfile(source_item_path):
            shutil.copy(source_item_path, target_item_path)
            print("COPIED FILE")
        elif os.path.isdir(source_item_path):
            pathlib.Path(target_item_path).mkdir(parents=True, exist_ok=True)
            print("COPIED FOLDER")
            copy_contents_helper(source_item_path, target_item_path)