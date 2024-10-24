from typing import Any, Tuple
from markdown.markdown_formatter import MarkdownFormatter as MDF
from markdown.interfaces import MarkdownElementInterface
from markdown.text_block import TextBlock

# TODO:
# - add support for index in add_unordered_list, add_ordered_list and add_text_block
# - add method to add code block, ... to list item


class ListItem(MarkdownElementInterface):

    def __init__(self, text: str) -> None:
        self.__text: str = text
        self.__items = []

    def set_text(self, text: str) -> None:
        self.__text = text

    def add_text_block(self, text_block: TextBlock) -> TextBlock:
        self.__items.append(text_block)
        return text_block

    def add_ordered_list(self, items: list = list(), index: int = -1) -> "BaseList":
        ordered_list: BaseList = BaseList(items=items)
        ordered_list.indent()
        self.__add_list_to_items(ordered_list, index)
        return ordered_list

    def add_unordered_list(self, items: list = list(), index: int = -1) -> "BaseList":
        unordered_list: BaseList = BaseList(items=items)
        unordered_list.set_dash()
        self.__add_list_to_items(unordered_list, index)
        return unordered_list

    def __add_list_to_items(self, list, index: int) -> "BaseList":
        list.indent()
        if index != -1:
            self.__items.insert(index, list)
        else:
            self.__items.append(list)

    def __str__(self) -> str:

        content: str = self.__text + MDF.LINE_BREAK

        for item in self.__items:
            content += item.__str__() + MDF.LINE_BREAK

        return content


class BaseList(MarkdownElementInterface):

    _indent_spaces: int = 2

    def __init__(self, items: list = list()):
        self._items = []
        self.__prefix: str = ""
        self.__indent_spaces: int = 0

        for item in items:
            self.add_item(item)

    def indent(self):
        self.__indent_spaces = BaseList._indent_spaces

    def set_prefix(self, prefix: str):
        self.__prefix = prefix

    def set_dash(self):
        self.set_prefix("- ")

    def set_star(self):
        self.set_prefix("* ")

    def add_item(self, text: str) -> ListItem:
        o_item: ListItem = ListItem(text)
        self._items.append(o_item)
        return o_item

    def add_ordered_list(self, text: str, items: list = list()) -> Tuple["BaseList", ListItem]:
        list_item: ListItem = ListItem(text)
        ordered_list = list_item.add_ordered_list(items=items)
        self._items.append(list_item)
        return [list_item, ordered_list]

    def add_unordered_list(self, text: str, items: list = list()) -> Tuple["BaseList", ListItem]:
        list_item: ListItem = ListItem(text)
        unordered_list = list_item.add_unordered_list(items=items)
        self._items.append(list_item)
        return [list_item, unordered_list]

    def __str__(self) -> str:
        content = ""
        for index, item in enumerate(self._items):

            # add prefix to item content, ident size of prefix spaces from second line of the item content
            if self.__prefix == "":
                prefix = f"{index+1}. "
            else:
                prefix = self.__prefix
            prefix_size = len(prefix)

            item_content: str = MDF.indent_text(item.__str__(), indent_spaces=prefix_size)
            item_content = item_content[prefix_size:]  # remove prefix from first line of the item content

            item_content = prefix + item_content

            content += item_content

        return content

    def __getitem__(self, key: int) -> Any:
        return self._items[key]


class OrderedList(BaseList):

    def __init__(self, items: list = list()) -> None:
        super().__init__(items=items)

    def __str__(self):
        return super().__str__() + MDF.LINE_BREAK


class UnorderedList(BaseList):

    def __init__(self, items: list = list()) -> None:
        super().__init__(items=items)
        self.set_dash()

    def __str__(self):
        return super().__str__() + MDF.LINE_BREAK


if __name__ == "__main__":  # pragma: no cover

    print("-----------------------------------")
    print("item:")

    item: ListItem = ListItem("item1")
    item.add_text_block("text block line 1")

    print(str(item))
    print("-----------------------------------")
    print("list:")

    base_list: BaseList = BaseList(["item1", "item2"])

    item = base_list[0]
    item.add_text_block("text block line 1")
    item.add_unordered_list(["sub1.1", "sub2.2"])
    item.add_text_block("text block line 2")

    base_list.add_unordered_list("item3", ["sub1", "sub2"])

    print(str(base_list))
    exit()

    print("-----------------------------------")
    print("unordered list:")

    unordered_list: UnorderedList = UnorderedList(["item1", "item2"])
    print(str(unordered_list))

    item = unordered_list.add_item("item3")
    item.add_text_block("text block line 1")
    item.add_text_block("text block line 2")
    print(str(unordered_list))

    [item, sub_list] = unordered_list.add_unordered_list(text="item4", items=["sub1", "sub2"])
    print(unordered_list)
    sub_list.set_star()

    sub_list.add_item("sub3")
    item4 = unordered_list.add_item("item4")

    [item_sub4, uo_list_sub4] = sub_list.add_unordered_list("sub4", ["sub4.1", "sub4.2"])
    item.add_text_block("sub4.1 text block line 1")
    print(str(unordered_list))

    item4.set_text("item4 replaced")
    print(str(unordered_list))

    print("-----------------------------------")
    print("ordered list:")

    ordered_list: OrderedList = OrderedList(["item1", "item2"])
    print(ordered_list)

    ordered_list.add_item("item3")
    print(ordered_list)

    [item, sub_list] = ordered_list.add_ordered_list(text="item4", items=["sub1", "sub2"])

    print(ordered_list)
