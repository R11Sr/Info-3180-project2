# Add any form classes for Flask-WTF here
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Email
import email_validator

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    fullname = StringField('Fullname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    biography = TextAreaField("Biography",validators=[DataRequired()])
    photo = FileField('Upload Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'])])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class AddNewCarForm(FlaskForm):
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    color = StringField('Colour', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    Car_Type = SelectField("Car Type", choices=['SUV','COUP','HATCH BACK','SEDAN','STATION WAGON'])
    transmission = SelectField('Transmission', choices=['MANUAL','AUTOMATIC'])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Upload Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'])])