
from datetime import datetime
from random import randint
from flask import Flask, render_template
import requests

app = Flask(__name__)

all_posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7", timeout=3600).json()
for p in all_posts:
    p['date'] = datetime(year=2024, month=4-p['id'], day= randint(1,31))

@app.route('/')
def home():
    header_title = 'Home'
    return render_template('index.html', title=header_title, posts = all_posts)

@app.route('/about')
def about():
    header_title = "About"
    return render_template("about.html", title=header_title)

@app.route('/contact')
def contact():
    header_title = "Contact"
    return render_template("contact.html", title=header_title)

@app.route('/post/<int:index>')
def post(index):
    header_title = "Post"
    requested_post = None
    for post in all_posts:
        if post['id'] == index:
            requested_post = post
    return render_template("post.html", title=header_title, post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
