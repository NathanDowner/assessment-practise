from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired

class AssignmentForm(FlaskForm):
    staffMember = SelectField('Worker', coerce=int, validators=[DataRequired()])
    projects = SelectMultipleField('Projects', coerce=int, validators=[DataRequired()])
    
class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    
class StaffForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    