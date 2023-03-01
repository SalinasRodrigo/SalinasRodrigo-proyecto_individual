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

#Citas----------------------------------------------------------------------------
@app.route('/cita')
def cita():
    if not 'user_id' in session:
         return redirect('/')
    return render_template("cita.html", all_medicos = Medico.get_all_medicos_especialidad(),
                            all_especialidades = Especialidad.get_all(), user_id = session['user_id'])

@app.route('/agendar_cita/<int:user_id>/<int:med_id>', methods=['POST'])
def agendar_cita(user_id, med_id):
    data = {
        "usuario_id":user_id,
        "medico_id": med_id
    }

    Cita.save(data)
    return redirect('/cita')

@app.route('/cita/delete/<int:id>', methods=['POST'])
def cita_delete(id):
    data = {
        "cita_id":id
    }

    Cita.destroy(data)
    return redirect('/')


@app.route('/cita_data/<int:id>')
def cita_data(id):
    if not 'user_id' in session:
         return redirect('/')
    data = {
        "id": id
    }
    cita = Cita.get_by_id(data)
    data["medico_id"] = cita.medico_id
    med = Medico.get_by_id(data)
    data ["especialidad_id"] = med.especialidad_id
    espe = Especialidad.get_by_id(data)
    return render_template("cita_data.html", cita = cita,
                            med = med, espe = espe)