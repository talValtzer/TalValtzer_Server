from datetime import timedelta

from flask import Blueprint, render_template, redirect, json
import mysql.connector
from mysql.connector import Error
from flask import request, session, jsonify
from flask import Flask
# about blueprint definition
from flask import request, session
import time
import requests
import random

import app

assignment_4 = Blueprint('assignment_4', __name__, static_folder='static', static_url_path='/assignment_4',
                         template_folder='templates')


@assignment_4.route('/assignment_4')
def ass4_func():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', users=users_list)


@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    username = request.form['user_name']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    user_age = request.form['user_age']
    try:
        query = "INSERT INTO users(user_name, email, first_name,last_name,age) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
            username, email, first_name, last_name, user_age)
        interact_db(query=query, query_type='commit')
        session['msg'] = username + "added"
    except Error as er:
        session['msg'] = username + "fdgg"

    return redirect('/assignment_4')


@assignment_4.route('/users')
def ass433_func():
    return render_template('assignment_4.html')


@assignment_4.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_name = request.form['user_name']
    query = "DELETE FROM users WHERE user_name='%s';" % user_name
    # print(query)
    interact_db(query, query_type='commit')
    session['msg'] = user_name + " deleted"
    return redirect('/assignment_4')


@assignment_4.route('/update_user', methods=['POST'])
def update_user_func():
    user_name = request.form['user_name']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['user_age']

    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             passwd='root',
                                             database='talweb')
        updateCursor = connection.cursor()
        updateCursor.execute('''
            UPDATE users
            SET email = %s,first_name = %s, last_name = %s, age = %s
            WHERE user_name = %s
            ''', (email, first_name, last_name, age, user_name))
        connection.commit()
        session['msg'] = connection.commit()


    except Error as er:
        session['msg'] = "can not found user " + user_name
    finally:
        connection.close()

    return redirect('/assignment_4')


@assignment_4.route('/assignment4/users')
def assignment4_users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    users_json = json.dumps(users_list)
    return users_json


@assignment_4.route('/fetch_be')
def fetch_be_func():
    print("Ddggggdd")

    print("dfdfasfaf")
    if 'type' in request.args:
        id = int(request.args['num_id'])
        session['num'] = id
        pockemons = get_pockemons(id)
        print(pockemons)
        print()
        save_users_to_session(pockemons)
    else:
        session.clear()
    return redirect('/fetch_fe')

@assignment_4.route('/assignment4/restapi_users',defaults={'USER_ID':-1})
@assignment_4.route('/assignment4/restapi_users/<USER_ID>')
def get_users_func(USER_ID):
    if USER_ID == -1:
        print("yes -1")
        return_dict = {}
        query = 'select * from users;'
        users = interact_db(query, query_type='fetch')
        for user in users:
            return_dict[f'user_{user.user_name}'] = {
                'status': 'success',
                'name': user.first_name,
                'email': user.email,
            }
    else:
        print(USER_ID)
        query = "select * from users where user_name='%s';"%USER_ID
        users = interact_db(query=query, query_type='fetch')
        print(len(users))
        if len(users) == 0:
            return_dict = {
                'status': 'failed',
                'message': 'user not found'
            }
        else:

            return_dict = {
                'status': 'success',
                'user_name': users[0].user_name,
                'email': users[0].email,
                'age': users[0].age,
            }
    return  jsonify(return_dict)


@assignment_4.route('/fetch_fe')
def fetch_fe_func():
    print("Dddd")
    return render_template('assignment4_froned.html')


def get_pockemons(id):
    pockemons = []
    res = requests.get(f'https://reqres.in/api/users/{id}')
    print(res)
    pockemons.append(res.json())
    return pockemons


def save_users_to_session(pockemons):
    users_list_to_save = []
    for pockemon in pockemons:
        pockemons_dict = {
            'data': {
                'avatar': pockemon['data']['avatar']
            },
            'email': pockemon['data']['email'],
            'first_name': pockemon['data']['first_name'],

        }
        users_list_to_save.append(pockemons_dict)
    session['pockemons'] = users_list_to_save
    session['start'] = True


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='talweb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value
