# Stage 1: Base build stage
FROM python:3.13-slim AS builder
 
# Create the app directory
RUN mkdir /app
 
# Set the working directory
WORKDIR /app
 
# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
# Install dependencies first for caching benefit
RUN pip install --upgrade pip 
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY  . .
EXPOSE 8000 

# Make entry file executable
RUN chmod +x  /app/docker-entrypoint.sh
 
# Start the application using Gunicorn
CMD ["/app/docker-entrypoint.sh"]