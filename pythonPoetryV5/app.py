from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data (replace with database or external source in real applications)
language_poem_form = {
    'English': ['Sonnet', 'Limerick', 'Haiku'],
    'Chinese': ['Jueju', 'Lüshi', 'Ci'],
    'Japanese': ['Haiku', 'Tanka', 'Senryu'],
    'Indian': ['Shloka', 'Ghazal', 'Doha'],
    'Vietnamese': ['Luc Bat', 'Song That', 'Cach Dieu']
}

@app.route('/')
def index():
    languages = list(language_poem_form.keys())
    return render_template('index.html', languages=languages)

@app.route('/get_forms')
def get_forms():
    selected_language = request.args.get('language')
    forms = language_poem_form.get(selected_language, [])
    return jsonify(forms)

@app.route('/index', methods=['GET', 'POST'])
def text_box():
    submitted_text = None
    if request.method == 'POST':
        submitted_text = request.form['text_input']
    return render_template('index.html', submitted_text=submitted_text)

if __name__ == '__main__':
    app.run(debug=True)