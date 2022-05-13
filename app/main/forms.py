from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Kindly let us know you better.', validators = [InputRequired()])
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField ('Kindly leave a comment', validators = [InputRequired()])
    submit = SubmitField('Comment')

class PitchForm(FlaskForm):
    title = StringField('Title', validators = [InputRequired()])
    category = SelectField('Category', choices = [('Events', 'Events'),('Job', 'Job'), ('Advertisement', 'Advertisement')], validators = [InputRequired()])
    post = TextAreaField('Add Your Pitch', validators = [InputRequired()])
    submit = SubmitField('Pitch')