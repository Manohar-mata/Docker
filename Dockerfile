FROM python:3.9-slim

WORKDIR /app

# Install numpy first to avoid compatibility issues
RUN pip install --no-cache-dir numpy

# Copy all files from the current directory to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
