from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, PreferencesForm
from news import news
import flask_datepicker
# from news import News
app = Flask(__name__)
app.config['SECRET_KEY'] = 'eea48b1de28faa679e0c9551182d7882'

@app.route('/')
@app.route('/home')

def home():
    newsimport = news()
    return render_template('home.html', news = newsimport)

@app.route('/login', methods=['GET',])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@a.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('preferences'))
        else:
            flash('Login Unsuccessful. Please check email/password.', 'danger')
    return render_template('login.html', title="Login", form=form)

@app.route('/preferences', methods=['GET','POST'])
def preferences():
    form = PreferencesForm()
    if form.validate_on_submit():
        flash('Your changes have been made!', 'success')
        return redirect(url_for('home'))
    return render_template('preferences.html', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created {form.username.data}!', 'success')
        return redirect(url_for('preferences'))
    # else:
    #     flash(f'BRUH WTF')
    #     redirect(url_for('register'))
    return render_template('register.html', form = form, title="Register")
if __name__ == '__main__':
    app.run(debug=True)

