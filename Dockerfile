FROM python:3.10-slim

# Install system dependencies
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    ffmpeg \
    aria2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (optional but clean practice)
EXPOSE 10000

# Start web server file
CMD ["gunicorn", "-b", "0.0.0.0:$PORT", "web:app"]
