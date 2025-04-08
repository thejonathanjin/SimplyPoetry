from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    options = ['English', 'Chinese', 'Japanese', 'Indian', 'Vietnamese']
    selected_option = None
    if request.method == 'POST':
        selected_option = request.form['my_dropdown']

    return render_template('index.html', options=options, selected_option=selected_option)


if __name__ == '__main__':
    app.run(debug=True)