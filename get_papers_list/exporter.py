import csv
from typing import List, Dict

def export_to_csv(data: List[Dict], filename: str):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["pubmed_id", "title", "publication_date", "non_academic_authors", "company_affiliations"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
