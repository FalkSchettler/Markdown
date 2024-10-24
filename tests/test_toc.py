import pytest
from markdown import TableOfContents, Chapter, MarkdownDocument


def create_doc_structure():

    doc: MarkdownDocument = MarkdownDocument("ToC Test")
    toc: TableOfContents = doc.add_toc()
    chapter1: Chapter = doc.add_subchapter("Chapter 1")
    chapter1.add_subchapter("Chapter 1.1")
    chapter1.add_subchapter("Chapter 1.2")
    chapter13: Chapter = chapter1.add_subchapter("Chapter 1.3")
    chapter13.add_subchapter("Chapter 1.3.1")
    chapter13.add_subchapter("Chapter 1.3.2")
    chapter13.add_subchapter("Chapter 1.3.3")
    chapter2: Chapter = doc.add_subchapter("Chapter 2")
    chapter2.add_subchapter("Chapter 2.1")
    chapter2.add_subchapter("Chapter 2.2")
    chapter2.add_subchapter("Chapter 2.3")

    return [doc, toc]


def test_empty_toc():

    doc: MarkdownDocument = MarkdownDocument("ToC Test")
    toc: TableOfContents = doc.add_toc()

    toc_content: str = toc.__str__()
    assert toc_content == ""


def test_simple_toc_structure():

    [doc, toc] = create_doc_structure()

    toc_content: str = toc.__str__()
    assert toc_content == "- [Chapter 1](#Chapter-1)\n" \
                          "  - [Chapter 1.1](#Chapter-11)\n" \
                          "  - [Chapter 1.2](#Chapter-12)\n" \
                          "  - [Chapter 1.3](#Chapter-13)\n" \
                          "    - [Chapter 1.3.1](#Chapter-131)\n" \
                          "    - [Chapter 1.3.2](#Chapter-132)\n" \
                          "    - [Chapter 1.3.3](#Chapter-133)\n" \
                          "- [Chapter 2](#Chapter-2)\n" \
                          "  - [Chapter 2.1](#Chapter-21)\n" \
                          "  - [Chapter 2.2](#Chapter-22)\n" \
                          "  - [Chapter 2.3](#Chapter-23)\n" \
                          "\n"


def test_indent_toc():

    [doc, toc] = create_doc_structure()
    toc.set_indent_spaces(3)

    toc_content: str = toc.__str__()
    assert toc_content == "- [Chapter 1](#Chapter-1)\n" \
                          "   - [Chapter 1.1](#Chapter-11)\n" \
                          "   - [Chapter 1.2](#Chapter-12)\n" \
                          "   - [Chapter 1.3](#Chapter-13)\n" \
                          "      - [Chapter 1.3.1](#Chapter-131)\n" \
                          "      - [Chapter 1.3.2](#Chapter-132)\n" \
                          "      - [Chapter 1.3.3](#Chapter-133)\n" \
                          "- [Chapter 2](#Chapter-2)\n" \
                          "   - [Chapter 2.1](#Chapter-21)\n" \
                          "   - [Chapter 2.2](#Chapter-22)\n" \
                          "   - [Chapter 2.3](#Chapter-23)\n" \
                          "\n"

    toc.set_indent_spaces(0)
    toc_content = toc.__str__()
    assert toc_content == "- [Chapter 1](#Chapter-1)\n" \
                          "- [Chapter 1.1](#Chapter-11)\n" \
                          "- [Chapter 1.2](#Chapter-12)\n" \
                          "- [Chapter 1.3](#Chapter-13)\n" \
                          "- [Chapter 1.3.1](#Chapter-131)\n" \
                          "- [Chapter 1.3.2](#Chapter-132)\n" \
                          "- [Chapter 1.3.3](#Chapter-133)\n" \
                          "- [Chapter 2](#Chapter-2)\n" \
                          "- [Chapter 2.1](#Chapter-21)\n" \
                          "- [Chapter 2.2](#Chapter-22)\n" \
                          "- [Chapter 2.3](#Chapter-23)\n" \
                          "\n"


def test_toc_level_to_include():

    [doc, toc] = create_doc_structure()

    toc.set_level_to_include(1)
    toc_content: str = toc.__str__()
    assert toc_content == "- [Chapter 1](#Chapter-1)\n" \
                          "- [Chapter 2](#Chapter-2)\n" \
                          "\n"

    toc.set_level_to_include(2)
    toc_content: str = toc.__str__()
    assert toc_content == "- [Chapter 1](#Chapter-1)\n" \
                          "  - [Chapter 1.1](#Chapter-11)\n" \
                          "  - [Chapter 1.2](#Chapter-12)\n" \
                          "  - [Chapter 1.3](#Chapter-13)\n" \
                          "- [Chapter 2](#Chapter-2)\n" \
                          "  - [Chapter 2.1](#Chapter-21)\n" \
                          "  - [Chapter 2.2](#Chapter-22)\n" \
                          "  - [Chapter 2.3](#Chapter-23)\n" \
                          "\n"


def test_without_anchor_generation_for_toc():

    expected = "# ToC Test\n" \
               "\n" \
               "- [Chapter 1](#Chapter-1)\n" \
               "  - [Chapter 1.1](#Chapter-11)\n" \
               "  - [Chapter 1.2](#Chapter-12)\n" \
               "  - [Chapter 1.3](#Chapter-13)\n" \
               "    - [Chapter 1.3.1](#Chapter-131)\n" \
               "    - [Chapter 1.3.2](#Chapter-132)\n" \
               "    - [Chapter 1.3.3](#Chapter-133)\n" \
               "- [Chapter 2](#Chapter-2)\n" \
               "  - [Chapter 2.1](#Chapter-21)\n" \
               "  - [Chapter 2.2](#Chapter-22)\n" \
               "  - [Chapter 2.3](#Chapter-23)\n" \
               "\n" \
               "## Chapter 1\n" \
               "\n" \
               "### Chapter 1.1\n" \
               "\n" \
               "### Chapter 1.2\n" \
               "\n" \
               "### Chapter 1.3\n" \
               "\n" \
               "#### Chapter 1.3.1\n" \
               "\n" \
               "#### Chapter 1.3.2\n" \
               "\n" \
               "#### Chapter 1.3.3\n" \
               "\n" \
               "## Chapter 2\n" \
               "\n" \
               "### Chapter 2.1\n" \
               "\n" \
               "### Chapter 2.2\n" \
               "\n" \
               "### Chapter 2.3\n" \
               "\n"

    [doc, toc] = create_doc_structure()

    TableOfContents.set_with_chapter_anchor_id(active=False)
    content: str = doc.__str__()

    assert content == expected


def test_anchor_generation_for_toc():

    expected = "<a id=\"ToC-Test\"></a>\n" \
               "# ToC Test\n" \
               "\n" \
               "- [Chapter 1](#Chapter-1)\n" \
               "  - [Chapter 1.1](#Chapter-11)\n" \
               "  - [Chapter 1.2](#Chapter-12)\n" \
               "  - [Chapter 1.3](#Chapter-13)\n" \
               "    - [Chapter 1.3.1](#Chapter-131)\n" \
               "    - [Chapter 1.3.2](#Chapter-132)\n" \
               "    - [Chapter 1.3.3](#Chapter-133)\n" \
               "- [Chapter 2](#Chapter-2)\n" \
               "  - [Chapter 2.1](#Chapter-21)\n" \
               "  - [Chapter 2.2](#Chapter-22)\n" \
               "  - [Chapter 2.3](#Chapter-23)\n" \
               "\n" \
               "<a id=\"Chapter-1\"></a>\n" \
               "## Chapter 1\n" \
               "\n" \
               "<a id=\"Chapter-11\"></a>\n" \
               "### Chapter 1.1\n" \
               "\n" \
               "<a id=\"Chapter-12\"></a>\n" \
               "### Chapter 1.2\n" \
               "\n" \
               "<a id=\"Chapter-13\"></a>\n" \
               "### Chapter 1.3\n" \
               "\n" \
               "<a id=\"Chapter-131\"></a>\n" \
               "#### Chapter 1.3.1\n" \
               "\n" \
               "<a id=\"Chapter-132\"></a>\n" \
               "#### Chapter 1.3.2\n" \
               "\n" \
               "<a id=\"Chapter-133\"></a>\n" \
               "#### Chapter 1.3.3\n" \
               "\n" \
               "<a id=\"Chapter-2\"></a>\n" \
               "## Chapter 2\n" \
               "\n" \
               "<a id=\"Chapter-21\"></a>\n" \
               "### Chapter 2.1\n" \
               "\n" \
               "<a id=\"Chapter-22\"></a>\n" \
               "### Chapter 2.2\n" \
               "\n" \
               "<a id=\"Chapter-23\"></a>\n" \
               "### Chapter 2.3\n" \
               "\n"

    [doc, toc] = create_doc_structure()

    TableOfContents.set_with_chapter_anchor_id(active=True)
    content: str = doc.__str__()

    assert content == expected


if __name__ == "__main__":  # pragma: no cover
    pytest.main()
