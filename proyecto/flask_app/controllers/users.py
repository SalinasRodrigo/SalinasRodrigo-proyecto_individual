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

#Users-----------------------------------------------------------------------------
@app.route('/')
def index():
    if 'user_id' in session:
        data = {
            "usuario_id": session['user_id']
        }
        Cita.validar(data)
        Cita_analisis.validar(data)
        return render_template("index.html", all_citas = Cita.get_all_by_usuario(data),
                                all_analisis = Cita_analisis.get_all_by_usuario(data))

    return  render_template("index.html")

@app.route('/admin')
def index_admin():
    return render_template("index_admin.html", all_especialidades = Especialidad.get_all(),
                            all_hospitales = Hospital.get_all())

@app.route('/med/process', methods=['POST'])
def add_med():
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "ci": request.form['ci'],
        "especialidad_id": request.form['especialidad_id'],
        "hospital_id": request.form['hospital_id']
    }
    
    if not Medico.validacion_registro(data):
        return redirect('/')
    
    Medico.save(data)

    return redirect('/admin')

@app.route('/espe/process', methods=['POST'])
def add_espe():
    data = {
        "nombre": request.form['nombre']
    }
    
    if not Especialidad.validacion_registro(data):
        return redirect('/')
    
    Especialidad.save(data)
    return redirect('/admin')


@app.route('/analisis/process', methods=['POST'])
def add_analisis():
    data = {
        "nombre": request.form['nombre'],
        "requisitos": request.form['requisitos']
    }
    
    if not Analisis.validacion_registro(data):
        return redirect('/admin')
    Analisis.save(data)
    return redirect('/admin')

@app.route('/hosp/process', methods=['POST'])
def add_hosp():
    data = {
        "nombre": request.form['nombre'],
        "direccion": request.form['direccion']
    }
    
    if not Hospital.validacion_registro(data):
        return redirect('/')
    
    Hospital.save(data)
    return redirect('/admin')

@app.route('/register/process', methods=['POST'])
def registro():
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "ci": request.form['ci'],
        "contraseña": request.form['contraseña'],
        "confi": request.form['confi']
    }
    
    if not Usuario.validacion_registro(data):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['contraseña'])
    data['contraseña'] = pw_hash
    id = Usuario.save(data)
    session['user_id'] = id
    return redirect('/registro_login')

@app.route('/login/process', methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    user_in_db = Usuario.get_by_email(data)
    
    if not user_in_db:
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    if len(request.form['contraseña'])<8:
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.contraseña, request.form['contraseña']):
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    if user_in_db.permisos == 1:
        return redirect('/admin')
    return redirect('/')

@app.route('/logout/process', methods=['POST'])
def logout():
    session.pop('user_id')
    return redirect('/')



