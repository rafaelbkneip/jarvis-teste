from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

#Templates em HTML
app = Flask(__name__, template_folder='templates')

app.app_context().push()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        info = (request.form['size'])
        return f"{info}"
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
