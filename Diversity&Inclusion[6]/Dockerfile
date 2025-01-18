# Use Python as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for frontend integration (optional for future)
EXPOSE 5000

# Command to run the backend script
CMD ["python", "backend.py"]
