from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.magazine import Magazine
from flask_app.models.subscription import Subscription


bcrypt = Bcrypt(app)

#Users-----------------------------------------------------------------------------
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template("index.html")

@app.route('/account')
def account():
    if not 'user_id' in session:
        return redirect('/')
    data={
        "user_id": session['user_id']
    }
    return render_template("account.html", user_magazines = Magazine.get_all_by_user_id(data))

@app.route('/register/process', methods=['POST'])
def registro():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
        "password": request.form['password'],
        "confi": request.form['confi']
    }

    if not User.validacion_registro(data):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data['password'] = pw_hash
    id = User.save(data)
    session['user_id'] = id
    return redirect('/')

@app.route('/update/process', methods=['POST'])
def update():
    data = {
        "id": session['user_id'],
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }

    if not User.validacion_update(data):
         return redirect('/account')

    User.update(data)
    return redirect('/dashboard')



@app.route('/login/process', methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    if len(request.form['password'])<8:
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Email/Contraseña invalido', 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/logout/process', methods=['POST'])
def logout():
    session.pop('user_id')
    return redirect('/')

#Magazine ----------------------------------------------------------------------------------------------

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("dashboard.html", user_session = User.get_by_id(session),
                            all_Magazines = Magazine.get_all_user_magazines())

@app.route('/created/magazine')
def create_magazine():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("created.html")

@app.route('/magazine/<int:id>')
def one_magazine(id):
    if not 'user_id' in session:
        return redirect('/')
    data = {
        "magazine_id": id
    }
    return render_template("one_magazine.html", magazine = Magazine.get_one_user_magazines(data))



@app.route('/created/process', methods=['POST'])
def create_magazine_process():
    data = {
        "name": request.form['name'],
        "contents": request.form['contents'],
        "user_id": session['user_id']
    }
    if len(data['name'])<5 or data['name']=="":
        flash('Name should be at least 2 characters.', 'magazine')
        return redirect ('/created/magazine')
    if len(data['contents'])<5 or data['contents']=="":
        flash('Description should be at least 10 characters.', 'magazine')
        return redirect ('/created/magazine')
    Magazine.save(data)
    return redirect ('/dashboard')

@app.route('/delete/process/<int:id>', methods=['POST'])
def delete_thought(id):
    data = {
        "id": id
    }
    Magazine.destroy(data)
    return redirect ('/account')



#subscription----------------------------------------------------------------------------------------------------------------------------------------------

@app.route('/subscribe/<int:user_id>/<int:magazine_id>', methods=['POST'])
def subscribe(user_id, magazine_id):
    data = {
        "user_id": user_id,
        "magazine_id": magazine_id
    }
    if Subscription.get_one(data):
        flash('You are already subscribed to this magazine', 'sub')
        return redirect ('/dashboard')

    Subscription.save(data)
    return redirect ('/dashboard')





