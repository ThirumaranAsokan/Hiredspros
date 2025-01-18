import re

# List of biased terms and their neutral alternatives
BIAS_TERMS = {
    "aggressive": "assertive",
    "dominant": "confident",
    "nurturing": "supportive",
    "rockstar": "expert",
    "guru": "specialist",
}

def detect_bias(text):
    """
    Detects biased terms in the provided text.

    Args:
    - text (str): The job description or input text.

    Returns:
    - dict: A dictionary of biased terms and their suggested alternatives.
    """
    found_bias = {}
    for term, alternative in BIAS_TERMS.items():
        if re.search(rf"\b{term}\b", text, re.IGNORECASE):
            found_bias[term] = alternative
    return found_bias

def suggest_replacement(text):
    """
    Replaces biased terms with neutral alternatives.

    Args:
    - text (str): The job description or input text.

    Returns:
    - str: Text with biased terms replaced by neutral alternatives.
    """
    for term, alternative in BIAS_TERMS.items():
        text = re.sub(rf"\b{term}\b", alternative, text, flags=re.IGNORECASE)
    return text

def main():
    job_description = "We are looking for a rockstar developer with an aggressive mindset."
    biased_terms = detect_bias(job_description)
    corrected_text = suggest_replacement(job_description)
    print("Biased Terms Found:", biased_terms)
    print("Corrected Job Description:", corrected_text)

if __name__ == "__main__":
    main()
