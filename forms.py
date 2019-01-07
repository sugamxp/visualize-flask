from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField, validators

class FileForm(FlaskForm):
    file = FileField("Select csv/tsv/xlsx file : ", validators=[FileRequired()], )
    submit = SubmitField('Upload file')