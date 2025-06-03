# Stage 1: Base build stage
FROM python:3.13-slim AS builder

# Create the app directory
RUN mkdir /app
WORKDIR /app

# Optimize Python behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Install dependencies
RUN apt-get update && \
    apt-get install -y bash dos2unix && \
    pip install --upgrade pip

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Fix Windows line endings; remove this when deploy in linus system
#RUN dos2unix /app/entrypoint.sh

COPY app/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Expose port
EXPOSE 8000

# Run the entrypoint script
CMD ["entrypoint.sh"]