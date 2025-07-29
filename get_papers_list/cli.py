import argparse
from .api_client import search_pubmed, fetch_pubmed_details
from .filter import parse_pubmed_xml
from .exporter import export_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors")
    parser.add_argument("query", type=str, help="PubMed query string")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()

    ids = search_pubmed(args.query)
    if args.debug:
        print(f"Found {len(ids)} papers for query '{args.query}'")

    xml_data = fetch_pubmed_details(ids)
    filtered_papers = parse_pubmed_xml(xml_data)

    if args.file:
        export_to_csv(filtered_papers, args.file)
        print(f"Exported {len(filtered_papers)} papers to {args.file}")
    else:
        for paper in filtered_papers:
            print(paper)

if __name__ == "__main__":
    main()
