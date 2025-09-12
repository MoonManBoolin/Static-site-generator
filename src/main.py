import os
import pathlib
import shutil
import sys
from copystatic import copy_contents_helper
from generatepages import generate_pages_recursive


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    public = "./docs"
    static = "./static"
    content_md = "./content"
    template_path = "./template.html"
    if os.path.exists(public):
        try:
            shutil.rmtree(public)
        except OSError as e:
            print(f"Error deleting folder: {e}")
    pathlib.Path(public).mkdir(parents=True, exist_ok=True)
    print("COPYING CONTENTS AND GENERATING PAGES...")
    copy_contents_helper(static, public)
    generate_pages_recursive(content_md, template_path, public, basepath)
    
if __name__ == "__main__":
    main()