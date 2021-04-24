from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email, InputRequired, NumberRange, ValidationError
from email_validator import validate_email
from cyclofit.models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email',
                validators=[InputRequired("Please enter your email address."), 
                Email("Enter valid email address")])
    username = StringField('Username', 
                validators=[DataRequired(), 
                Length(min=2, max=20)])
    password = PasswordField('Password',
                validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                validators=[DataRequired(), 
                EqualTo('password')])
    submit = SubmitField('Register')

    # custom validations 
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        # query if the entered username is present in the db
        # if username already present throw validation error
        if user:
            raise ValidationError('Username already taken! Pick another!')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        # query if the entered email is present in the db
        # if email already present throw validation error
        if user:
            raise ValidationError('Email already taken! Pick another!')

class ProfileForm(FlaskForm):
    area = StringField('Area', 
                validators=[DataRequired(), 
                Length(min=2, max=20)])
    contactno = IntegerField('Contact Number', validators=[NumberRange(min=10), DataRequired('Enter valid number with no symbols')])
    dob = StringField('Date of Birth',
                validators=[DataRequired(), Length(min=7)])
    emergencyno = IntegerField('Emergency Number', validators=[NumberRange(min=10), DataRequired('Enter valid number with no symbols')])
    submit = SubmitField('GO')

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')