# Use Python 3.9 with Debian Buster base image
FROM python:3.9-buster

# Set the working directory in the container
WORKDIR /app

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgomp1 \
    gcc \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip to avoid outdated notices and add retries for robustness
RUN pip install --upgrade pip && \
    pip install --retries 10 --timeout 300 --no-cache-dir setuptools

# Copy requirements.txt to the container
COPY requirements.txt /app/

# Install Python dependencies with retries to avoid timeout errors
RUN pip install --retries 10 --timeout 300 --no-cache-dir -r requirements.txt

# Download and install the Spacy language model
RUN python -m spacy download en_core_web_sm

# Copy the rest of the project files to the container
COPY . /app

# Expose port 5000 (optional)
EXPOSE 5000

# Command to run the backend script
CMD ["python", "backend.py"]