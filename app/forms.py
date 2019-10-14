from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField ,SubmitField
from wtforms.validators import Required

class ArticleForm(FlaskForm):

    title = StringField("Article title", validators= [Required()])
    article = TextAreaField("News review", validators= [Required()])
    submit = SubmitField("Submit")