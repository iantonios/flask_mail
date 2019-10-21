# Need to install flask-mail to run
# Also create an environment variable MAIL_PASSWORD:
#    export MAIL_PASSWORD=your_gmail_password

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
        flash('Message sent!')
        mail_form.email.data = ''
        mail_form.message.data = ''
    return render_template('index.html', form=mail_form)




