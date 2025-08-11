# SimplyPoetry

SimplyPoetry is a Python Web App for writing your own and submitting poetry, so far, locally to a development server.

The end goal is to create a Web Server that will collect all submissions from users so that users can share their creative work.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the Flask web framework.

```bash
pip install Flask
```

File & Folder Path:

```
.
├── app.py
├── __init__.py
├── poetry_forms.py
├── __pycache__
│   └── poetry_forms.cpython-312.pyc
└── templates
    └── index.html
```

## Usage

app.py

```python
from flask import Flask, render_template, request, jsonify
from poetry_forms import poetry_forms as language_poem_form

app = Flask(__name__)

@app.route('/')
def index():
    languages = list(language_poem_form.keys())
    return render_template('index.html', languages=languages)

@app.route('/get_forms')
def get_forms():
    selected_language = request.args.get('language')
    forms = language_poem_form.get(selected_language, {})
    return jsonify(forms)

@app.route('/index', methods=['GET', 'POST'])
def text_box():
    submitted_text = None
    if request.method == 'POST':
        submitted_text = request.form['text_input']
    languages = list(language_poem_form.keys())
    return render_template('index.html', languages=languages, submitted_text=submitted_text)

if __name__ == '__main__':
    app.run(debug=True)
```

poetry_forms.py
```python
poetry_forms = {
    "English": {
        "Haiku": {"syllables": [5, 7, 5], "lines": 3},
        "Sonnet": {"syllables": [10] * 14, "lines": 14},  # Iambic pentameter, 10 syllables per line
        "Limerick": {"syllables": [8, 8, 5, 5, 8], "lines": 5}
    },
    "Chinese": {
        "Jueju": {"syllables": [5, 5, 7, 7], "lines": 4},  # 5 or 7 syllables, regulated tone
        "Lüshi": {"syllables": [5] * 8, "lines": 8},      # 5 or 7 syllables, strict parallelism
        "Ci": {"syllables": "variable", "lines": "variable"}  # Depends on tune pattern
    },
    "Japanese": {
        "Haiku": {"syllables": [5, 7, 5], "lines": 3},
        "Tanka": {"syllables": [5, 7, 5, 7, 7], "lines": 5},
        "Senryu": {"syllables": [5, 7, 5], "lines": 3}
    },
    "Indian": {  # Sanskrit and regional traditions
        "Shloka": {"syllables": [8, 8], "lines": 2},  # Typically 8 syllables per half-line, epic form
        "Ghazal": {"syllables": "variable", "lines": 10},  # Urdu influence, 5+ couplets
        "Doha": {"syllables": [13, 11], "lines": 2}  # Hindi/Prakrit, syllable split per line
    },
    "Vietnamese": {
        "Luc Bat": {"syllables": [6, 8] * 3, "lines": 6},  # Alternating 6 and 8, extensible
        "Song That": {"syllables": [7] * 4, "lines": 4},  # 7 syllables, folk style
        "Cach Dieu": {"syllables": "variable", "lines": 4}  # Regulated, varies by tone
    }
}
```

<iframe src="https://giphy.com/embed/uQhr9Y6c8DJAbiSAOq" width="480" height="269" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/uQhr9Y6c8DJAbiSAOq">via GIPHY</a></p>

<iframe src="https://giphy.com/embed/IHWGDeTEFKuRpIJRMK" width="480" height="274" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/IHWGDeTEFKuRpIJRMK">via GIPHY</a></p>

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

A major thanks to Jonathan Tuan Tran and Sahil Gupta for initiating this project!

## License

Creative Commons

[The Unlicense] (https://choosealicense.com/licenses/unlicense/)
p
