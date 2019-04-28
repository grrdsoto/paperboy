from flask import Flask, render_template, url_for, flash, redirect, session
from forms import RegistrationForm, LoginForm, PreferencesForm
from news import news
from flask_session import Session
import flask_datepicker
# from news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eea48b1de28faa679e0c9551182d7882'
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
sess.init_app(app)


@app.route('/')
@app.route('/home')
def home():
    articles = session.get('articles', 'Nothing to show')
    print(articles)
    return render_template('home.html', news = articles)

@app.route('/login', methods=['GET', 'POST'])
def login():
# from news import news
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
        newsobj = news()
        newsobj.update(form.query.data, form.time.data, form.sortBy.data)
        session['articles']= newsobj.articles
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

