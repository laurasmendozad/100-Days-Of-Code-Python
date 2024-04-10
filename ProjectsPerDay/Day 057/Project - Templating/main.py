from flask import Flask, render_template
import requests

app = Flask(__name__)
all_posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for post in all_posts:
        if post['id'] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
