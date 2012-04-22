from flaskext.wtf import Form, TextField, Required

class MessageForm(Form):
    message = TextField('Message', validators=[Required()])