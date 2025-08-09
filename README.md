# SimplyPoetry

SimplyPoetry is a Python Web App for writing your own and submitting poetry, so far, locally to a development server.

The end goal is to create a Web Server that will collect all submissions from users so that users can share their creative work.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the Flask web framework.

```bash
pip install Flask
```

## Usage

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

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Creative Commons

[The Unlicense] (https://choosealicense.com/licenses/unlicense/)
