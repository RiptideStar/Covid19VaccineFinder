
from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import sqlite3

# App config.
DEBUG = True
app = Flask(__name__)
# app.config.from_object(__name__)
# app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class RegistrationForm(Form):
    # username = StringField('Username', [validators.Length(min=4=, max=25)])
    email = StringField('Email:', [validators.Length(min=8, max=65)])
    # password = PasswordField('New Password', [
    #     validators.DataRequired(),
    #     validators.EqualTo('confirm', message='Passwords must match')
    # ])
    # confirm = PasswordField('Repeat Password')
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

def queryFromDataBase(db_name, sql):
    # init_db(name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    return_list = []
    cur.execute(sql)    
    return_list = cur.fetchall()
    conn.commit()
    cur.close
    conn.close()
    return return_list

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

def removeFromDataBase(email, db_name):
    # init_db(name)
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
     #'"'+email+'"'
    # print(data[index])
    sql = '''
        delete from Users where email=?
        '''
    try:    
        cur.execute(sql, (email,))
    except sqlite3.Error as e:
        print(e)
        flash("This email has been removed!")
        return False
    flash("This email has been removed!")    
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
        # if form.submitted == 'Register':
        if 'Register' in request.form:
            saveToDataBase(form.email.data, 'covid19siteDB.db')
            flash('Thanks for registering!')
        else:
            removeFromDataBase(form.email.data, 'covid19siteDB.db')   

        # return redirect(url_for('login')) # different formed website for entering the email
    sites = [("4500 NE 122nd, Portland", "www.signupgenius.com/go/copvaccination4-17", "No"), ("MHCC", "www.signupgenius.com/go/4-16pfizermhcc", "Yes")]
    return render_template('register.html', form=form, sites=sites)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True) 