from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])\S{8,16}$')
from flask import flash
from flask_app.models import magazine

class User:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name'] 
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.thoughts = []

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at , updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(),NOW());"
        result = connectToMySQL('revistas_db').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        emails_from_db =  connectToMySQL('revistas_db').query_db(query)
        emails = []
        for user in emails_from_db:
            emails.append(cls(user))
        return emails

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL('revistas_db').query_db(query, data)

        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('revistas_db').query_db(query, data)
        if not result:
            return result
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s,  email=%(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('revistas_db').query_db(query,data)

    @classmethod
    def destroy(cls,id):
        query = "DELETE FROM users WHERE id = %i;"%(id)
        return connectToMySQL('revistas_db').query_db(query)

    @staticmethod
    def validacion_registro(data):
        is_true = True
        if  len(data['fname'])<3 or data['fname']=="":
            flash('The first name must have at least 3 characters.', 'registro')
            is_true = False
        if len(data['lname'])<3 or data['lname']=="":
            flash('The last name must have at least 3 characters.', 'registro')
            is_true = False
        if (not EMAIL_REGEX.match(data['email']) or data['email']==""):
            flash('Wrong email format.', 'registro')
            is_true = False
        if  User.get_by_email(data):
            flash('There is already a registered user with that email.', 'registro')
            is_true = False
        if len(data['password'])<8 or data['password']=="":
            flash('The password must have at least 8 characters.', 'registro')
            is_true = False
        if not data['password'] == data['confi']:
            flash ('The passwords do not match.', 'registro')
            is_true = False
        return is_true

    @staticmethod
    def validacion_update(data):
        is_true = True
        if  len(data['fname'])<3 or data['fname']=="":
            flash('The first name must have at least 3 characters.', 'update')
            is_true = False
        if len(data['lname'])<3 or data['lname']=="":
            flash('The last name must have at least 3 characters.', 'update')
            is_true = False
        if (not EMAIL_REGEX.match(data['email']) or data['email']==""):
            flash('Wrong email format.', 'update')
            is_true = False
        return is_true