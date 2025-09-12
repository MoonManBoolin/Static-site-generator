
def extract_title(markdown):
    print(markdown[0])
    if markdown.strip().startswith("# "):
        return markdown.replace("#", "", 1).strip().split("\n")[0]
    else:
        raise Exception("Error extracting title")