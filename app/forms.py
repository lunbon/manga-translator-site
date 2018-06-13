from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired

class EditChapterForm(FlaskForm):
	chapter_name = StringField('chapter name: ', validators=[DataRequired()])
	chapter_number = IntegerField('chapter_number: ', validators=[DataRequired()])
	poster_url = StringField('poster url: ', validators=[DataRequired()])
	read_url = StringField('read url: ', validators=[DataRequired()])
	submit = SubmitField('Save')

class EditTitleForm(FlaskForm):
	title_name = StringField('title_name: ', validators=[DataRequired()])
	description = StringField('description: ')
	submit = SubmitField('Save')

