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

```HTML
<!DOCTYPE html>
<html>
<head>
    <title>Simply Poetry</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <style>
        textarea {
            width: 500px;
            height: 200px;
            padding: 10px;
            font-size: 16px;
            color: #333;
            border: 1px solid #ccc;
            border-radius: 5px;
            resize: vertical;
        }
        textarea::placeholder {
            color: #aaa;
            font-style: italic;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        #poetryDetails, #liveFeed {
            margin-top: 15px;
            padding: 10px;
            border: 1px solid #ccc;
            background: #f9f9f9;
            width: 520px;
        }
        #liveFeed p {
            border-bottom: 1px solid #ddd;
            padding: 5px 0;
            margin: 0;
        }
    </style>
</head>
<body>
    <h1>Simply Poetry</h1>
    <h2>Select Language and Poetry Form</h2>
    <form>
        <label for="language">Language:</label>
        <select name="language" id="language">
            <option value="">Select Language</option>
            {% for language in languages %}
                <option value="{{ language }}">{{ language }}</option>
            {% endfor %}
        </select>
        <br><br>
        <label for="form">Form:</label>
        <select name="form" id="form">
            <option value="">Select Poetry Form</option>
        </select>
    </form>

    <!-- Display details of the selected poetry form -->
    <div id="poetryDetails"></div>

    <h2>Enter Your Poetry</h2>
    <!-- Change the action to '#' to prevent actual page navigation -->
    <form id="poetryForm" method="POST" action="#">
        <textarea name="text_input" id="text_input" placeholder="Enter your poetry here..."></textarea>
        <br><br>
        <input type="submit" value="Submit">
    </form>

    <h2>Live Preview</h2>
    <div id="liveFeed"></div>

    <script>
        $(document).ready(function() {
            // When language is selected, fetch the available forms
            $('#language').change(function() {
                var selectedLanguage = $(this).val();
                $('#poetryDetails').empty();
                $('#form').empty();
                $('#form').append($('<option></option>').attr('value', '').text('Select Poetry Form'));
                if (selectedLanguage === "") return;
                $.ajax({
                    url: '/get_forms',
                    type: 'GET',
                    data: { language: selectedLanguage },
                    success: function(data) {
                        // 'data' is an object with keys as form names and values as details
                        $.each(data, function(formName, details) {
                            $('#form').append($('<option></option>').attr('value', formName).text(formName));
                        });
                    },
                    error: function() {
                        alert('Error fetching forms');
                    }
                });
            });
    
            // When a poetry form is selected, display its details (syllables and lines)
            $('#form').change(function() {
                var selectedLanguage = $('#language').val();
                var selectedForm = $(this).val();
                if (selectedLanguage === "" || selectedForm === "") {
                    $('#poetryDetails').empty();
                    return;
                }
                // Fetch the form details again
                $.ajax({
                    url: '/get_forms',
                    type: 'GET',
                    data: { language: selectedLanguage },
                    success: function(data) {
                        var details = data[selectedForm];
                        if (details) {
                            var syllables = details.syllables;
                            var lines = details.lines;
                            $('#poetryDetails').html("<strong>Required Syllables:</strong> " + syllables + "<br><strong>Number of Lines:</strong> " + lines);
                        } else {
                            $('#poetryDetails').html("No details available.");
                        }
                    },
                    error: function() {
                        alert('Error fetching form details');
                    }
                });
            });
    
            // Live preview: append submitted text with timestamp to the feed on form submit
            $('#poetryForm').on('submit', function(e) {
                e.preventDefault(); // Prevent actual form submission
                var text = $('#text_input').val().trim();
                if (text !== "") {
                    var timestamp = new Date().toLocaleString(); // Get current timestamp
                    // Append the new text with timestamp as a paragraph to the live feed
                    $('#liveFeed').append("<p><strong>[" + timestamp + "]</strong> " + text + "</p>");
                    // Clear the textarea
                    $('#text_input').val("");
                }
            });
        });
    </script>
</body>
</html>

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

A major thanks to Jonathan Tuan Tran and Sahil Gupta for initiating this project!

## License

Creative Commons

[The Unlicense] (https://choosealicense.com/licenses/unlicense/)
