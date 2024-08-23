# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8080 to the outside world (optional, if your app needs it)
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run the application
CMD ["python", "scripts/train_stylegan2.py"]
