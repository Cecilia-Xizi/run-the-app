
#from datetime import datetime
#
#from app.models.book import Book
#
#from conftest import GOOGLE_SHEETS_TEST_DOCUMENT_ID
#
#def test_books(model_context):
#    # model context ensures tests are using data from the test document:
#    assert Book.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
#
#    # DESTROY ALL:
#
#    Book.destroy_all()
#
#    # SEED RECORDS:
#
#    Book.seed()
#
#    # FIND ALL:
#
#    books = Book.all()
#    assert len(books) == 12
#
#    # CREATE
#
#    # given a dictionary of compatible attributes:
#    new_book = Book(dict(title="My Book", author="Me", year=2024))
#    new_book.save()
#    # persists the record to sheet:
#    books = Book.all()
#    assert len(books) == 13
#    assert books[-1].title == "My Book"
#
#    # FIND:
#
#    book = Book.find(3)
#    assert book.id == 3
#    assert book.title == "The Great Gatsby"
#    assert book.year == 1925
#    assert isinstance(book.created_at, datetime)
#
#    # FILTER:
#
#    books = Book.where(author="J.K. Rowling")
#    assert len(books) == 2
#
