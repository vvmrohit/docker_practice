# Use the official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the Python dependencies file and install them
COPY requirements.txt .

# Install Flask and other dependencies
RUN pip install -r requirements.txt

# Copy the entire contents of the 'script' folder to the container's working directory
COPY app/. .

# Expose port 5000 to allow external access
EXPOSE 5050

# Command to run the Flask application
CMD ["python", "server.py"]
