from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SelectField, PasswordField
from wtforms.validators import DataRequired


class ChoiceForm(FlaskForm):
    choice1 = StringField('choice1', validators=[DataRequired()])
    choice2 = StringField('choice2', validators=[DataRequired()])


class AuthForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])