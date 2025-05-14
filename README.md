![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.2-lightgrey.svg)
![spaCy](https://img.shields.io/badge/spaCy-3.5-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Deployed](https://img.shields.io/badge/deployed-Railway-success?logo=railway)

# 🧠 Named Entity Recognition App (Flask + spaCy)

A full-stack NLP web app for Named Entity Recognition (NER) using [spaCy](https://spacy.io/) and [Flask](https://flask.palletsprojects.com/). This app allows users to input text or upload `.txt` files, choose specific entity types, and visualize named entities interactively. Supports multiple languages and includes a REST API for integration.

![NER Demo](https://user-images.githubusercontent.com/your-demo.gif)

---

## 📌 Features

- ✅ Upload or paste plain text for processing  
- ✅ Supports multiple spaCy models (English, multilingual)  
- ✅ Filter entities by type (e.g., PERSON, ORG, GPE)  
- ✅ Interactive entity visualization via `displacy`  
- ✅ Entity statistics chart with `matplotlib`  
- ✅ REST API (`/api/entity`) for programmatic access  
- ✅ Deployed via Docker and Railway  

---

## 🚀 Live Demo

> 🔗 **[View the app live](https://named-entity-recognition-app-spacy-flask-production.up.railway.app/))**  

---

## 🧰 Tech Stack

| Layer       | Technology                    |
|-------------|-------------------------------|
| Backend     | Python, Flask, spaCy          |
| Frontend    | HTML, Bootstrap (Jinja2)      |
| Visualization | spaCy `displacy`, Matplotlib |
| API         | Flask REST endpoint (`/api/entity`) |
| Deployment  | Docker, Railway               |

---

## 🛠️ Local Installation

```bash
# Clone the repo
git clone https://github.com/your-username/named-entity-recognition-app.git
cd named-entity-recognition-app

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
Then open: http://localhost:8080
```
---

## 📦 Docker Deployment
```bash
Copy
Edit
# Build Docker image
docker build -t ner-app .

# Run the container
docker run -p 8080:8080 ner-app
```
---

## 🧪 REST API
Use the /api/entity endpoint for programmatic access.

### POST /api/entity
**Request Body** (JSON):
``` json
{
  "text": "Apple was founded by Steve Jobs in California.",
  "model": "en_core_web_sm"
}
```
### Response Example:
``` json
{
  "entities": [
    {"text": "Apple", "label": "ORG", "start_char": 0, "end_char": 5},
    {"text": "Steve Jobs", "label": "PERSON", "start_char": 21, "end_char": 31},
    {"text": "California", "label": "GPE", "start_char": 35, "end_char": 45}
  ]
}
```
---

## 📁 Project Structure
``` bash

├── app.py               # Flask backend
├── templates/
│   └── index.html       # Frontend interface
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker setup
└── README.md            # Project documentation
```
---

## ✨ Future Enhancements
- Add more spaCy models (e.g., transformer-based)
- Export annotated text (JSON/CSV)
- User accounts and session history
- Model performance comparison dashboard

---

## 👤 Author
**Rishita Makkar**
🔗 [LinkedIn](https://www.linkedin.com/in/rishita-makkar-256851291/)  
💻 [GitHub](https://github.com/Rishita-rm)

---

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## ⭐️ Show Your Support
If you found this project useful:

- ⭐️ Star the repo
- 🍴 Fork and contribute
- 📢 Share with others

