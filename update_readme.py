"""Provide functionality to update README.md file"""

import glob

_BASE_URL = "https://github.com/kktsuji/til/blob/main/"
_REPLACE_LIST = {
    "## Test-driven-development": "## Test-Driven Development (TDD)",
    "Tdd Key Concepts": "TDD Key Concepts",
}


def _make_header(num):
    return f"# TIL\n\nToday I Learned\n\n{num} TILs and counting...\n\n"


def _get_categories(files):
    categories = []
    for file in files:
        category = file.split("/")[1]
        if category not in categories:
            categories.append(category)
    return categories


def _replace_words(src):
    dst = src
    for key, value in _REPLACE_LIST.items():
        dst = dst.replace(key, value)
    return dst


def _make_article_list(files):
    categories = _get_categories(files)
    contents = ""
    for category in categories:
        contents += f"## {category.capitalize()}\n\n"
        for file in files:
            if category in file:
                title = file.split("/")[-1].replace(".md", "").replace("-", " ").title()
                contents += f"- [{title}]({_BASE_URL}{file[2:]})\n"
        contents += "\n"
    return _replace_words(contents)


def main():
    """Main function to update README.md file"""
    files = sorted(glob.glob("./*/*.md"))
    contents = _make_header(len(files))
    contents += _make_article_list(files)
    with open("README.md", "w") as file:
        file.write(contents)


if __name__ == "__main__":
    main()
