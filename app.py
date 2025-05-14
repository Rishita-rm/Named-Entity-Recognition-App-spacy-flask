from flask import Flask, request, render_template, jsonify
import spacy
from spacy import displacy
from collections import Counter
import matplotlib.pyplot as plt
import os
import io
import base64

app = Flask(__name__)

# ✅ Lazy-loaded model cache
LOADED_MODELS = {}

# ✅ Load or download model on demand
def get_model(name):
    if name not in LOADED_MODELS:
        try:
            LOADED_MODELS[name] = spacy.load(name)
        except OSError:
            os.system(f"python -m spacy download {name}")
            LOADED_MODELS[name] = spacy.load(name)
    return LOADED_MODELS[name]

# ✅ Just list names (don't preload)
MODEL_NAMES = ['en_core_web_sm', 'xx_ent_wiki_sm']

@app.route('/')
def index():
    return render_template('index.html', models=MODEL_NAMES)

@app.route('/entity', methods=['POST'])
def entity():
    selected_model = request.form.get('model', 'en_core_web_sm')
    entity_types = request.form.getlist('entity_type')
    text = ""

    if 'text' in request.form and request.form['text'].strip():
        text = request.form['text']
    elif 'file' in request.files:
        file = request.files['file']
        if file:
            text = file.read().decode('utf-8', errors='ignore')

    if not text:
        return render_template('index.html', error="No text provided.", models=MODEL_NAMES)

    nlp = get_model(selected_model)
    doc = nlp(text)

    if entity_types:
        ents = [ent for ent in doc.ents if ent.label_ in entity_types]
        doc.ents = ents

    html = displacy.render(doc, style='ent', jupyter=False)

    labels = [ent.label_ for ent in doc.ents]
    counter = Counter(labels)
    chart = plot_entity_distribution(counter)

    return render_template('index.html', html=html, text=text, models=MODEL_NAMES, chart=chart)

def plot_entity_distribution(counter):
    if not counter:
        return None
    fig, ax = plt.subplots()
    ax.bar(counter.keys(), counter.values())
    ax.set_title("Entity Type Frequency")
    ax.set_ylabel("Count")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    img_data = base64.b64encode(buf.read()).decode('utf-8')
    return f"data:image/png;base64,{img_data}"

@app.route('/api/entity', methods=['POST'])
def api_entity():
    data = request.get_json()
    text = data.get('text', '')
    model_name = data.get('model', 'en_core_web_sm')
    if model_name not in MODEL_NAMES:
        return jsonify({"error": "Model not supported"}), 400

    nlp = get_model(model_name)
    doc = nlp(text)

    entities = [{
        "text": ent.text,
        "label": ent.label_,
        "start_char": ent.start_char,
        "end_char": ent.end_char
    } for ent in doc.ents]

    return jsonify({"entities": entities})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
