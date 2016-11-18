from flask_wtf import Form
from wtforms import StringField,  BooleanField, PasswordField
from wtforms.validators import Required


class LoginForm(Form):
    email = StringField('Email adress', validators = [Required()])
    password = PasswordField ('Password', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)


