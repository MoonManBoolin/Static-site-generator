
import os
import pathlib

from generatepage import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        source_entry_path = os.path.join(dir_path_content, entry)
        source_target_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(source_entry_path) and entry.endswith(".md"):
            
            generate_page(source_entry_path, template_path, source_target_path.replace(".md", ".html"), basepath)
        elif os.path.isdir(source_entry_path):
            pathlib.Path(source_target_path).mkdir(parents=True, exist_ok=True)
            generate_pages_recursive(source_entry_path, template_path, source_target_path, basepath)