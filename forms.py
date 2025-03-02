from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.fields import (
    StringField, PasswordField, IntegerField, SubmitField,
    DateField, SelectField, RadioField, BooleanField
)

from wtforms.validators import DataRequired, Length, ValidationError, equal_to
from string import punctuation, digits



class ProductForm(FlaskForm):
    name = StringField("Enter product name", validators=[DataRequired(), Length(min=2, max=32)])
    title = StringField("Enter product title")
    platform = SelectField("platform", choices=["Playstation", "Xbox", "Other"], validators=[DataRequired()])
    condition = RadioField("Condition", choices=["New", "Second-hand", "Repaired"], validators=[DataRequired()])
    price = IntegerField("Enter product price", validators=[DataRequired()])
    date = DateField("Enter product date:", validators=[DataRequired()])
    category = SelectField("Category", choices=["Console", "Disc", "Other"], validators=[DataRequired()])
    img = FileField("Enter product image", validators=[FileRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    remember_me = BooleanField("Remember")


class RegisterForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    repeat_password = PasswordField("Repeat password", validators=[equal_to("password")])
    Submit = SubmitField("Register")

    def validate_password(self, field):
        if not any(char in punctuation for char in field.data):
            raise ValidationError("Password needs some symbols.")

        if not any(char in digits for char in field.data):
            raise ValidationError("Password needs numbers.")

