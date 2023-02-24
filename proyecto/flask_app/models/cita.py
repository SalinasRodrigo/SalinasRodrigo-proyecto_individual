from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import magazine

class Cita:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.fecha = db_data['fecha']
        self.usuario_id = db_data['usuario_id']
        self.medico_id = db_data['medico_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = ("INSERT INTO citas (fecha, medico_id, usuario_id, created_at , updated_at) "+
                 "VALUES (%(fecha)s, %(medico_id)s, %(usuario_id)s, NOW(),NOW());")
        result = connectToMySQL('proyecto_db').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM citas;"
        fechas_from_db =  connectToMySQL('proyecto_db').query_db(query)
        fechas = []
        for user in fechas_from_db:
            fechas.append(cls(user))
        return fechas

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM citas WHERE id = %(id)s;"
        result = connectToMySQL('proyecto_db').query_db(query, data)

        return cls(result[0])

    @classmethod
    def get_by_fecha(cls, data):
        query = "SELECT * FROM citas WHERE fecha = %(fecha)s;"
        result = connectToMySQL('proyecto_db').query_db(query, data)
        if not result:
            return result
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE citas SET fecha=%(fecha)s, medico_id=%(medico_id)s, usuario_id=%(usuario_id)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('proyecto_db').query_db(query,data)

    @classmethod
    def destroy(cls,id):
        query = "DELETE FROM citas WHERE id = %i;"%(id)
        return connectToMySQL('proyecto_db').query_db(query)