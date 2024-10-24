import pytest
from markdown import UnorderedList, OrderedList, ListItem


class TestListItem:

    def test_item_insert_add(self):

        item: ListItem = ListItem("List Item")

        item.add_ordered_list(['Item4', 'Item5', 'Item6'])

        content = str(item)

        assert content == "List Item\n1. Item4\n2. Item5\n3. Item6\n\n"

        item.add_ordered_list(items=['Item1', 'Item2', 'Item3'], index=0)

        content = str(item)

        assert content == "List Item\n" \
                          "1. Item1\n2. Item2\n3. Item3\n\n" \
                          "1. Item4\n2. Item5\n3. Item6\n\n"

    def test_item_text_bloc(self):

        item: ListItem = ListItem("List Item")
        item.add_text_block("Test Text")

        content = str(item)

        assert content == "List Item\nTest Text\n"


class TestUnorderedLists:

    def test_creation_empty_list_(self):

        unordered_list: UnorderedList = UnorderedList()
        unordered_list.add_item("item1")

        content = str(unordered_list)
        assert content == "- item1\n\n"

    def test_creation_initialized_list(self):

        unordered_list: UnorderedList = UnorderedList(["item1", "item2"])

        content = str(unordered_list)
        assert content == "- item1\n" + "- item2\n\n"

    def test_creation_initialized_list_with_star(self):

        unordered_list: UnorderedList = UnorderedList(["item1", "item2"])
        unordered_list.set_star()

        content = str(unordered_list)
        assert content == "* item1\n" + "* item2\n\n"

    def test_new_add_new_item(self):

        unordered_list: UnorderedList = UnorderedList(["item1", "item2"])
        unordered_list.add_item("item3")

        content = str(unordered_list)
        assert content == "- item1\n" + "- item2\n" + "- item3\n\n"

    def test_new_sub_list(self):

        unordered_list: UnorderedList = UnorderedList(["item1", "item2"])
        unordered_list.add_unordered_list("item3", ["sub1", "sub2"])

        content = str(unordered_list)
        assert content == "- item1\n" + "- item2\n" + "- item3\n" + "  - sub1\n" + "  - sub2\n\n"

        unordered_list.add_item("item4")
        content = str(unordered_list)
        assert content == "- item1\n" + "- item2\n" + "- item3\n" + "  - sub1\n" + "  - sub2\n" + "- item4\n\n"


class TestOrderedLists:

    def test_creation_empty_list_(self):

        ordered_list: OrderedList = OrderedList()
        ordered_list.add_item("item1")

        content = str(ordered_list)
        assert content == "1. item1\n\n"

    def test_creation_initialized_list(self):

        ordered_list: OrderedList = OrderedList(["item1", "item2"])

        content = str(ordered_list)
        assert content == "1. item1\n" + "2. item2\n\n"

    def test_new_sub_list(self):

        ordered_list: OrderedList = OrderedList(["item1", "item2"])
        ordered_list.indent()
        ordered_list.add_ordered_list("item3", ["sub1", "sub2"])

        content = str(ordered_list)
        assert content == "1. item1\n" + "2. item2\n" + "3. item3\n" + "   1. sub1\n" + "   2. sub2\n\n"

        ordered_list.add_item("item4")
        content = str(ordered_list)
        assert content == "1. item1\n" + "2. item2\n" + "3. item3\n" + "   1. sub1\n" + "   2. sub2\n" + "4. item4\n\n"

    def test_index(self):

        ordered_list: OrderedList = OrderedList(["item1", "item2"])

        item: ListItem = ordered_list[1]

        item.set_text("item2 (manipulated)")
        content: str = str(ordered_list)

        assert content == "1. item1\n" + "2. item2 (manipulated)\n\n"


if __name__ == "__main__":  # pragma: no cover
    pytest.main()
