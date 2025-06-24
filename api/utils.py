import pdfplumber

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def enrich_description(text):
    # Example: add generic job market context
    enrichment = "The ideal candidate should be familiar with modern tools and agile practices."
    return enrichment + "\n\n" + text
