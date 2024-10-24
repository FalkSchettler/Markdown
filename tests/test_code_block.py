import pytest
from utils import link_to_requirement
from markdown import CodeBlock


@link_to_requirement("Req.1")
class TestCodeBlock:

    def test_content_without_language(self):
        code = CodeBlock("Code without Language")
        assert str(code) == "```\nCode without Language\n```\n"

    def test_content_with_language(self):
        code = CodeBlock("Code without Language", "python")
        assert str(code) == "```python\nCode without Language\n```\n"


if __name__ == "__main__":  # pragma: no cover
    pytest.main()
