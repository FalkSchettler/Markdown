from utils import link_to_requirement
from markdown.chapter import Chapter


@link_to_requirement("Req.2")
class TestChapter:

    def test_chapter_initialization(self):
        chapter = Chapter("Introduction", 1)
        assert chapter.get_headline() == "Introduction"
        assert chapter.get_level() == 1
        assert chapter.get_subchapters() == []

    def test_add_text_block(self):
        chapter = Chapter("Introduction", 1)
        text_block = chapter.add_text_block("This is a text block.")
        assert text_block is not None
        assert "This is a text block." in str(chapter)

    def test_add_subchapter(self):
        chapter = Chapter("Introduction", 1)
        subchapter = chapter.add_subchapter("Subchapter 1")
        assert subchapter.get_headline() == "Subchapter 1"
        assert subchapter.get_level() == 2
        assert subchapter in chapter.get_subchapters()

    def test_add_table(self):
        chapter = Chapter("Introduction", 1)
        headers = ["Header1", "Header2"]
        rows = [["Row1Col1", "Row1Col2"], ["Row2Col1", "Row2Col2"]]
        table = chapter.add_table(headers, rows)
        assert table is not None
        assert "Header1" in str(chapter)
        assert "Row1Col1" in str(chapter)

    def test_add_ordered_list(self):
        chapter = Chapter("Introduction", 1)
        items = ["Item 1", "Item 2"]
        ordered_list = chapter.add_ordered_list(items)
        assert ordered_list is not None
        assert "Item 1" in str(chapter)

    def test_add_unordered_list(self):
        chapter = Chapter("Introduction", 1)
        items = ["Item A", "Item B"]
        unordered_list = chapter.add_unordered_list(items)
        assert unordered_list is not None
        assert "Item A" in str(chapter)

    def test_add_toc(self):
        pass
        # chapter = Chapter("Introduction", 1)
        # toc = chapter.add_toc()
        # assert toc is not None
        # assert toc in str(chapter)
