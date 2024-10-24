import pytest
from markdown import Table


class TestTable:

    def test_empty_table(self):
        table = Table([], [])
        assert str(table) == ""

        table = Table(["col1", "col2"], [])
        assert str(table) == ""

        table = Table([], ["col1", "col2"])
        assert str(table) == ""

    def test_table_with_headers(self):
        table = Table(["col1", "col2"], [["val1", "val2"]])
        assert str(table) == "| col1 | col2 |\n| --- | --- |\n| val1 | val2 |\n\n"

        table = Table(["col1", "col2"], [["val1", "val2"], ["val3", "val4"]])
        assert str(table) == "| col1 | col2 |\n" + \
                             "| --- | --- |\n" + \
                             "| val1 | val2 |\n" + \
                             "| val3 | val4 |\n\n"

    def test_table_append(self):
        table = Table(["col1", "col2"], [["val1", "val2"]])
        assert str(table) == "| col1 | col2 |\n| --- | --- |\n| val1 | val2 |\n\n"

        table.append_row(["val3", "val4"])
        assert str(table) == "| col1 | col2 |\n" + \
                             "| --- | --- |\n" + \
                             "| val1 | val2 |\n" + \
                             "| val3 | val4 |\n\n"


if __name__ == "__main__":  # pragma: no cover
    pytest.main()
