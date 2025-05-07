import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required,current_user
from werkzeug.utils import secure_filename
from app.models.users import Users
from app import db  # Importamos `app` para acceder a la configuración


bp = Blueprint('users', __name__)
@bp.before_request
@login_required
def before_request():
    pass
# Configuración para la subida de imágenes
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','jfif','webp','bmp','ico'}
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'static\imagenes')  # Ruta absoluta

# Verificar que la carpeta existe, si no, crearla
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Verifica si la extensión del archivo es válida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/users')
def index():
    data = Users.query.all()
    if current_user.tipousu == 1 : #administrador
        return render_template('usuarios/index.html', data=data,datausu=current_user)
    else:
        return redirect(url_for('auth.dashboard')) 
@bp.route('/users/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        #print("📩 Datos recibidos:", request.form)
        #print("📂 Archivos recibidos:", request.files)

        nameuser = request.form['nameuser']
        clave = request.form['claveuser']
        vclave = request.form['vclaveuser']
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        telefono = request.form['telefono']
        correo = request.form['correo']
        tipousu = request.form['tipousu']
        # Usuario con imagen predeterminada
        new_user = Users(passworduser=clave, nameuser=nameuser, imgper="usuario.png",nombre=nombre,
                         cedula=cedula,telefono=telefono,correo=correo,tipousu=tipousu)

        # Verificar si 'img1' está en los archivos recibidos
        #if 'img1' not in request.files:
            #flash("⚠ No se encontró la imagen en la solicitud", "error")
            #return redirect(request.url)

        file = request.files['img1']

        #if file.filename == '':
            #flash("⚠ No se seleccionó ninguna imagen", "error")
            #return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Nombre seguro
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            
            print(f"📁 Guardando imagen en: {filepath}")  # Depuración

            try:
                file.save(filepath)  # Guarda la imagen
                print(f"✅ Imagen {filename} guardada correctamente")
                new_user.imgper = filename  # Guarda solo el nombre en la BD
            except Exception as e:
                print(f"❌ Error al guardar la imagen: {str(e)}")
                flash(f"❌ Error al guardar la imagen: {str(e)}", "error")

        # Guardar usuario en la base de datos
        try:
            db.session.add(new_user)
            db.session.commit()
            flash(f"✅ Usuario creado correctamente")
        except Exception as e:
            flash(f"Error durante la Creacion del Usuario:  {str(e)}", "danger")
            flash("Error en la base de datos add Usuarios")
        return redirect(url_for('users.index'))  # Redirigir a la lista de usuarios

    return render_template('usuarios/add.html')




@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user = Users.query.get_or_404(id)

    if request.method == 'POST':
        user.nameuser = request.form['nameuser']
        user.nombre = request.form['nombre']
        user.cedula = request.form['cedula']
        user.telefono = request.form['telefono']
        user.correo = request.form['correo']
        user.tipousu = request.form['tipousu']
        file = request.files['img1']

        #if file.filename == '':
            #flash("⚠ No se seleccionó ninguna imagen", "error")
            #return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Nombre seguro
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            
            print(f"📁 Guardando imagen en: {filepath}")  # Depuración

            try:
                file.save(filepath)  # Guarda la imagen
                print(f"✅ Imagen {filename} guardada correctamente")
                user.imgper = filename  # Guarda solo el nombre en la BD
            except Exception as e:
                print(f"❌ Error al guardar la imagen: {str(e)}")
                flash(f"❌ Error al guardar la imagen: {str(e)}", "error")

        try:
            db.session.commit()
            flash(f"✅ Usuario Actualizado correctamente")
        except Exception as e:
            flash("Error en la base de datos edit Usuarios")     
        return redirect(url_for('users.index'))

    return render_template('usuarios/edit.html', datauser=user)


@bp.route('/editperf/<int:id>', methods=['GET', 'POST'])
def editperf(id):
    user = Users.query.get_or_404(id)

    if request.method == 'POST':
        user.nameuser = request.form['nameuser']
        user.nombre = request.form['nombre']
        user.cedula = request.form['cedula']
        user.telefono = request.form['telefono']
        user.correo = request.form['correo']
        user.tipousu = request.form['tipousu']
        file = request.files['img1']

        #if file.filename == '':
            #flash("⚠ No se seleccionó ninguna imagen", "error")
            #return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Nombre seguro
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            
            print(f"📁 Guardando imagen en: {filepath}")  # Depuración

            try:
                file.save(filepath)  # Guarda la imagen
                print(f"✅ Imagen {filename} guardada correctamente")
                user.imgper = filename  # Guarda solo el nombre en la BD
            except Exception as e:
                print(f"❌ Error al guardar la imagen: {str(e)}")
                flash(f"❌ Error al guardar la imagen: {str(e)}", "error")

        try:
            db.session.commit()
            flash(f"✅ Usuario Actualizado correctamente")
        except Exception as e:
            flash("Error en la base de datos edit Usuarios")     
        return redirect(url_for('auth.dashboard'))

    return render_template('usuarios/editperf.html', datauser=user)



@bp.route('/delete/<int:id>')
def delete(id):
    user = Users.query.get_or_404(id)
    db.session.delete(user)
    try:
        db.session.commit()
        flash(f"✅ Usuario Eliminado correctamente")
    except Exception as e:
        flash(f"Error durante la Eliminacion del Usuario:  {str(e)}", "danger")
        flash("Error en la base de datos delete Usuarios")
    return redirect(url_for('users.index'))
























