from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField, FileField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email, InputRequired


class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    type = SelectField('Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[DataRequired()])
    no_of_bedrooms = StringField('Number of Bedrooms', validators=[DataRequired()])
    no_of_bathrooms = StringField('Number of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    picture = FileField('Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    price = StringField('Price', validators=[DataRequired()])