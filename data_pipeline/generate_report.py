import csv


def save_to_csv(book_data, filename="book_report.csv"):
    """Saves processed book data to a CSV file."""
    keys = ["title", "author", "first_publish_year", "isbn"]

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(book_data)

    print(f"Report saved as {filename}")


if __name__ == "__main__":
    from process_data import process_books
    from fetch_data import fetch_books_by_author

    books = fetch_books_by_author("George Orwell", 5)
    processed_books = process_books(books)
    save_to_csv(processed_books)
