from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, DateField
from wtforms.validators import InputRequired, Email, Length, ValidationError, DataRequired, EqualTo
from app.models import User, Circle

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=12)])
    submit = SubmitField('Log In')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('Username doesn\'t exist')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    college = StringField('College',validators=[InputRequired()])
    gender = RadioField('Gender',validators=[InputRequired()],choices=[('1','Male'),('2','Female')])
    dob = DateField('Date of Birth')
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=12)])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class CreateCircleForm(FlaskForm):
    circlecode = StringField('Circle code',validators=[DataRequired()])
    title = StringField('Title',validators=[DataRequired(),Length(max=50)])
    description = TextAreaField('Description',validators=[DataRequired()])
    submit = SubmitField('Create Circle')

    def validate_circlecode(self,circlecode):
        if not circlecode.data.isalnum():
            raise ValidationError('Only use english alphabet and numbers')

        circle = Circle.query.filter_by(code=circlecode.data).first()
        if circle is not None:
            raise ValidationError('Circle with this code already exists')

