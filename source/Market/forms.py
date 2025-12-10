from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField,
    RadioField, IntegerField, HiddenField, TextAreaField
)
from wtforms.validators import (
    DataRequired, Email, Length, ValidationError, NumberRange
)
from Market.models import User


class RegisterForm(FlaskForm):
    username = StringField(validators=[Length(min=2, max=30), DataRequired()], label="User Name")
    email_address = StringField(validators=[Email(), DataRequired()], label="Email Address")
    password1 = PasswordField(validators=[Length(min=3), DataRequired()], label="Password")
    submit = SubmitField(label="Create Account")

    def validate_username(self, val):
        exists = User.query.filter_by(username=val.data).first()
        if exists:
            raise ValidationError("Username already exists! Please try a different username.")

    def validate_email_address(self, val):
        exists = User.query.filter_by(email_address=val.data).first()
        if exists:
            raise ValidationError("Email Address already exists! Please try a different email address.")


class LoginForm(FlaskForm):
    username = StringField(label="User Name", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Sign In")


class AddToCartForm(FlaskForm):
    submit = SubmitField(label="Add to Cart")


class RemoveFromCartForm(FlaskForm):
    submit = SubmitField(label="Remove")


class CheckoutForm(FlaskForm):
    full_name = StringField(validators=[DataRequired()], label="Full Name")
    phone = StringField(validators=[DataRequired()], label="Phone Number")
    email = StringField(validators=[Email(), DataRequired()], label="Email")
    address1 = StringField(validators=[DataRequired()], label="Address Line 1")
    address2 = StringField(label="Address Line 2")
    zip_code = StringField(validators=[DataRequired()], label="Zip code")
    card_number = StringField(validators=[Length(min=12, max=19), DataRequired()], label="Card Number")
    expiry = StringField(validators=[Length(min=4, max=7), DataRequired()], label="Exp Date")
    cvv = PasswordField(validators=[Length(min=3, max=4), DataRequired()], label="CVV")

    shipping_option = RadioField(
        label="Shipping Option",
        choices=[
            ("ground", "Ground"),
            ("three_day", "3 Day"),
            ("overnight", "Overnight")
        ],
        default="ground",
        validators=[DataRequired()]
    )

    submit = SubmitField(label="Complete Checkout")


class PromoteAdminForm(FlaskForm):
    username = StringField(
        validators=[DataRequired(), Length(min=2, max=30)],
        label="Username"
    )
    submit = SubmitField(label="Submit")


class AdminItemForm(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(min=2, max=50)], label="Name")
    price = IntegerField(validators=[DataRequired(), NumberRange(min=0)], label="Price (integer dollars)")
    description = TextAreaField(validators=[DataRequired(), Length(min=2, max=1024)], label="Description")
    image_url = StringField(validators=[Length(max=255)], label="Image URL")
    item_id = HiddenField()
    submit = SubmitField(label="Save")
