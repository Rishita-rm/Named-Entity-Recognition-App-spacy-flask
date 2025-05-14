FROM python:3.11-slim

WORKDIR /app

# Install required OS packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy app files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ✅ Pre-download spaCy models to avoid runtime delays
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download xx_ent_wiki_sm

# Set environment port
ENV PORT 8080

# Run with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
