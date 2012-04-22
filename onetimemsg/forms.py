from flaskext.wtf import Form, TextAreaField, Required, Length

class MessageForm(Form):
    message = TextAreaField('Message', validators=[Required(), Length(min=1, max=500)])