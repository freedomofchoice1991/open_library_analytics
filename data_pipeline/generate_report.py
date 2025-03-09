import csv


def save_to_csv(book_data, filename="book_report.csv"):
    """Saves processed book data to a CSV file."""
    keys = ["title", "author", "first_publish_year", "isbn"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(book_data)

    print(f"Report saved as {filename}")
