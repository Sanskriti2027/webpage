from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['name']
    email = request.form['email']
    # Process the form data or perform an action here (Python functionality)
    return f'Hello {name}, your email {email} has been processed!'

if __name__ == '__main__':
    app.run(debug=True)
