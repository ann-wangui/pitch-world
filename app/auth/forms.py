from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, ValidationError, BooleanField,TextAreaField
from wtforms.validators import InputRequired,Email,EqualTo

class RegistrationForm(FlaskForm):
    email = StringField('Enter Your Email Address')
    username = StringField('Enter Your username')
    password = PasswordField('Input password')
    password_confirm = PasswordField('Kindly confirm password')
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField ('Enter Your Email Address')
    password = PasswordField('Input Password')
    remember = BooleanField('Save password')
    submit = SubmitField('Sign In')