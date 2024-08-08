
def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    for block in markdown.split("\n\n"):
        if block.strip():
            blocks.append(block.strip())
    return blocks

