from data_pipeline.fetch_data import fetch_books_by_author
from data_pipeline.process_data import process_books
from data_pipeline.generate_report import save_to_csv


def main():
    """Runs the full data pipeline: Fetch → Process → Save"""
    author_name = input("Enter an author's name: ")
    book_limit = int(input("Enter number of books to fetch: "))

    # Fetch Data
    books = fetch_books_by_author(author_name, book_limit)

    if not books:
        print("No books found. Exiting.")
        return

    # Process Data
    processed_books = process_books(books)

    # Generate Report
    save_to_csv(processed_books)
    print("✅ Report generated successfully!")


if __name__ == "__main__":
    main()
