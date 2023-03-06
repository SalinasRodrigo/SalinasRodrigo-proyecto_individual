from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash
# from flask_app.models import magazine

class Usuario:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.nombre = db_data['nombre']
        self.apellido = db_data['apellido'] 
        self.email = db_data['email']
        self.ci = db_data['ci']
        self.permisos = db_data['permisos']
        self.contraseña = db_data['contraseña']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = ("INSERT INTO usuarios ( nombre, apellido, email, contraseña, ci, permisos, created_at , updated_at) "+
                 "VALUES (%(nombre)s, %(apellido)s, %(email)s, %(contraseña)s, %(ci)s, 0, NOW(),NOW());")
        result = connectToMySQL('proyecto_db').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        emails_from_db =  connectToMySQL('proyecto_db').query_db(query)
        emails = []
        for user in emails_from_db:
            emails.append(cls(user))
        return emails

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL('proyecto_db').query_db(query, data)

        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        result = connectToMySQL('proyecto_db').query_db(query, data)
        if not result:
            return result
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s,  email=%(email)s, ci=%(ci)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('proyecto_db').query_db(query,data)

    @classmethod
    def destroy(cls,id):
        query = "DELETE FROM usuarios WHERE id = %i;"%(id)
        return connectToMySQL('proyecto_db').query_db(query)

    @staticmethod
    def validacion_registro(data):
        is_true = True
        if  len(data['nombre'])<3 or data['nombre']=="":
            flash('El nombre debe tener al menos 3 caracteres.', 'registro')
            is_true = False
        if len(data['apellido'])<3 or data['apellido']=="":
            flash('El apellido debe tener al menos 3 caracteres.', 'registro')
            is_true = False
        if (not EMAIL_REGEX.match(data['email']) or data['email']==""):
            flash('Formato de email incorrecto.', 'registro')
            is_true = False
        if  Usuario.get_by_email(data):
            flash('Ya existe una cuenta con este email', 'registro')
            is_true = False
        if data['ci']=="":
            flash('El usuario debe tener un número de CI.', 'registro')
            is_true = False
        if len(data['contraseña'])<8 or data['contraseña']=="":
            flash('La contraseña debe tener al menos 8 caracteres.', 'registro')
            is_true = False
        if not data['contraseña'] == data['confi']:
            flash ('Las contraseñas no coinciden.', 'registro')
            is_true = False
        return is_true

    @staticmethod
    def validacion_update(data):
        is_true = True
        if  len(data['nombre'])<3 or data['nombre']=="":
            flash('The first name must have at least 3 characters.', 'update')
            is_true = False
        if len(data['apellido'])<3 or data['apellido']=="":
            flash('The last name must have at least 3 characters.', 'update')
            is_true = False
        if (not EMAIL_REGEX.match(data['email']) or data['email']==""):
            flash('Wrong email format.', 'update')
            is_true = False
        return is_true