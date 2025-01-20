import re
import spacy
import logging

logging.basicConfig(level=logging.INFO)

# Load spaCy's pre-trained model for English
nlp = spacy.load("en_core_web_sm")

def anonymize_resume(resume_text):
    """
    Anonymizes personal information in a resume.
    
    Args:
    - resume_text (str): The text content of the resume.
    
    Returns:
    - str: Anonymized resume text.
    """
    logging.info("Starting anonymization...")

    # Redact email addresses
    anonymized_text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[REDACTED EMAIL]', resume_text)
    
    # Redact phone numbers (handles various formats)
    anonymized_text = re.sub(r'\b(?:\+?\d{1,3})?[ -]?\(?\d{1,4}?\)?[ -]?\d{1,4}[ -]?\d{1,4}[ -]?\d{1,9}\b', '[REDACTED PHONE]', anonymized_text)
    
    # Redact addresses (enhanced regex)
    anonymized_text = re.sub(
        r'\b\d{1,5}(?: [A-Za-z0-9.,]+)+(?: Street|St|Avenue|Ave|Boulevard|Blvd|Road|Rd|Drive|Dr|Court|Ct|Lane|Ln|Way|Place|Pl)\b',
        '[REDACTED ADDRESS]', anonymized_text
    )

    # Redact names, locations, and other entities using spaCy's NER
    doc = nlp(anonymized_text)
    spans = [(ent.start_char, ent.end_char) for ent in doc.ents if ent.label_ in ['PERSON', 'GPE', 'ORG', 'DATE', 'TIME']]
    for start, end in sorted(spans, key=lambda x: x[0], reverse=True):
        anonymized_text = anonymized_text[:start] + "[REDACTED]" + anonymized_text[end:]

    logging.info("Anonymization completed.")
    return anonymized_text

def main():
    # Example usage:
    resume_text = """Thirumaran Asokan
                     Address: 123 Main St, City
                     Phone: 0744200
                     Email: Thiru.a@example.com"""
    anonymized_resume = anonymize_resume(resume_text)
    print("Anonymized Resume:")
    print(anonymized_resume)

if __name__ == "_main_":
    main()