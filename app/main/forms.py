from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,DataRequired,EqualTo,EqualTo
from ..models import Pitch


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class NewPitch(FlaskForm):
    category = SelectField('Pitch Category', coerce=int, choices=[(0, 'Please Input your Category...'), (1, 'Interview'),(2, 'pickup_lines'),(3, 'product_pitch'),(4, 'promotion_pitch')],validators=[DataRequired()])
    title = StringField('Pitch Title', validators=[Required()])
    pitch = TextAreaField('Pitch',validators=[Required()])
    submit = SubmitField('Submit')