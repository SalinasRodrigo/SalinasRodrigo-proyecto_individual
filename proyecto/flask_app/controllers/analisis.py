from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario
from flask_app.models.analisis import Analisis
from flask_app.models.cita import Cita
from flask_app.models.cita_analisis import Cita_analisis
from flask_app.models.hospital import Hospital
from flask_app.models.medico import Medico
from flask_app.models.cita_analisis_analisis import Cita_analisis_analisis
from flask_app.models.especialidad import Especialidad

bcrypt = Bcrypt(app)

#Analisis------------------------------------------------------------------------
@app.route('/analisis')
def analisis():
    if not 'user_id' in session:
         return redirect('/')
    return render_template("analisis.html", all_analisis = Analisis.get_all(), user_id = session['user_id'])

@app.route('/agendar_analisis/<int:user_id>/<int:hospital_id>', methods=['POST'])
def agendar_analisis(user_id, hospital_id):
    data = {
        "usuario_id":user_id,
        "hospital_id": hospital_id
    }
    id = Cita_analisis.save(data)
    
    for a in request.form:
        data["cita_analisis_id"] = id
        print("Cita_analisis ID:", id)
        data["analisis_id"]=request.form[a]
        print("analisis_id:", data["analisis_id"])
        Cita_analisis_analisis.save(data)
    return redirect('/analisis_data/'+str(id))

@app.route('/cita_analisis/delete/<int:id>', methods=['POST'])
def cita_analisis_delete(id):
    data = {
        "cita_analisis_id":id
    }

    Cita_analisis_analisis.destroy_by_cita_analisis_id(data)
    Cita_analisis.destroy(data)
    
    return redirect('/')

@app.route('/analisis_data/<int:id>')
def analisis_data(id):
    if not 'user_id' in session:
         return redirect('/')
    data = {
        "id": id
    }
    return render_template("analisis_data.html", cita = Cita_analisis.get_by_id(data),
                            all_analisis = Cita_analisis_analisis.get_analisis(data))