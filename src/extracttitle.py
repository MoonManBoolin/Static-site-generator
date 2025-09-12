
def extract_title(markdown):
    print(markdown[0])
    if markdown.strip().startswith("# "):
        return markdown.replace("#", "", 1).strip()
    else:
        raise Exception("Error extracting title")