# from flask import Flask, render_template
# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#   app.run(host='127.0.0.1', port=8000, debug=True)

from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import sqlite3

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class RegistrationForm(Form):
    # username = StringField('Username', [validators.Length(min=4=, max=25)])
    email = StringField('email', [validators.Length(min=6, max=45)])
    # password = PasswordField('New Password', [
    #     validators.DataRequired(),
    #     validators.EqualTo('confirm', message='Passwords must match')
    # ])
    # confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

# def init_db(db_name):
#     sql = '''
#         create table Users1
#         (
#             email text
#         );
#         '''
#     conn = sqlite3.connect(db_name)
#     c = conn.cursor()
#     c.execute(sql)
#     conn.commit()
#     conn.close()

def saveToDataBase(email, db_name):
    # init_db(name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    insertEmail = email #'"'+email+'"'
    # print(data[index])
    sql = '''
        insert into Users(
            email
        )
        values (?)
        '''
    try:    
        cur.execute(sql, (insertEmail,))
    except sqlite3.Error as e:
        flash("This email is already registered!")
        return False
    conn.commit()
    cur.close
    conn.close()
    return True

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.email.data) #watch out for no username and password
        # init_db('covid19siteDB.db')
        saveToDataBase(form.email.data, 'covid19siteDB.db')
        flash('Thanks for registering!')
        # return redirect(url_for('login')) # different formed website for entering the email
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