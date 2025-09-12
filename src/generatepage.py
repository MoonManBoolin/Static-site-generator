import pathlib
from extracttitle import extract_title
from markdowntohtmlnode import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        md = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    title = extract_title(md)
    html_content = markdown_to_html_node(md)
    html_content = html_content.to_html()
    
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    html = html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    dest_path = pathlib.Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html)