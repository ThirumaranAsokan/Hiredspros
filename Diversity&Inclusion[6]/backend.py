import os
from anonymizer import anonymize_resume
from enhanced_bias import detect_bias
from enhanced_metrics import generate_mock_data, plot_metrics, predict_diversity_trends

def process_resumes(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)

        if not os.path.isfile(input_file_path):
            continue

        with open(input_file_path, 'r') as file:
            text = file.read()

        anonymized_text = anonymize_resume(text)

        output_file_path = os.path.join(output_folder, filename)
        with open(output_file_path, 'w') as output_file:
            output_file.write(anonymized_text)
    print("Resumes processed and anonymized successfully!")

def analyze_job_description(job_description):
    result = detect_bias(job_description)
    print(f"Bias Analysis Result: {result}")

def visualize_metrics():
    metrics_data = generate_mock_data()
    plot_metrics(metrics_data)
    predict_diversity_trends(metrics_data["Gender"])

if _name_ == "_main_":
    process_resumes("Hiredspros", "data/output")
    job_description = "We are looking for a data who thrives under pressure and is motivated."
    analyze_job_description(job_description)
    visualize_metrics()
