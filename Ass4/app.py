from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

from flask import Flask

app = Flask(__name__)


##assignment_4
from assignment_4.assignment_4 import assignment_4
app.register_blueprint(assignment_4)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=2)


@app.route('/HomePage')
def homepage_func():
    return render_template('HomePage.html')


@app.route('/ContactPage')
def cont_func():
    return render_template('ContactPage.html')


@app.route('/assignment3_1')
def about_page():
    user_info = {'First_Name': 'Tal', 'Last_name': 'Valtzer'}

    hobbies = ('drawing', 'reading', 'traveling', 'TV', 'sea')
    return render_template('assignment3_1.html',
                           user_info=user_info,

                           hobbies=hobbies)


@app.route('/assignment3_2', methods=['GET', 'POST'])
def ass3():
    if request.method == 'GET':
        if 'user_name' in request.args:
            user_name = request.args['user_name']
            if user_name in user_dict:
                return render_template('assignment3_2.html',
                                       user_name=user_name,
                                       user_email=user_dict[user_name][0],
                                       user_Firstname=user_dict[user_name][1],
                                       user_Lastname=user_dict[user_name][2],
                                       user_age=user_dict[user_name][3]
                                       )
            elif len(user_name) == 0:
                return render_template('assignment3_2.html',
                                       user_dict=user_dict)

            else:
                return render_template('assignment3_2.html',
                                       message='User not found.')

    if request.method == 'POST':

        reg_username = request.form['user_name']
        reg_userEmail = request.form['user_email']
        reg_Firstname = request.form['user_Firstname']
        reg_Lastname = request.form['user_Lastname']
        reg_age = request.form['user_age']
        session['user_name'] = reg_username
        session['user_email'] = reg_userEmail
        session['user_Firstname'] = reg_Firstname
        session['user_Lastname'] = reg_Lastname
        session['user_age'] = reg_age
        session['Registered'] = True
        if reg_username in user_dict:
            return render_template('assignment3_2.html', message2='user is already exist!!')
        else:
            new_user = {reg_username: [reg_userEmail, reg_Firstname, reg_Lastname, reg_age]}
            user_dict.update(new_user)
            return render_template('assignment3_2.html', message2='registration succeeded')
        return render_template('assignment3_2.html')

    return render_template('assignment3_2.html')


user_dict = {
    'Tal_val': ['Tal@gmail.com', 'Tal', 'Val', '25'],
    'YoniBayoni': ['yon@gmail.com', 'Yoni', 'Rnoev', '25'],
    'Inbaraa': ['inbo@gmail.com', 'Inbar', 'Duv', '27'],
    'Rotemdi': ['rotem@gmail.com', 'Rotem', 'Didi', '26'],
    'Coralel': ['Cori@gmail.com', 'Coral', 'El', '26']

}


@app.route('/log_out')
def logout():
    session['Registered'] = False
    session.clear()
    return redirect(url_for('ass3'))


@app.route('/')
def hello_world():  # put application's code here
    return redirect('/HomePage')


if __name__ == '__main__':
    app.run()


# ----------------------------------- import -----------------------------------
import json



