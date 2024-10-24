from markdown.chapter import Chapter


class MarkdownDocument(Chapter):

    def __init__(self, headline: str) -> None:
        super().__init__(headline=headline, level=1)

    def write(self, filename: str):

        with open(filename, "w") as file:
            file.write(self.__str__())
            file.close()

    def __str__(self) -> str:
        return super().__str__()
