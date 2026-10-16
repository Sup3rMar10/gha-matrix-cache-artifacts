from app.text import slugify


def test_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_extra_spaces():
    assert slugify("  a   b  ") == "a-b"


def test_empty():
    assert slugify("") == ""
