import os
from anonymizer import anonymize_resume

def process_resumes(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        with open(os.path.join(input_folder, filename), 'r') as file:
            text = file.read()

        anonymized_text = anonymize_resume(text)

        with open(os.path.join(output_folder, filename), 'w') as output_file:
            output_file.write(anonymized_text)

if __name__ == "__main__":
    process_resumes("data/sample_resumes", "data/output")
