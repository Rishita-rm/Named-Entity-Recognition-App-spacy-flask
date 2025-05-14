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

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PORT 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
