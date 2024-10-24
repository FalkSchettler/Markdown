from markdown.markdown_formatter import MarkdownFormatter as MDF


class CodeBlock:
    def __init__(self, text: str, language: str = ""):
        self.text = text
        self.language = language

    def __str__(self):
        return MDF.code_block(self.language, self.text) + MDF.LINE_BREAK
