from transformers import pipeline
from textblob import TextBlob

# Load pre-trained model for bias detection
bias_detector = pipeline("text-classification", model="unitary/toxic-bert")

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the job description using TextBlob.
    """
    analysis = TextBlob(text)
    return "Negative" if analysis.sentiment.polarity < 0 else "Positive"

def detect_bias_with_ai(text):
    """
    Detects biased or toxic language in the job description using a pre-trained AI model.
    """
    result = bias_detector(text)
    if result[0]['label'] == 'LABEL_1':  # Toxic label detected
        return "Potential Bias Detected!"
    else:
        return "No Bias Detected"

def main():
    job_description = "We are looking for a python developer with an aggressive mindset."
    print("Sentiment Analysis:", analyze_sentiment(job_description))
    print("Bias Detection Result:", detect_bias_with_ai(job_description))

if _name_ == "_main_":
    main()