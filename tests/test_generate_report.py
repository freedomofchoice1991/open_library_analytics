import os
import csv
from data_pipeline.generate_report import save_to_csv


def test_save_to_csv():
    test_data = [
        {"title": "Test Book", "author": "John Doe", "first_publish_year": 2020, "isbn": "1234567890"}
    ]
    filename = "test_report.csv"

    save_to_csv(test_data, filename)

    assert os.path.exists(filename)  # Check if the file was created

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0]["title"] == "Test Book"
    assert rows[0]["author"] == "John Doe"
    assert rows[0]["first_publish_year"] == "2020"
    assert rows[0]["isbn"] == "1234567890"

    os.remove(filename)  # Clean up the test file
