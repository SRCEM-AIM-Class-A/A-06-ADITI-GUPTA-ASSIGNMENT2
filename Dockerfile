# Use Python base image
FROM python:3.8

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Install dependencies
#RUN pip install django

# Expose the port
EXPOSE 8000

# Ensure the correct working directory
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
