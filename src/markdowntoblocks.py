

def markdown_to_blocks(markdown):
    result = list(filter(lambda part: part != "", map(lambda x: x.strip(), markdown.split("\n\n"))))
    return result