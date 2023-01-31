from wtforms import Form, RadioField, StringField, validators, SubmitField, HiddenField
from flask_wtf import FlaskForm

class owner(FlaskForm):
    name = StringField("What is your name ? ")
    pet_name = StringField("Your pet name ? ")
    pet_breed = RadioField("Please Choose your Breed : ", choices = [('Dog', 'Dog'), ('Cat', 'Cat')])
    submit = SubmitField("Submit")


