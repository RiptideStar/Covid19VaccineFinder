# from flask import Flask, render_template
# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#   app.run(host='127.0.0.1', port=8000, debug=True)

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms import Form, BooleanField, StringField, PasswordField, validators

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class RegistrationForm(Form):
    # username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('email', [validators.Length(min=6, max=45)])
    # password = PasswordField('New Password', [
    #     validators.DataRequired(),
    #     validators.EqualTo('confirm', message='Passwords must match')
    # ])
    # confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    # if request.method == 'POST' and form.validate():
    #     user = User(form.username.data, form.email.data, form.password.data) #watch out for no username and password
    #     db_session.add(user)
    #     flash('Thanks for registering')
    #     return redirect(url_for('login'))
    return render_template('register.html', form=form)

# @app.route("/", methods=['GET', 'POST'])
# def hello():
#     form = ReusableForm(request.form)

#     print (form.errors)
#     if request.method == 'POST':
#         name=request.form['name']
#         print (name)

#     if form.validate():
#         # Save the comment here.
#         flash('Your email is: ' + name)
#     else:
#         flash('All the form fields are required. ')
#     return render_template('inputForm.html', form=form)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True) 