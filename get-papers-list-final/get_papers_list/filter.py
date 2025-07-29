from typing import List, Dict
import xml.etree.ElementTree as ET

NON_ACADEMIC_KEYWORDS = ["pharma", "biotech", "inc", "corp", "ltd"]

def parse_pubmed_xml(xml_data: str) -> List[Dict]:
    root = ET.fromstring(xml_data)
    papers = []
    for article in root.findall(".//PubmedArticle"):
        paper = {
            "pubmed_id": article.findtext(".//PMID"),
            "title": article.findtext(".//ArticleTitle"),
            "publication_date": article.findtext(".//PubDate/Year") or "N/A"
        }
        authors, companies = [], []
        for author in article.findall(".//Author"):
            affiliation = author.findtext(".//Affiliation")
            if affiliation and any(k in affiliation.lower() for k in NON_ACADEMIC_KEYWORDS):
                authors.append(f"{author.findtext('LastName')} {author.findtext('ForeName')}")
                companies.append(affiliation)
        if authors:
            paper["non_academic_authors"] = authors
            paper["company_affiliations"] = companies
            papers.append(paper)
    return papers
