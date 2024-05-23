"""
After Refactoring with the Factory Method Design Pattern
We refactor the code to use the Factory Method design pattern by creating a Creator class that declares the factory
method, and concrete creators that implement this method.
"""
from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def display(self):
        pass


class WordDocument(Document):
    def __init__(self):
        self.content = "Word Document Content"

    def display(self):
        print(self.content)


class PDFDocument(Document):
    def __init__(self):
        self.content = "PDF Document Content"

    def display(self):
        print(self.content)


class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

    def render_document(self):
        doc = self.create_document()
        doc.display()


class WordDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return WordDocument()


class PDFDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return PDFDocument()


if __name__ == '__main__':
    # Client code
    word_creator = WordDocumentCreator()
    word_creator.render_document()

    pdf_creator = PDFDocumentCreator()
    pdf_creator.render_document()
