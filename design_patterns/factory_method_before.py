"""
Let's assume we have a simple application that creates different types of documents:
Word documents and PDF documents. Without the Factory Method, we might have code like this:
"""


class WordDocument:
    def __init__(self):
        self.content = "Word Document Content"

    def display(self):
        print(self.content)


class PDFDocument:
    def __init__(self):
        self.content = "PDF Document Content"

    def display(self):
        print(self.content)


def create_document(doc_type):
    if doc_type == "word":
        return WordDocument()
    elif doc_type == "pdf":
        return PDFDocument()
    else:
        raise ValueError("Unknown document type")


if __name__ == '__main__':
    # Client code
    doc = create_document("word")
    doc.display()

    doc = create_document("pdf")
    doc.display()
