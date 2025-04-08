from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dropdown_options = ['Option 1', 'Option 2', 'Option 3']
    selected_option = None
    text_input = None

    if request.method == 'POST':
        selected_option = request.form.get('dropdown')
        text_input = request.form.get('text_input')
        # Process the selected option and text input as needed
        print(f"Selected option: {selected_option}, Text input: {text_input}")

    return render_template('index.html',
                           dropdown_options=dropdown_options,
                           selected_option=selected_option,
                           text_input=text_input)

if __name__ == '__main__':
    app.run(debug=True)