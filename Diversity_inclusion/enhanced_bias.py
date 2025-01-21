from transformers import pipeline  # type: ignore
import spacy  # type: ignore

# Load pre-trained model for bias detection from Hugging Face
bias_detector = pipeline("text-classification", model="unitary/toxic-bert")

# Load SpaCy's model for semantic analysis
nlp = spacy.load("en_core_web_sm")

# Expanded dictionary of biased terms
BIAS_DICTIONARY = {
    "gendered": {
        "terms": [
            "manpower", "chairman", "salesman", "he/him", "guys", "waitress", "fireman", "businessman"
        ],
        "suggestions": [
            "workforce", "chairperson", "salesperson", "they/them", "everyone", "server", "firefighter", "businessperson"
        ]
    },
    "aggressive": {
        "terms": [
            "rockstar", "ninja", "killer", "dominate", "alpha", "aggressive", "smash", "warrior"
        ],
        "suggestions": [
            "expert", "skilled professional", "accomplished", "lead", "collaborative", "problem-solver", "champion"
        ]
    },
    "age-related": {
        "terms": [
            "young", "energetic", "recent graduate", "digital native", "junior", "fresh out of college"
        ],
        "suggestions": [
            "motivated", "enthusiastic", "qualified", "experienced", "early career", "new professional"
        ]
    },
    "ethnic": {
        "terms": [
            "oriental", "colored", "minority", "ghetto", "tribal", "caucasian", "latino", "hispanic", "black"
        ],
        "suggestions": [
            "diverse", "global", "international", "people of color", "ethnically diverse", "inclusive", "multicultural"
        ]
    },
    "disability": {
        "terms": [
            "handicapped", "crippled", "wheelchair-bound", "invalid", "suffering", "autistic", "mentally challenged"
        ],
        "suggestions": [
            "person with a disability", "differently-abled", "person using a wheelchair", "person with autism", "neurodiverse"
        ]
    }
}

# Simple dictionary-based bias detection
def detect_bias_with_dictionary(text):
    flagged_terms = []
    for category, details in BIAS_DICTIONARY.items():
        for term, suggestion in zip(details["terms"], details["suggestions"]):
            if term.lower() in text.lower():
                flagged_terms.append(term)
    return flagged_terms

# Use Hugging Face's model for AI-based detection
def detect_bias_with_ai(text):
    result = bias_detector(text)
    if result[0]['label'] == 'LABEL_1':  # Toxic label detected
        return "Potential Bias Detected!"
    else:
        return "No Bias Detected"

# Combining both methods: Dictionary + AI-based detection
def analyze_bias(text):
    dictionary_results = detect_bias_with_dictionary(text)
    ai_results = detect_bias_with_ai(text)
    
    # Additional semantic analysis using SpaCy
    doc = nlp(text)
    for token in doc:
        if token.pos_ in ['NOUN', 'ADJ'] and token.text.lower() not in dictionary_results:
            # Check semantic similarity with bias terms in the dictionary
            for category, details in BIAS_DICTIONARY.items():
                for term in details["terms"]:
                    similarity = nlp(term).similarity(token)
                    if similarity > 0.75:  # Threshold for semantic similarity
                        dictionary_results.append(token.text)
    
    return {
        "dictionary_results": dictionary_results,
        "ai_results": ai_results
    }