import os
from anonymizer import anonymize_resume
from enhanced_bias import detect_bias_with_ai
from enhanced_metrics import plot_metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from bs4 import BeautifulSoup

# Analyze job description for bias and extract keywords
def analyze_job_description(job_description):
    """
    Analyzes the job description for bias and extracts keywords.
    """
    bias_result = detect_bias_with_ai(job_description)
    print(f"Bias Analysis Result: {bias_result}")

    # Simple keyword extraction (can replace with advanced NLP)
    keywords = job_description.split()
    print(f"Extracted Keywords: {keywords}")

    return keywords

# Match resumes to job description using TF-IDF
def match_resumes_with_job(keywords, input_folder):
    """
    Matches resumes to job description keywords and ranks them.
    """
    resumes = []
    resume_names = []

    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_file_path):
            with open(input_file_path, 'r') as file:
                resumes.append(file.read())
                resume_names.append(filename)

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([' '.join(keywords)] + resumes)
    cosine_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Rank resumes by similarity
    ranked_resumes = sorted(zip(resume_names, cosine_scores), key=lambda x: x[1], reverse=True)
    print("Ranked Resumes:")
    for name, score in ranked_resumes:
        print(f"{name}: {score:.2f}")

    return ranked_resumes

# Analyze portfolio or website links
def analyze_portfolio(url):
    """
    Analyzes a candidate's portfolio website for relevant skills and information.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()

        # Example keywords (can extend this list)
        keywords = ['Python', 'Machine Learning', 'Portfolio', 'Experience', 'Project']
        found_keywords = [kw for kw in keywords if kw.lower() in text.lower()]
        return found_keywords
    except Exception as e:
        print(f"Error analyzing portfolio: {e}")
        return []

# Analyze GitHub profiles using the GitHub API
def analyze_github(username):
    """
    Analyzes a candidate's GitHub profile for relevant repositories and activity.
    """
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url)
        repos = response.json()

        # Extract programming languages and repositories
        languages = []
        repo_names = []
        for repo in repos:
            if 'language' in repo and repo['language']:
                languages.append(repo['language'])
            repo_names.append(repo['name'])

        return {"repositories": repo_names[:5], "languages": list(set(languages))}
    except Exception as e:
        print(f"Error analyzing GitHub: {e}")
        return {}

# Process resumes and anonymize shortlisted ones
def process_resumes(input_folder, output_folder, ranked_resumes):
    """
    Processes and anonymizes shortlisted resumes.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename, _ in ranked_resumes:
        input_file_path = os.path.join(input_folder, filename)
        with open(input_file_path, 'r') as file:
            text = file.read()

        # Anonymize the resume
        anonymized_text = anonymize_resume(text)

        # Save anonymized resume
        output_file_path = os.path.join(output_folder, filename)
        with open(output_file_path, 'w') as output_file:
            output_file.write(anonymized_text)

    print("Anonymized shortlisted resumes saved!")

# Main workflow
def main(analyze_links=False):
    # Example job description
    job_description = "Looking for a Python developer with experience in Machine Learning and strong problem-solving skills."

    # Analyze the job description
    keywords = analyze_job_description(job_description)

    # Match resumes
    ranked_resumes = match_resumes_with_job(keywords, "Hiredspros")

    # Optionally analyze portfolio and GitHub links
    if analyze_links:
        for resume, _ in ranked_resumes:
            # Example function to extract links from resume text
            portfolio_links = ["https://example-portfolio.com", "https://github.com/example"]
            for link in portfolio_links:
                if "github.com" in link:
                    github_data = analyze_github("example")  # Replace "example" with username extraction
                    print(f"GitHub Analysis for {resume}: {github_data}")
                else:
                    portfolio_data = analyze_portfolio(link)
                    print(f"Portfolio Analysis for {resume}: {portfolio_data}")

    # Process and anonymize shortlisted resumes
    process_resumes("Hiredspros", "data/output", ranked_resumes)

if _name_ == "_main_":
    # Set analyze_links to True if you want to enable portfolio/GitHub analysis
    main(analyze_links=True)
