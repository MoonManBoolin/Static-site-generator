import os
import pathlib
import shutil
from copystatic import copy_contents_helper
from generatepages import generate_pages_recursive


def main():
    public = "./public"
    static = "./static"
    content_md = "./content"
    template_path = "./template.html"
    if os.path.exists(public):
        try:
            shutil.rmtree(public)
        except OSError as e:
            print(f"Error deleting folder: {e}")
    pathlib.Path(public).mkdir(parents=True, exist_ok=True)
    copy_contents_helper(static, public)
    generate_pages_recursive(content_md, template_path, public)
    
if __name__ == "__main__":
    main()