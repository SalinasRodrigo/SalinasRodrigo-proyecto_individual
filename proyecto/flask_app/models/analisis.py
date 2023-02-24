from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.models import magazine

class Analisis:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.nombre = db_data['nombre']
        self.requisitos = db_data['requisitos']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = ("INSERT INTO hospitles ( nombre, requisitos, created_at , updated_at) "+
                 "VALUES (%(nombre)s, %(requisitos)s, NOW(),NOW());")
        result = connectToMySQL('proyecto_db').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM hospitles;"
        emails_from_db =  connectToMySQL('proyecto_db').query_db(query)
        emails = []
        for user in emails_from_db:
            emails.append(cls(user))
        return emails

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM hospitles WHERE id = %(id)s;"
        result = connectToMySQL('proyecto_db').query_db(query, data)

        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE hospitles SET nombre=%(nombre)s, requisitos=%(requisitos)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('proyecto_db').query_db(query,data)

    @classmethod
    def destroy(cls,id):
        query = "DELETE FROM hospitles WHERE id = %i;"%(id)
        return connectToMySQL('proyecto_db').query_db(query)

    @staticmethod
    def validacion_registro(data):
        is_true = True
        if  len(data['nombre'])<3 or data['nombre']=="":
            flash('The first name must have at least 3 characters.', 'registro')
            is_true = False
        return is_true

    @staticmethod
    def validacion_update(data):
        is_true = True
        if  len(data['nombre'])<3 or data['nombre']=="":
            flash('The first name must have at least 3 characters.', 'update')
            is_true = False
        return is_true