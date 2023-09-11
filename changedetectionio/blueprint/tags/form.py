import sys
sys.path.append("changedetectionio")

from wtforms import (
    BooleanField,
    Form,
    IntegerField,
    RadioField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
    validators,
)



class SingleTag(Form):

    name = StringField('Tag name', [validators.InputRequired()], render_kw={"placeholder": "Name"})
    save_button = SubmitField('Save', render_kw={"class": "pure-button pure-button-primary"})




