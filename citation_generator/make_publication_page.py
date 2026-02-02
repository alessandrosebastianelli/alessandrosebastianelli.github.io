import re
from collections import defaultdict

def parse_bibtex_entry(entry):
    """Parse a single BibTeX entry and extract relevant fields."""
    # Extract entry type and cite key
    entry_match = re.match(r'@(\w+)\s*\{([^,]+),', entry)
    if not entry_match:
        return None
    
    entry_type = entry_match.group(1)
    
    # Extract fields
    fields = {}
    
    # Extract author
    author_match = re.search(r'author\s*=\s*\{([^}]+)\}', entry)
    if author_match:
        fields['author'] = author_match.group(1)
    else:
        author_match = re.search(r'author\s*=\s*([^,]+),', entry)
        if author_match:
            fields['author'] = author_match.group(1).strip()
    
    # Extract title
    title_match = re.search(r'title\s*=\s*\{([^}]+)\}', entry)
    if title_match:
        fields['title'] = title_match.group(1)
    
    # Extract year
    year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', entry)
    if year_match:
        fields['year'] = year_match.group(1)
    
    # Extract journal/booktitle/publisher
    journal_match = re.search(r'journal\s*=\s*\{([^}]+)\}', entry)
    if journal_match:
        fields['publication'] = journal_match.group(1)
    else:
        booktitle_match = re.search(r'booktitle\s*=\s*\{([^}]+)\}', entry)
        if booktitle_match:
            fields['publication'] = booktitle_match.group(1)
    
    # Extract URL (try multiple sources with error handling)
    url = None
    
    # Try DOI first (case insensitive) - both DOI= and doi=
    try:
        doi_match = re.search(r'DOI\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE)
        if not doi_match:
            doi_match = re.search(r'DOI\s*=\s*([^,\s}]+)', entry, re.IGNORECASE)
        
        if doi_match:
            doi = doi_match.group(1).strip()
            # Clean up any remaining braces or quotes
            doi = doi.strip('{}"\' ')
            url = f"https://doi.org/{doi}"
    except Exception:
        pass
    
    # If no DOI, try regular URL (case insensitive)
    if not url:
        try:
            url_match = re.search(r'url\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE)
            if url_match:
                url = url_match.group(1).strip()
                # Clean up URL
                url = url.strip('{}"\' ')
        except Exception:
            pass
    
    # If still no URL, try to find ArXiv ID
    if not url:
        try:
            # Look for explicit ArXiv patterns
            arxiv_match = re.search(r'arxiv[:\s]+([0-9]{4}\.[0-9]+v?[0-9]*)', entry, re.IGNORECASE)
            if not arxiv_match:
                arxiv_match = re.search(r'arXiv:([0-9]{4}\.[0-9]+v?[0-9]*)', entry)
            if not arxiv_match:
                # Check if journal is "Arxiv" and look for any arxiv ID in title or elsewhere
                if re.search(r'journal\s*=\s*\{?arxiv\}?', entry, re.IGNORECASE):
                    # Try to find arxiv pattern anywhere in the entry
                    arxiv_match = re.search(r'([0-9]{4}\.[0-9]{4,5}v?[0-9]*)', entry)
            
            if arxiv_match:
                arxiv_id = arxiv_match.group(1)
                url = f"https://arxiv.org/abs/{arxiv_id}"
        except Exception:
            pass
    
    # Store URL if found
    try:
        if url:
            fields['url'] = url
    except Exception:
        pass
    
    return fields


def determine_type(entry_text, fields):
    """Determine if the publication is a Journal, Conference, or Book chapter."""
    entry_lower = entry_text.lower()
    
    # Check for book chapter
    if '@incollection' in entry_lower or '@inbook' in entry_lower:
        return "Book-ch"
    
    # Check publication field
    pub = fields.get('publication', '').lower()
    
    if any(keyword in pub for keyword in ['journal', 'transaction', 'nature', 'letters', 'magazine']):
        return "Journal"
    elif any(keyword in pub for keyword in ['conference', 'symposium', 'igarss', 'workshop', 'proceedings']):
        return "Conference"
    elif any(keyword in entry_lower for keyword in ['book', 'chapter']):
        return "Book-ch"
    
    # Check for ArXiv
    if 'arxiv' in pub:
        return "Journal"  # Treat ArXiv as Journal for sorting
    
    return "Journal"  # Default to Journal


def find_author_position(author_string):
    """Find the position of Alessandro Sebastianelli in the author list."""
    try:
        # Split authors by 'and' or ';'
        authors = re.split(r'\s+and\s+|;\s*', author_string)
        
        # Look for Sebastianelli in various formats
        for idx, author in enumerate(authors, 1):
            if re.search(r'\bSebastianelli\b', author, re.IGNORECASE):
                # Format position with ordinal suffix
                if idx == 1:
                    return "1st"
                elif idx == 2:
                    return "2nd"
                elif idx == 3:
                    return "3rd"
                else:
                    return f"{idx}th"
        
        return "-"
    except Exception:
        return "-"


def format_apa_citation(fields):
    """Format fields into a beautifully structured citation with line breaks."""
    author = fields.get('author', 'Unknown')
    year = fields.get('year', 'n.d.')
    title = fields.get('title', 'Untitled')
    publication = fields.get('publication', '')
    
    # Clean up author formatting - use commas instead of semicolons
    author = author.replace(' and ', ', ')
    
    # Bold Alessandro Sebastianelli's name (various formats)
    author = re.sub(
        r'\b(Alessandro\s+Sebastianelli|A\.\s*Sebastianelli|A\s+Sebastianelli|Sebastianelli,?\s*Alessandro|Sebastianelli,?\s*A\.?)\b',
        r'**\1**',
        author,
        flags=re.IGNORECASE
    )
    
    # Build beautifully formatted citation with line breaks
    # Format: Authors (Year)
    #         "Title"
    #         Journal/Conference
    citation = f"{author} ({year})"
    citation += f"<br/>*\"{title}\"*"
    
    # Add publication on new line if available
    if publication:
        citation += f"<br/>*{publication}*"
    
    return citation


def parse_bibtex_file(filepath):
    """Parse a BibTeX file and return a list of publications."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split entries by @ symbol
    entries = re.split(r'\n\s*@', content)
    entries = ['@' + entry if not entry.startswith('@') else entry for entry in entries if entry.strip()]
    
    publications = []
    
    for entry in entries:
        if not entry.strip() or entry.strip().startswith('%'):
            continue
        
        fields = parse_bibtex_entry(entry)
        if fields and 'year' in fields:
            apa = format_apa_citation(fields)
            pub_type = determine_type(entry, fields)
            author_pos = find_author_position(fields.get('author', ''))
            
            pub = {
                'apa': apa,
                'year': fields['year'],
                'type': pub_type,
                'url': fields.get('url', ''),
                'position': author_pos,
            }
            publications.append(pub)
    
    return publications


def generate_markdown(publications, output_file):
    """Generate markdown file with publications organized by year."""
    # Group publications by year
    pubs_by_year = defaultdict(list)
    for pub in publications:
        pubs_by_year[pub['year']].append(pub)
    
    # Sort years in descending order
    sorted_years = sorted(pubs_by_year.keys(), reverse=True)
    
    # Start building markdown content
    md_content = """---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}


I started co-authoring scientific papers since 2018, during these years I collaborated with many researchers

![](/images/collaborations.png)


## Books

### Artificial Intelligence Applied to Satellite-based Remote Sensing Data for Earth Observation


> **Editors:**\\
> Maria Pia Del Rosso; Alessandro Pia Sebastianelli; Silvia Liberata Ullo\\
> Published in 2021\\
> 283 pages\\
> ISBN: 978-1-83953-212-2\\
> e-ISBN: 978-1-83953-213-9\\
> https://doi.org/10.1049/PBTE098E


Buy it on: [IET Digital Library](https://digital-library.theiet.org/doi/book/10.1049/pbte098e) or [Amazon](https://www.amazon.it/Artificial-Intelligence-Applied-Satellite-based-Observation/dp/1839532122)


## Papers

"""
    
    # Add publications by year
    for year in sorted_years:
        md_content += f"### {year}\n\n"
        md_content += "| apa | year | type | position | url |\n"
        md_content += "|-----|------|------|----------|-----|\n"
        
        # Sort publications within each year by author/title
        sorted_pubs = sorted(pubs_by_year[year], key=lambda x: x['apa'])
        
        for pub in sorted_pubs:
            try:
                url_link = f"[url]({pub['url']})" if pub.get('url') else "-"
            except Exception:
                url_link = "-"
            
            try:
                position = pub.get('position', '-')
                md_content += f"|{pub['apa']}|{pub['year']}|{pub['type']}|{position}|{url_link}|\n"
            except Exception:
                # Skip entries that cause errors
                continue
        
        md_content += "\n"
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Markdown file generated: {output_file}")


if __name__ == '__main__':
    BIB_FILE = 'citation_generator/works.bib'
    OUTPUT_FILE = '_pages/publications.md'
    
    print("Parsing BibTeX file...")
    publications = parse_bibtex_file(BIB_FILE)
    print(f"Found {len(publications)} publications")
    
    print("Generating markdown file...")
    generate_markdown(publications, OUTPUT_FILE)
    print("Done!")