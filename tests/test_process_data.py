from data_pipeline.process_data import process_books


def test_process_books():
    books = [
        {
            "title": "Test Book",
            "author_name": ["John Doe"],
            "first_publish_year": 2020,
            "isbn": ["1234567890"]
        }
    ]
    processed = process_books(books)

    assert len(processed) == 1
    assert processed[0]["title"] == "Test Book"
    assert processed[0]["author"] == "John Doe"
    assert processed[0]["first_publish_year"] == 2020
    assert processed[0]["isbn"] == "1234567890"


def test_process_books_missing_fields():
    books = [{}]  # Book with missing fields
    processed = process_books(books)

    assert len(processed) == 1
    assert processed[0]["title"] == "Unknown"
    assert processed[0]["author"] == "Unknown"
    assert processed[0]["first_publish_year"] == "N/A"
    assert processed[0]["isbn"] == "N/A"
