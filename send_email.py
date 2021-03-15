# To run, do the following first:
# 1) install flask-mail and flask-bootstrap: sudo pip3 install flask-mail flask-bootstrap
# 2) create an environment variable MAIL_PASSWORD:
#    export MAIL_PASSWORD=your_gmail_password
#    export FLASK_APP=send_email.py
#    export FLASK_DEBUG=1
# 3) Modify MAIL_USERNAME below to your gmail address (preferably create a test account).
# 4) Modify MAIL_DEFAULT_SENDER as well 
# 5) In the security settings of your Google account, turn on "Less Secure App Access"

from flask import Flask, render_template, flash
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
import os


class SendEmail(FlaskForm):
    email = StringField('Recipient: ', validators=[DataRequired(), Email()])
    message = TextAreaField('Your message:', validators=[DataRequired()])
    submit = SubmitField('Send')

app = Flask(__name__)

app.config.update(
        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT = 465,
        MAIL_USE_TLS = False,
        MAIL_USE_SSL = True, 
        MAIL_USERNAME = 'scsucsc330@gmail.com',
        MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD'),
        MAIL_DEFAULT_SENDER = ('I Antonios', 'scsucsc330@gmail.com'),
        SECRET_KEY = 'some secret key for CSRF')

mail = Mail(app)
moment = Moment(app)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def send_mail():
    mail_form = SendEmail()
    if mail_form.validate_on_submit():
        recipient = mail_form.email.data
        message = mail_form.message.data
        subject = 'Test Flask email'
        msg = Message(subject, recipients=[recipient], body = message)
        mail.send(msg)
        mail_form.email.data = ''
        mail_form.message.data = ''
    return render_template('index.html', form=mail_form)




