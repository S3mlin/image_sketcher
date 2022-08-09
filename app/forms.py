from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired


class ImageForm(FlaskForm):
    image = FileField('Image', validators=[FileRequired(),
             FileAllowed(['jpg', 'png'], 'Jpg and png images only!')])
    submit = SubmitField('Upload')