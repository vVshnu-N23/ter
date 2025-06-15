# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]