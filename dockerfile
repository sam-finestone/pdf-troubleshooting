# # Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Install Nginx
# RUN apt-get update && apt-get install -y nginx

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Copy the templates directory
# COPY ./templates /app/templates

# # Copy Nginx configuration file
# COPY nginx.conf /etc/nginx/sites-available/default

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Install Gunicorn
# RUN pip install gunicorn

# # Make port 5000 available to the world outside this container
# EXPOSE 80

# # Define environment variable
# ENV FLASK_APP=run.py

# # Run run.py when the container launches
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]

# Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Install system dependencies
# RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# # Set the working directory in the container
# WORKDIR /app

# # Install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install gunicorn

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Copy the Nginx configuration file
# COPY nginx.conf /etc/nginx/sites-available/default

# # Link Nginx config
# RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
# RUN rm /etc/nginx/sites-enabled/default

# # Expose port 80 to the outside world
# EXPOSE 80

# # Set environment variables
# ENV FLASK_APP=run.py

# # Start Gunicorn and use the flask application factory
# CMD ["gunicorn", "--config", "gunicorn_config.py", "run:app"]

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the templates directory
COPY ./templates /app/templates

# Copy Nginx configuration file
COPY nginx.conf /etc/nginx/sites-available/default

# Create the symlink if it does not exist
RUN if [ ! -e /etc/nginx/sites-enabled/default ]; then ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled; fi

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Make port 80 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV FLASK_APP=run.py

# Start Nginx and Gunicorn
CMD service nginx start && gunicorn -w 4 -b 0.0.0.0:5001 "app:create_app()"
# CMD ["sh", "-c", "service nginx start && gunicorn -w 4 -b 127.0.0.1:5000 app:create_app()"]

