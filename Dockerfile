# Use official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create 'data' directory if it doesn't exist
RUN mkdir -p data

# Expose port 80
EXPOSE 80

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
