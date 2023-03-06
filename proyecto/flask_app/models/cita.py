from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import medico
import datetime

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
        #creación de una fecha para la cita
        ultima_cita = Cita.get_ultima_cita(data)
        fecha = datetime.datetime.now()
        if not ultima_cita:
            fecha = fecha.replace(hour=7, minute=0, second = 0)
            fecha = fecha + datetime.timedelta(days=1)

        elif ultima_cita.fecha < ((fecha + datetime.timedelta(days=1)).replace(hour=6, minute=59, second = 59)):

            fecha = fecha.replace(hour=7, minute=0, second = 0)
            fecha = fecha + datetime.timedelta(days=1)
        else:
            fecha = ultima_cita.fecha + datetime.timedelta(minutes=30)
            if int(fecha.strftime("%H")) >= 16:
                fecha = fecha.replace(hour=7, minute=0, second = 0)
                fecha = fecha + datetime.timedelta(days=1)
            if int(fecha.strftime("%H")) >= 12 and int(fecha.strftime("%H")) < 13:
                fecha = fecha.replace(hour=13, minute=0, second = 0)
        data['fecha'] = fecha
        query = ("INSERT INTO citas (fecha, medico_id, usuario_id, created_at , updated_at) "+
                 "VALUES (%(fecha)s, %(medico_id)s, %(usuario_id)s, NOW(),NOW());")
        result = connectToMySQL('proyecto_db').query_db(query, data)
        return result

    @classmethod
    def get_ultima_cita(cls, data):
        query = ("SELECT * FROM citas WHERE medico_id = %(medico_id)s "+
                "ORDER BY fecha DESC;")
        result = connectToMySQL('proyecto_db').query_db(query, data)
        print(result)
        if not result:
            return result
        return cls(result[0])


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM citas;"
        citas_from_db =  connectToMySQL('proyecto_db').query_db(query)
        citas = []
        for cita in citas_from_db:
            citas.append(cls(cita))
        return citas
    
    @classmethod
    def get_all_by_usuario(cls, data):
        query = "SELECT * FROM citas WHERE usuario_id = %(usuario_id)s;"
        citas_from_db =  connectToMySQL('proyecto_db').query_db(query, data)
        citas = []
        for cita in citas_from_db:
            citas.append(cls(cita))
        return citas


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
    def destroy(cls,data):
        query = "DELETE FROM citas WHERE id = %(cita_id)s;"
        return connectToMySQL('proyecto_db').query_db(query, data)
    
    @classmethod
    def validar(cls,data):
        #validación para eliminar la citas que ya pasaron
        citas = Cita.get_all_by_usuario(data)
        fecha = datetime.datetime.now()
        for cita in citas:
            if fecha>cita.fecha:
                data_2 = {
                    "cita_id": cita.id
                }
                Cita.destroy(data_2)
        return
    
    def formato_fecha(self):
        formato = str(self.fecha.strftime("%d")) + "/" + str(self.fecha.strftime("%m"))
        return formato
    
    def formato_hora(self):
        formato = str(self.fecha.strftime("%H"))+":"+str(self.fecha.strftime("%M"))
        return formato