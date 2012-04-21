from flaskext.wtf import Form, TextField, required

class MessageForm(Form):
    message = TextField('Message', validators=[Required()])