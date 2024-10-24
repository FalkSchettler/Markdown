from markdown_generator.markdown_formatter import MarkdownFormatter
from markdown_generator.interfaces import MarkdownElementInterface

class OrderedList(MarkdownElementInterface):

    def __init__(self, items) -> None:
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):

        content = ""

        # add numbers as prefix to each item
        for index, item in enumerate(self.items):
            content += str(index + 1) + ". " + item + MarkdownFormatter.LINE_BREAK

        return content


class UnorderedList(MarkdownElementInterface):

    def __init__(self, items: list = list()) -> None:
        self.add_ordered_list(items)
        self.prefix = "- "

    def set_asterisk(self):
        self.prefix = "* "

    def set_dash(self):
        self.prefix = "- "

    def set_plus(self):
        self.prefix = "+ "

    def add_item(self, item):
        self.items.append(item)

    # def add_ordered_list(self, items: list = []):
    #     ordered_list = OrderedList(items)
    #     self.items.append(ordered_list)
    #     return ordered_list

    def append_unordered_list(self, ordered_list):
        self.items.append(ordered_list)

    def to_enumeration(self):
        pass

    def __str__(self):

        content = ""

        for item in self.items:
            content += "- " + item + MarkdownFormatter.LINE_BREAK

        return content

