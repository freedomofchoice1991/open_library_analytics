def process_books(book_list):
    """Processes book data and extracts relevant information."""
    processed_books = []
    for book in book_list:
        processed_books.append({
            "title": book.get("title", "Unknown"),
            "author": ", ".join(book.get("author_name", ["Unknown"])),
            "first_publish_year": book.get("first_publish_year", "N/A"),
            "isbn": book.get("isbn", ["N/A"])[0] if "isbn" in book else "N/A",
        })
    return processed_books

if __name__ == "__main__":
    from fetch_data import fetch_books_by_author

    books = fetch_books_by_author("J.K. Rowling", 5)
    processed = process_books(books)
    for book in processed:
        print(book)