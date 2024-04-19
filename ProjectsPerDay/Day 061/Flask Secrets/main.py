import os
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = os.urandom(12).hex()
print(app.secret_key)

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(),
                                                           Length(min=8, 
                                                                  message='Field must be at least 8 characters long.')])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return redirect(url_for('loginSuccess'))
        else:
            return redirect(url_for('loginDenied'))
        
            
    return render_template('login.html', form=login_form)


@app.route("/loginSuccess")
def loginSuccess():
    return render_template('success.html')

@app.route("/loginDenied")
def loginDenied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
