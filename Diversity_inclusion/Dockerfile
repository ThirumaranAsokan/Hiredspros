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

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /app

# Debug: List files to confirm everything is copied
RUN ls -la /app

# Expose port 5000 (future use)
EXPOSE 5000

# Command to run the backend script
CMD ["python", "backend.py"]
