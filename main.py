from flask import Flask
from flask import render_template
from flask import abort

app = Flask(__name__)

@app.route('/')
def main():
    abort(426)
    return '<h1>Hello world!</h1>'

@app.route('/test')
def test_page():
    return my_site

if __name__ == '__main__':
    app.run(debug = True)

