import os


def create_pdf():
    os.system("python md2pdfy/main.py tests/test.md")


def test_create_pdf():
    create_pdf()
    assert os.path.exists("output.pdf")
    os.remove("output.pdf")
