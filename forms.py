from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField



class RegistrationForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm): 
    email = StringField('Email', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PreferencesForm(FlaskForm):
    query = StringField('Topic', validators=[DataRequired()])
    time = DateField('Start Date', format='%Y-%m-%d')
    sortBy = SelectField('Sort By', validators=[DataRequired()], choices=[('relevancy', 'Relevancy'), ('popularity', 'Popularity'), ('publishedAt', "Published At")])
    submit = SubmitField('Submit')