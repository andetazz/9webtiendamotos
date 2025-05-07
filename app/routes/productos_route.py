import os
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required,current_user
from werkzeug.utils import secure_filename
from app.models.productos import Productos
from app.models.categorias import Categorias
from app import db
import uuid  # Para generar nombres aleatorios únicos
bp = Blueprint('productos', __name__)

# hacer que todas las rutas necesiten el logeo
@bp.before_request
@login_required
def before_request():
    pass

# Configuración para la subida de imágenes
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','jfif','webp','bmp','ico'}
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'imagenes')  # Ruta absoluta

# Verificar que la carpeta existe, si no, crearla
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Verifica si la extensión del archivo es válida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def subir_imagen(img, img_actual=None):
    """Guarda una imagen con un nombre aleatorio y elimina la anterior si existe."""

    if img and allowed_file(img.filename):
        try:
            # Obtener extensión del archivo
            ext = img.filename.rsplit('.', 1)[1].lower()
            # Generar nombre único aleatorio
            nuevo_nombre = f"{uuid.uuid4().hex}.{ext}"
            # Ruta completa donde se guardará
            filepath = os.path.join(UPLOAD_FOLDER, nuevo_nombre)

            # Guardar imagen nueva
            img.save(filepath)
            print(f"✅ Imagen guardada: {filepath}")

            # Eliminar la imagen anterior si no es la predeterminada
            if img_actual and img_actual != "productos.png":
                path_anterior = os.path.join(UPLOAD_FOLDER, img_actual)
                if os.path.exists(path_anterior):
                    os.remove(path_anterior)
                    print(f"🗑 Imagen anterior eliminada: {path_anterior}")

            return nuevo_nombre  # Devuelve el nuevo nombre

        except Exception as e:
            flash(f"❌ Error al guardar la imagen: {str(e)}", "error")
            print(f"❌ Error al guardar la imagen: {str(e)}")

    # Si no se subió nueva imagen o hubo error, mantener la anterior
    return img_actual or "productos.png"

@bp.route('/productos')
def index():
    data = Productos.query.all()
    datacategorias = Categorias.query.all()
    print(datacategorias)
    return render_template('productos/index.html', data=data,datausu=current_user,datacategorias=datacategorias)

@bp.route('/productos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        nombre = request.form['nombre'].upper()
        stock = request.form['stock']
        precio = request.form['precio'] 
        pordes = request.form['pordes']
        descuento = request.form['descuento']
        iva = request.form['poriva']
        descripcion = request.form['descripcion']
        idcategoria = request.form['idcategoria']
        new_Producto =  Productos(nombre=nombre,stock=stock,precio=precio,pordes=pordes,
                                  iva=iva,descuento=descuento,descripcion=descripcion,idcategoria=idcategoria)
       
        # Subir imagen si está en la solicitud
        img1 = subir_imagen(request.files.get('img1'))
        new_Producto.img1= img1
        img2 = subir_imagen(request.files.get('img2'))
        new_Producto.img2= img2
        img3 = subir_imagen(request.files.get('img3'))
        new_Producto.img3= img3
        img4 = subir_imagen(request.files.get('img4'))
        new_Producto.img4= img4
        db.session.add(new_Producto)
        try:
            db.session.commit()
            flash(f"✅ Registro Guardado: ")
        except:
            print("Error en la base de datos add productos")
        return redirect(url_for('productos.index'))
    catdata= Categorias.query.all()
    return render_template('productos/add.html',catdata=catdata,)

@bp.route('/productos/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    producto = Productos.query.get_or_404(id)  
    if request.method == 'POST':

        producto.nombre = request.form['nombre'].upper()
        producto.stock = request.form['stock']
        producto.precio = request.form['precio']
        producto.pordes = request.form['pordes']
        producto.descuento = request.form['descuento'] 
        producto.iva = request.form['poriva']
        producto.descripcion = request.form['descripcion']
        producto.idcategoria = request.form['idcategoria']

        # Subir la nueva imagen y eliminar la anterior
        if 'img1' in request.files and request.files['img1'].filename:
            producto.img1 = subir_imagen(request.files['img1'], producto.img1)
        if 'img2' in request.files and request.files['img2'].filename:
            producto.img2 = subir_imagen(request.files['img2'], producto.img2)
        if 'img3' in request.files and request.files['img3'].filename:
            producto.img3 = subir_imagen(request.files['img3'], producto.img3)
        if 'img4' in request.files and request.files['img4'].filename:
            producto.img4 = subir_imagen(request.files['img4'], producto.img4)
        try:
            db.session.commit()
            flash(f"✅ Registro Actualizado: ")
        except:
            print("Error en la base de datos edit productos")
        return redirect(url_for('productos.index'))

    categorias= Categorias.query.all() 
    return render_template('productos/edit.html',catdata=categorias, Productodata=producto)

@bp.route('/productos/delete/<int:id>')
def delete(id):
    producto = Productos.query.get_or_404(id)

    # Eliminar imágenes si existen (opcional)
    for img in [producto.img1, producto.img2, producto.img3, producto.img4]:
        if img and img != "productos.png":
            ruta_img = os.path.join(UPLOAD_FOLDER, 'static', 'imagenes', img)
            if os.path.exists(ruta_img):
                os.remove(ruta_img)

    db.session.delete(producto)
    try:
        db.session.commit()
        flash("✅ Producto eliminado con éxito", "success")
    except:
        print("Error en la base de datos Eliminar Producto")
    return redirect(url_for('productos.index'))