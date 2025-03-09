import requests

OPEN_LIBRARY_URL = "https://openlibrary.org/search.json"

def fetch_books_by_author(author_name, limit=5):
    """Fetches book data by author name from Open Library API."""
    params = {"author": author_name, "limit": limit}
    response = requests.get(OPEN_LIBRARY_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("docs", [])  # Return book documents
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []

if __name__ == "__main__":
    books = fetch_books_by_author("George Orwell", 10)
    print(books)
    for book in books:
        print(f"title: {book['title']}\n"
              f"Published year: {book['first_publish_year']}\n"
              f"Languages: {book['language']}\n")