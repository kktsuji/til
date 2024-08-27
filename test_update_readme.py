"Unit tests for update_readme.py"

from update_readme import (
    _BASE_URL,
    _make_header,
    _get_categories,
    _make_article_list,
    _replace_words,
)


def test_get_header():
    expect = "# TIL\n\nToday I Learned\n\n0 TILs and counting...\n\n"
    result = _make_header(0)
    assert expect == result


def test_get_categories():
    files = [
        "./aws/article0.md",
        "./bash/article0.md",
        "./bash/article1.md",
        "./python/article0.md",
        "./python/article1.md",
    ]
    expect = ["aws", "bash", "python"]
    result = _get_categories(files)
    assert expect == result


def test_replace_words():
    src = "## Test-driven-development\n\nTdd Key Concepts"
    expect = "## Test-Driven Development (TDD)\n\nTDD Key Concepts"
    result = _replace_words(src)
    assert expect == result


def test_make_article_list():
    files = [
        "./aws/article0.md",
        "./bash/article0.md",
        "./bash/article1.md",
        "./python/article0.md",
        "./python/article1.md",
    ]
    expect = (
        "## Aws\n\n"
        f"- [Article0]({_BASE_URL}aws/article0.md)\n\n"
        "## Bash\n\n"
        f"- [Article0]({_BASE_URL}bash/article0.md)\n"
        f"- [Article1]({_BASE_URL}bash/article1.md)\n\n"
        "## Python\n\n"
        f"- [Article0]({_BASE_URL}python/article0.md)\n"
        f"- [Article1]({_BASE_URL}python/article1.md)\n\n"
    )
    result = _make_article_list(files)
    assert expect == result
