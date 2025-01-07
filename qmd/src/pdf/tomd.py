from markitdown import MarkItDown
import glob, os

md = MarkItDown()

for file in glob.glob("*.pdf"):
    print(file)
    result = md.convert(file)
    open(file.replace(".pdf", ".qmd"), "w", encoding="utf-8").write(result.text_content)