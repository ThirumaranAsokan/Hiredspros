import re
import spacy

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
    # Redact email addresses
    anonymized_text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[REDACTED EMAIL]', resume_text)
    
    # Redact phone numbers (handles various formats)
    anonymized_text = re.sub(r'\b(?:\+?\d{1,3})?[ -]?\(?\d{1,4}?\)?[ -]?\d{1,4}[ -]?\d{1,4}[ -]?\d{1,9}\b', '[REDACTED PHONE]', anonymized_text)
    
    # Redact addresses (simple example)
    anonymized_text = re.sub(r'\b\d{1,4} [A-Za-z0-9 ]+ St|Ave|Blvd|Road|Rd|Drive|Dr|Court|Ct\b', '[REDACTED ADDRESS]', anonymized_text)
    
    # Redact names using spaCy's NER
    doc = nlp(anonymized_text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            anonymized_text = anonymized_text.replace(ent.text, '[REDACTED NAME]')
    
    return anonymized_text

def main():
    # Example usage:
    resume_text = "Thirumaran Asokan\n Address: 123 Main St, City\n Phone: 0744200\n Email: Thiru.a@example.com"
    anonymized_resume = anonymize_resume(resume_text)
    print("Anonymized Resume:")
    print(anonymized_resume)

if __name__ == "__main__":
    main()
