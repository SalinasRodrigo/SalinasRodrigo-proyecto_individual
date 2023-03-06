from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask import flash
from flask_app.models import especialidad

class Medico:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.nombre = db_data['nombre']
        self.apellido = db_data['apellido'] 
        self.email = db_data['email']
        self.ci = db_data['ci']
        self.especialidad_id = db_data['especialidad_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.especialidad = None

    @classmethod
    def save( cls , data ):
        query = ("INSERT INTO medicos ( nombre, apellido, email, especialidad_id, hospital_id, ci, created_at , updated_at) "+
                 "VALUES (%(nombre)s, %(apellido)s, %(email)s, %(especialidad_id)s, %(hospital_id)s, %(ci)s, NOW(),NOW());")
        result = connectToMySQL('proyecto_db').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM medicos;"
        meds_from_db =  connectToMySQL('proyecto_db').query_db(query)
        meds = []
        for med in meds_from_db:
            meds.append(cls(med))
        return meds
    
    @classmethod
    def get_all_medicos_especialidad(cls):
        query = ("SELECT * FROM medicos " +
                "left join especialidades on especialidades.id = medicos.especialidad_id "+
                "ORDER BY especialidades.nombre ASC;")
        meds_from_db =  connectToMySQL('proyecto_db').query_db(query)
        meds = []
        if not meds_from_db:
            return meds_from_db
        for row_db in meds_from_db:
            especialidad_data = {
                "id" : row_db["especialidades.id"],
                "nombre" : row_db["especialidades.nombre"],
                "created_at" : row_db["especialidades.created_at"],
                "updated_at" : row_db["especialidades.updated_at"]
            }
            med = cls(row_db)
            med.especialidad = especialidad.Especialidad(especialidad_data)
            meds.append(med)
        return meds

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM medicos WHERE id = %(medico_id)s;"
        result = connectToMySQL('proyecto_db').query_db(query, data)
        if not result:
            return result
        return cls(result[0])

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM medicos WHERE email = %(email)s;"
        result = connectToMySQL('proyecto_db').query_db(query, data)
        if not result:
            return result
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE medicos SET nombre=%(nombre)s, apellido=%(apellido)s,  email=%(email)s, especialidad_id=%(especialidad_id)s, ci=%(ci)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('proyecto_db').query_db(query,data)

    @classmethod
    def destroy(cls,id):
        query = "DELETE FROM medicos WHERE id = %i;"%(id)
        return connectToMySQL('proyecto_db').query_db(query)

    @staticmethod
    def validacion_registro(data):
        is_true = True
        if  len(data['nombre'])<3 or data['nombre']=="":
            flash('The first name must have at least 3 characters.', 'registro')
            is_true = False
        if len(data['apellido'])<3 or data['apellido']=="":
            flash('The last name must have at least 3 characters.', 'registro')
            is_true = False
        if (not EMAIL_REGEX.match(data['email']) or data['email']==""):
            flash('Wrong email format.', 'registro')
            is_true = False
        if  Medico.get_by_email(data):
            flash('There is already a registered user with that email.', 'registro')
            is_true = False
        if data['ci']=="":
            flash('The ci must have at least 8 characters.', 'registro')
            is_true = False
        if data['especialidad_id']=="":
            flash('The especialidad_id must have at least 8 characters.', 'registro')
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
        if data['ci']=="":
            flash('The ci must have at least 8 characters.', 'update')
            is_true = False
        if data['especialidad_id']=="":
            flash('The especialidad_id must have at least 8 characters.', 'update')
            is_true = False
        return is_true