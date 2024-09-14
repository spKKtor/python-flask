from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# 1.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2.
db = SQLAlchemy(app)


# 3.
class User(db.Model):
    __tablename_ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"<user {self.username}"


# 4.
with app.app_context():
    db.create_all()


@app.route('/')
@app.route('/user/<name>')
def index(name=''):
    return render_template('index.html', name=name)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/articles')
def articles():
    new_articles = ['How to avoid expensive travel mistakes', 'Top 5 places to experience supernatural forces',
                    'Three wonderfully bizarre Mexican festivals', 'The 20 greenest destinations on Earth',
                    'How to survive on a desert island']

    return render_template('articles.html', articles=new_articles)


@app.route('/details')
def details():
    return render_template('details.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


#
if __name__ == '__main__':
    app.run(debug=True)