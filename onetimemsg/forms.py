from flaskext.wtf import Form, TextField, Required, Length

class MessageForm(Form):
    message = TextField('Message', validators=[Required(), Length(max=500)])