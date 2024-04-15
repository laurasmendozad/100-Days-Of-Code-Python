
from datetime import datetime
from random import randint
import os
import smtplib
from flask import Flask, render_template, request
import requests

def send_email(subject, message):
    ''' Send the email '''
    email = "laurasofi0507@gmail.com"
    password = os.environ.get("GMAIL_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="laurasofi0507@hotmail.com",
            msg=f"Subject:{subject}\n\n{message}"
        )

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

@app.route('/contact', methods=["GET","POST"])
def contact():
    header_title = "Contact"
    if request.method == "POST":
        data = request.form
        send_email("New Blog Message", f'Name: {data["name"]} \nEmail: {data["email"]} \nPhone: {data["phone"]} \nMessage: {data["message"]}')
        return render_template("contact.html", title=header_title, msg_sent=True)
    return render_template("contact.html", title=header_title, msg_sent=False)

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
