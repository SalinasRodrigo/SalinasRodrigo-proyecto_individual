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


bcrypt = Bcrypt(app)

#Users-----------------------------------------------------------------------------
@app.route('/')
def index():
    # if 'user_id' in session:
    #     return redirect('/dashboard')
    return render_template("index.html")

@app.route('/admin')
def index_admin():
    # if 'user_id' in session:
    #     return redirect('/dashboard')
    return render_template("index_admin.html")

#Citas----------------------------------------------------------------------------
@app.route('/cita')
def cita():
    # if 'user_id' in session:
    #     return redirect('/dashboard')
    return render_template("cita.html")


#Analisis------------------------------------------------------------------------
@app.route('/analisis')
def analisis():
    # if 'user_id' in session:
    #     return redirect('/dashboard')
    return render_template("analisis.html")


#Registro y loguin (temporal)-----------------------------------------------------
@app.route('/registro_login')
def registro_login():
    # if 'user_id' in session:
    #     return redirect('/dashboard')
    return render_template("registro_login.html")

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
        return redirect('/registro_login')
    if len(request.form['contraseña'])<8:
        flash('Email/Contraseña invalido', 'login')
        return redirect('/registro_login')
    if not bcrypt.check_password_hash(user_in_db.contraseña, request.form['contraseña']):
        flash('Email/Contraseña invalido', 'login')
        return redirect('/registro_login')
    session['user_id'] = user_in_db.id
    if user_in_db.permisos == 1:
        return redirect('/admin')
    return redirect('/')

@app.route('/logout/process', methods=['POST'])
def logout():
    session.pop('user_id')
    return redirect('/')



