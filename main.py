from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return "<h1>Моя сторінка на Flask</h1>"
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/about')
def about():
    return "<h2>Тaнк 2 світової війни</h2><p> т-34 рубив Тігрів як дрова</p>"


# only local
if __name__ == '__main__':
    app.run(debug=True)
