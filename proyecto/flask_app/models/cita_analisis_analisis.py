from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import analisis

class Cita_analisis_analisis:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.analisis_id = db_data['analisis_id']
        self.cita_analisis = db_data['cita_analisis']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = ("INSERT INTO citas_analisis_analisis (cita_analisis_id, analisis_id, created_at , updated_at) "+
                 "VALUES (%(cita_analisis_id)s, %(analisis_id)s, NOW(),NOW());")
        result = connectToMySQL('proyecto_db').query_db(query, data)
        print(result)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM citas_analisis_analisis;"
        fechas_from_db =  connectToMySQL('proyecto_db').query_db(query)
        fechas = []
        for user in fechas_from_db:
            fechas.append(cls(user))
        return fechas
    
    @classmethod
    def get_analisis(cls, data):
        query = ("SELECT analisis.id FROM citas_analisis "+
                "left join citas_analisis_analisis on citas_analisis_analisis.cita_analisis_id = citas_analisis.id "+
                "left join analisis on analisis.id = citas_analisis_analisis.analisis_id "+
                "where citas_analisis.id = %(id)s;")
        analisis_from_db =  connectToMySQL('proyecto_db').query_db(query, data)
        analisis_list = []
        for a in analisis_from_db:
            analisis_list.append(analisis.Analisis.get_by_id(a))
        return analisis_list

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM citas_analisis_analisis WHERE id = %(id)s;"
        result = connectToMySQL('proyecto_db').query_db(query, data)

        return cls(result[0])

    @classmethod
    def get_by_fecha(cls, data):
        query = "SELECT * FROM citas_analisis_analisis WHERE fecha = %(fecha)s;"
        result = connectToMySQL('proyecto_db').query_db(query, data)
        if not result:
            return result
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE citas_analisis_analisis SET cita_analisis_id=%(cita_analisis_id)s, analisis_id=%(analisis_id)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('proyecto_db').query_db(query,data)

    @classmethod
    def destroy(cls,id):
        query = "DELETE FROM citas_analisis_analisis WHERE id = %i;"%(id)
        return connectToMySQL('proyecto_db').query_db(query)
    
    @classmethod
    def destroy_by_cita_analisis_id(cls,data):
        query = "DELETE FROM citas_analisis_analisis WHERE cita_analisis_id = %(cita_analisis_id)s;"
        return connectToMySQL('proyecto_db').query_db(query,data)