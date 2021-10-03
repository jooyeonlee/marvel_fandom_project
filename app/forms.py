from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms import validators
from wtforms.validators import DataRequired, Email, EqualTo

class CharacterSearchForm(FlaskForm):
    search = StringField('Search')

class SignInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

class SignUpForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit_button = SubmitField()

class NewCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description')
    comics = StringField('Comics')
    superpower = StringField('Super Power')
    submit_button = SubmitField()

class EditUserForm(FlaskForm):
    new_name = StringField('New Name')
    newpassword = PasswordField('New Password')
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('newpassword')])
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    submit_button = SubmitField()