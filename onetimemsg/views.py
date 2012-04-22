from flask import flash, redirect, render_template, request, url_for
from onetimemsg import app
from onetimemsg.database import db_session
from onetimemsg.models import Message
from onetimemsg.forms import MessageForm
from onetimemsg.utils import uid_generator

@app.route('/')
def index():
    form = MessageForm()
    return render_template('index.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    form = MessageForm()
    if form.validate_on_submit():
        uid = uid_generator()
        while Message.query.filter_by(uid=uid).first() is None:
            uid = uid_generator()
        message = Message(ip=request.remote_addr,
                          uid=uid,
                          text=form.message.data,
                          )
        db_session.add(message)
        db_session.commit()
        flash(uid, 'message_created')
        return redirect(url_for('index'))
    return render_template('submit.html', form=form)

@app.route('/<regex("[a-zA-Z0-9]+"):uid>')
def message_detail(uid):
    message = Message.query.filter_by(uid=uid).first_or_404()
    db_session.delete(message)
    db_session.commit()
    return render_template('message_detail.html', message=message)