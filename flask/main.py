from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, ' + name + '!</h1>'


@app.route('/mine')
def mine():
    return render_template('mypage.html')


@app.route('/mine/<name>')
def mine2(name):
    return render_template('mypage2.html', name=name)

@app.route('/freediving')
def freediving():
    return render_template('freediving.html')

app.run()
