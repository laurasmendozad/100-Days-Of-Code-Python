from random import randint
from datetime import datetime
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = randint(1,10)
    current_year = datetime.now().year
    my_name = "Laura Mendoza"
    return render_template('index.html', num=random_number, year=current_year, name=my_name)

@app.route('/guess/<name>')
def guess(name):
    response_genderize = requests.get(f'https://api.genderize.io?name={name}')
    gender = response_genderize.json()['gender']
    response_agify = requests.get(f'https://api.agify.io?name={name}')
    age = response_agify.json()['age']
    return render_template('guess.html', some_name=name, gender=gender, age=age)

@app.route('/blog')
def blog():
    response_fakeblogs = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    all_posts = response_fakeblogs.json()
    return render_template('blog.html', posts=all_posts)

if __name__=="__main__":
    app.run(debug=True)
    