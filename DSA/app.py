from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input from the HTML form
        names = request.form.get('names')

        # Split the input into a list of names
        names_list = names.split(',')

        # Sort the names
        sorted_names = sorted(names_list)

        # Join the sorted names back into a string
        sorted_names_str = ', '.join(sorted_names)

        # Pass the sorted names to the template for rendering
        return render_template('result.html', sorted_names=sorted_names_str)

    # If it's a GET request or the form is not submitted yet, render the form
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
