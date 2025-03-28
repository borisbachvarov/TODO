# Use an official Python runtime as the base image
FROM python:3.12-slim-bookworm

# Set the working directory inside the container
WORKDIR /app/todolist

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app
# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8011"]