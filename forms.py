from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    title = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Submit')
