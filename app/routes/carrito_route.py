import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, make_response,send_file,current_app
from flask_login import login_required,current_user
from werkzeug.utils import secure_filename
from app.models.carrito import Carrito
from app.models.productos import Productos
from app.models.categorias import Categorias
from app.models.ventas_t import Ventas_t
from app.models.ventas_d import Ventas_d
from app import db
#from weasyprint import HTML
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image as RLImage
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import red
from reportlab.lib.enums import TA_CENTER
from io import BytesIO
from datetime import datetime, timedelta
import pytz
import base64
import requests
import qrcode
import io
import base64

bp = Blueprint('carrito', __name__)

# coloca como predeterminada la fecha de colombia 
colombia_tz = pytz.timezone('America/Bogota')
# hacer que todas las rutas necesiten el logeo
@bp.before_request
@login_required
def before_request():
    pass


#formulario para generar la vista para agregar al Carrito
@bp.route('/carrito')
def index():
    data = Carrito.query.all()
    return render_template('carrito/addcarrito.html', data=data,datausu=current_user)

# adicionar al carrito
@bp.route('/carrito/add/<int:id>', methods=['GET', 'POST'])
@login_required
def add(id):
    dataPro = Productos.query.get_or_404(id)
    iduser= current_user.iduser
    dataexit = Carrito.query.filter_by(idproducto=id,iduser= iduser).first()
    imagenes_validas = []
    for i in range(1, 5):
        img = getattr(dataPro, f'img{i}')
        if img and img != 'productos.png':
            imagenes_validas.append(img)


    if request.method == 'POST':

        idproducto= request.form['idproducto']
        cantidad = request.form['cantidad']
        print(dataexit)
        if dataexit:
            dataexit.cantidad = cantidad
        else:
            new_carrito = Carrito(idproducto=idproducto, iduser=iduser, cantidad=cantidad)
            db.session.add(new_carrito)

        db.session.commit()
        return jsonify({'success': True, 'message': '✅ Producto agregado al carrito correctamente'})
    
    return render_template('carrito/addcarrito.html', dataPro= dataPro,dataexit=dataexit,imagenes=imagenes_validas)


@bp.route('/carrito/list')
def listarcarrito():
    dataexit = Carrito.query.filter_by(iduser=current_user.iduser).all()

    for itemcarrito in dataexit:
        try:
            itemcarrito.productos.pordes = itemcarrito.productos.pordes or 0
            itemcarrito.productos.precio = itemcarrito.productos.precio or 0
            itemcarrito.productos.descuento = itemcarrito.productos.descuento or 0
            itemcarrito.productos.iva= itemcarrito.productos.iva or 0
        except AttributeError:
            # Si el carrito no tiene productos, simplemente seguir
            continue

    return render_template('carrito/ver_carrito.html', data=dataexit)

@bp.route('/carrito/comprar', methods=['GET', 'POST'])
def comprar():
    try:
        selected_items = request.form.getlist('selected_items')
        if not selected_items:
            flash("No seleccionaste ningún producto.", "warning")
            return redirect(url_for('carrito.listarcarrito'))

        detalles = []
        subtotal_general = 0
        total_general = 0
        descuento_total = 0
        iva_total = 0
        fecha = datetime.now(colombia_tz).strftime('%Y-%m-%d')

        for id_producto in selected_items:
            producto = Productos.query.get(id_producto)
            cantidad_str = request.form.get(f'cantidad[{id_producto}]')
            producto.pordes = producto.pordes or 0
            producto.precio =  producto.precio or 0
            producto.descuento =  producto.descuento or 0
            producto.iva=  producto.iva or 0
      
            if producto and cantidad_str:
                cantidad = int(cantidad_str)
                subpro = cantidad * producto.precio
                descuentopro = cantidad * producto.descuento
                subtotal_producto = subpro - descuentopro
                ivapro = subtotal_producto * (producto.iva / 100)
                total_producto = subtotal_producto + ivapro

                subtotal_general += subpro
                total_general += total_producto
                descuento_total += descuentopro
                iva_total += ivapro
                producto.stock = int(producto.stock) -cantidad
                detalles.append(Ventas_d(
                    idproducto=producto.idproducto,
                    precio=producto.precio,
                    cantidad=cantidad,
                    descuento=descuentopro,
                    iva=ivapro,
                    total=subpro,
                    fecha=fecha
                ))

        if detalles:
            new_venta_t = Ventas_t(
                iduser=current_user.iduser,
                fecha=fecha,
                f_vto=datetime.now(colombia_tz) + timedelta(days=30),
                observacion=request.form.get('observacion', ''),
                subtotal=subtotal_general,
                iva=iva_total,
                descuento=descuento_total,
                total=total_general
            )
            db.session.add(new_venta_t)
            db.session.commit()

            for d in detalles:
                d.idventa = new_venta_t.idventa
                db.session.add(d)
            db.session.commit()

            # Eliminar del carrito
            for id_producto in selected_items:
                carritos = Carrito.query.filter_by(idproducto=id_producto, iduser=current_user.iduser).all()
                for carrito in carritos:
                    db.session.delete(carrito)
            db.session.commit()
            
            flash("Compra realizada con éxito.", "success")
        else:
            flash("No se encontraron productos válidos.", "warning")

    except Exception as e:
        db.session.rollback()
        flash(f"Error durante la compra: {str(e)}", "danger")

    return redirect(url_for('carrito.vercompras'))

@bp.route('/carrito/ver_compra')
def vercompras():
    dataventas_t = Ventas_t.query.filter_by(iduser= current_user.iduser).all()

    return render_template('carrito/ver_compras.html', data=dataventas_t)

@bp.route('/carrito/detalleventa/<int:id>', methods=['GET', 'POST'])
def detalleventa(id):
    dataventas_d = Ventas_d.query.filter_by(idventa=id).all()
    dataventas_t = Ventas_t.query.filter_by(iduser= current_user.iduser).all()
    return render_template('carrito/ver_compras.html', datad=dataventas_d, data=dataventas_t)
    

import qrcode
from PIL import Image as PILImage 
from reportlab.lib.utils import ImageReader
from io import BytesIO

from flask import current_app as app, render_template, flash, redirect, url_for
import requests, qrcode, io, base64

# URL exacta de tu entorno sandbox (o prod)
GENERATE_QR_URL = "https://sandbox.conecta.nequi.com.co/collect/v1.0/generate/qr"

@bp.route('/carrito/generar_qr/<int:venta_id>')
def generar_qr(venta_id):
    venta = Ventas_t.query.get_or_404(venta_id)
    # Construir payload con monto en centavos
    payload = {
      "RequestMessage": {
        "RequestHeader": {
          "Channel": "PQR03-C001",
          "MessageID": str(venta_id),
          "ClientID": "3045822360",
          "Destination": {
            "ServiceName": "PaymentsService",
            "ServiceOperation": "generateCodeQR",
            "ServiceRegion": "C001",
            "ServiceVersion": "1.0.0"
          }
        },
        "RequestBody": {
          "amount": int(venta.total * 100),
          "currency": "COP",
          "reference": str(venta_id)
        }
      }
    }

    # Cabeceras con token y client id
    token = get_nequi_token()  # tu función que obtiene el Bearer
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "ClientId": "3045822360"
    }

    try:
        resp = requests.post(GENERATE_QR_URL, json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        qr_value = data["ResponseMessage"]["ResponseBody"]["any"]["generateCodeQRRS"]["qrValue"]

        # Generar imagen QR
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data(qr_value); qr.make(fit=True)
        img = qr.make_image()
        buffer = io.BytesIO(); img.save(buffer, format="PNG")
        qr_b64 = base64.b64encode(buffer.getvalue()).decode()

        flash("QR de pago generado correctamente.", "success")
        return render_template('carrito/mostrar_qr.html', qr_b64=qr_b64, venta_id=venta_id)

    except requests.HTTPError as e:
        # Muestra el body para debug
        app.logger.error(f"Nequi 403 Body: {resp.text}")
        flash(f"Error al generar QR: {e}", "danger")
        return redirect(url_for('carrito.vercompras'))

import os
import requests

# Variables de entorno — puedes ponerlas en .env o en tu entorno de ejecución
NEQUI_CLIENT_ID     = os.getenv("NEQUI_CLIENT_ID")
NEQUI_CLIENT_SECRET = os.getenv("NEQUI_CLIENT_SECRET")
# Punto de token para sandbox o prod según corresponda:
NEQUI_OAUTH_URL     = "https://sandbox.conecta.nequi.com.co/oauth/v3/token"

def get_nequi_token():
    """
    Llama al endpoint OAuth2 Client Credentials de Nequi Conecta
    y devuelve el access_token para usar en las siguientes peticiones.
    """
    payload = {
        "grant_type":    "client_credentials",
        "client_id":     NEQUI_CLIENT_ID,
        "client_secret": NEQUI_CLIENT_SECRET
    }
    headers = {
        "Content-Type": "application/json"
    }

    resp = requests.post(NEQUI_OAUTH_URL, json=payload, headers=headers)
    # Si algo falla (credenciales erróneas, URL mal), lanzará excepción HTTPError
    resp.raise_for_status()

    data = resp.json()
    # Normalmente Nequi devuelve {"access_token": "...", "expires_in": 3600, ...}
    token = data.get("access_token")
    if not token:
        raise RuntimeError(f"No se recibió access_token: {data}")

    return token

def generar_qr_nequi(numero_cuenta, monto, referencia="Pago factura ComPuMotos"):
    """
    Genera un código QR para realizar pagos a través de Nequi.
    
    Args:
        numero_cuenta (str): Número de cuenta Nequi.
        monto (float): Monto del pago.
        referencia (str): Referencia o mensaje adicional.
        
    Returns:
        BytesIO: Imagen del código QR en formato PNG.
    """
    # Crear el contenido del QR
    contenido = f"NEQUI:{numero_cuenta}|MONTO:{monto}|REF:{referencia}"
    
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(contenido)
    qr.make(fit=True)
    
    # Crear una imagen del QR
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar la imagen en un objeto BytesIO para usarla en ReportLab
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    
    return buffer

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.lib.units import inch
from io import BytesIO


@bp.route('/carrito/imp_fact/<int:id>', methods=['GET', 'POST'])
def imp_fact(id):
    datacli = current_user
    dataventas_t = Ventas_t.query.filter_by(idventa=id).first()
    dataventas_d = Ventas_d.query.filter_by(idventa=id).all()
    
    datos_factura = {
        'cliente': 'Cliente Ejemplo',
        'direccion': 'Av. Siempre Viva 742',
        'fecha': datetime.now().strftime("%d/%m/%Y"),
        'numero': 'FAC-2023-001',
        'items': [
            {'descripcion': 'Producto 1', 'cantidad': 2, 'precio_unitario': 150.00, 'total': 300.00},
            {'descripcion': 'Producto 2', 'cantidad': 8, 'precio_unitario': 150.00, 'total': 300.00},
            {'descripcion': 'Producto 3', 'cantidad': 4, 'precio_unitario': 150.00, 'total': 300.00},
            {'descripcion': 'Servicio Técnico', 'cantidad': 1, 'precio_unitario': 500.00, 'total': 500.00}
        ],
        'subtotal': 800.00,
        'iva': 128.00,
        'total': 928.00
    }

    pdf = generar_factura(datos_factura,datacli,dataventas_t,dataventas_d)
    return send_file(
        pdf,
        mimetype='application/pdf',
        download_name='factura.pdf',
        as_attachment=True
    )

def generar_factura(datos_factura,datacli, dataventas_t, dataventas_d):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=36, leftMargin=36,
                            topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    estilo_normal = styles['Normal']
    estilo_titulo = ParagraphStyle('Titulo', parent=styles['Heading1'], alignment=TA_CENTER, fontSize=18, textColor=colors.darkblue)
    estilo_subt = ParagraphStyle('Subt', parent=styles['Heading3'], alignment=TA_LEFT, fontSize=10)
    estilo_dcha = ParagraphStyle('Derecha', parent=styles['Normal'], alignment=TA_RIGHT)
    estilo_encabezado = ParagraphStyle('Enc', parent=styles['Heading2'], alignment=TA_LEFT)

    story = []

    # 1. Encabezado principal con dos columnas
    header_data = [
        [
        Paragraph(
            "<b>TALLER Y ALMACÉN DONDE EULISES</b><br/>NIT: 1101753808-9<br/>"
            "ANDRES PEÑA VELASCO<br/>CARRERA 6 5 A 126<br/>Vélez Santander<br/>"
            "CEL: 304 582 2360<br/>EMAIL: andetazz87@gmail.com",
            estilo_subt),
        Paragraph(
            "<b>RÉGIMEN SIMPLIFICADO</b><br/>"
            "Facturación por computador Res. DIAN No. 40000166098<br/>"
            f"<b>Factura Nro:</b> <font color='red'>{dataventas_t.idventa}</font><br/>"
            f"Fecha: {dataventas_t.fecha} &nbsp;&nbsp;&nbsp; Fecha Vto: {dataventas_t.f_vto}<br/>"
            f"Observaciones: {dataventas_t.observacion}",
            estilo_subt)
        ]
    ]
  
    header = Table(header_data, colWidths=[3.5*inch, 3.5*inch])
    header.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,0), 1, colors.black),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ]))
    story.append(header)
    story.append(Spacer(1, 12))

    # 2. Datos del cliente
    cli_data = [
        ['Señor(es):', datacli.nombre],
        ['Correo:', datacli.correo],
        ['C.C. / NIT:', datacli.cedula],
        ['Teléfono:', datacli.telefono]
    ]
    cli_tbl = Table(cli_data, colWidths=[1.2*inch, 6*inch])
    cli_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.lightgrey),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica',),
        ('FONTSIZE', (0,0), (-1,-1), 9),
    ]))
    story.append(cli_tbl)
    story.append(Spacer(1, 12))

    # 3. Detalle de productos
    story.append(Paragraph("Detalle de Venta", estilo_subt))
    prod_data = [['CONCEPTO','CANTIDAD','Vr. UNIT.','Descuento','IVA','Vr. TOTAL']]
    for item in dataventas_d:
        nombre_corto = item.productos.nombre.upper()
        if len(nombre_corto) > 60:
            nombre_corto = nombre_corto[:57] + "..."
        prod_data.append([
        Paragraph(nombre_corto, estilo_normal),
            str(item.cantidad),
            f"{item.precio:,.0f}",
            f"{item.descuento:,.0f}",
            f"{item.iva:,.0f}",
            f"{item.total:,.0f}"
        ])
    prod_tbl = Table(prod_data, colWidths=[3*inch, 0.8*inch, 1*inch, 1*inch, 0.8*inch, 1*inch])
    prod_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (1,1), (-1,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
    ]))
    story.append(prod_tbl)
    story.append(Spacer(1, 12))

    # 4. Totales al pie
    totales = [
        ['','','', 'Subtotal:', f"${dataventas_t.subtotal:,.0f}"],
        ['','','', 'Descuento:', f"${dataventas_t.descuento:,.0f}"],
        ['','','', 'IVA:', f"${dataventas_t.iva:,.0f}"],
        ['','','', 'Total:', f"${dataventas_t.total:,.0f}"]
    ]
    tot_tbl = Table(totales, colWidths=[3*inch, 0.8*inch, 1.5*inch, 1.2*inch])
    tot_tbl.setStyle(TableStyle([
        ('ALIGN', (2,0), (-1,-1), 'RIGHT'),
        ('FONTNAME', (2,0), (2,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,0), (-1,0), 4),
    ]))
    story.append(tot_tbl)
    story.append(Spacer(1, 24))

    # 5. Monto en letras
    tot_letras = numero_a_pesos(dataventas_t.total).upper()
    story.append(Paragraph(f"Son: {tot_letras}", estilo_subt))
    story.append(Spacer(1, 24))

    # 6. Código QR Nequi
    # suponiendo que `generar_qr_nequi()` te devuelve un BytesIO con la imagen
    qr_buffer = generar_qr_nequi("3126566205", int(dataventas_t.total * 100))
    qr_img = RLImage(qr_buffer, width=1.5*inch, height=1.5*inch)
    qr_tbl = Table([[qr_img, Paragraph("Escanea este código QR para pagar", estilo_normal)]],
                   colWidths=[1.6*inch, 5.0*inch])
    qr_tbl.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (1,0), (1,0), 12),
    ]))
    story.append(qr_tbl)
    story.append(Spacer(1, 24))

    # 7. Pie de página
    story.append(Paragraph("Gracias por su compra en ComPuMotos!", estilo_subt))
    story.append(Paragraph("La presente factura de Venta se asimila en sus efectos legales a la letra de cambio.", estilo_normal))

    doc.build(story)
    buffer.seek(0)
    return buffer

def numero_a_pesos(numero):
    """
    Convierte un número en su representación en letras con formato de pesos.
    
    Args:
        numero (float o int): El número a convertir.
        
    Returns:
        str: Representación del número en letras con formato de pesos.
    """

    # Diccionarios para las palabras básicas
    unidades = ["", "un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = {
        10: "diez",
        11: "once",
        12: "doce",
        13: "trece",
        14: "catorce",
        15: "quince",
        16: "dieciséis",
        17: "diecisiete",
        18: "dieciocho",
        19: "diecinueve",
        21: "veintiuno",
        22: "veintidós",
        23: "veintitrés",
        24: "veinticuatro",
        25: "veinticinco",
        26: "veintiséis",
        27: "veintisiete",
        28: "veintiocho",
        29: "veintinueve"
    }
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    def convertir_parte_entera(n):
        """Convierte la parte entera del número."""
        if n == 0:
            return "cero"
        elif n < 10:
            return unidades[n]
        elif n < 20:
            return especiales[n]
        elif n < 30 and n in especiales:
            return especiales[n]
        elif n < 100:
            return f"{decenas[n // 10]} {unidades[n % 10]}".strip()
        elif n < 1000:
            return f"{centenas[n // 100]} {convertir_parte_entera(n % 100)}".strip()
        elif n < 1000000:
            miles = n // 1000
            resto = n % 1000
            if miles == 1:
                return f"mil {convertir_parte_entera(resto)}".strip()
            else:
                return f"{convertir_parte_entera(miles)} mil {convertir_parte_entera(resto)}".strip()
        elif n < 1000000000:
            millones = n // 1000000
            resto = n % 1000000
            if millones == 1:
                return f"un millón {convertir_parte_entera(resto)}".strip()
            else:
                return f"{convertir_parte_entera(millones)} millones {convertir_parte_entera(resto)}".strip()
        else:
            return "Número demasiado grande"

    def convertir_parte_decimal(n):
        """Convierte la parte decimal del número."""
        if n == 0:
            return ""
        else:
            return f"{convertir_parte_entera(n)} centavos"

    # Separar la parte entera y decimal
    if isinstance(numero, float):
        parte_entera, parte_decimal = divmod(numero, 1)
        parte_decimal = int(round(parte_decimal * 100))  # Redondear a dos decimales
    else:
        parte_entera, parte_decimal = numero, 0

    # Convertir cada parte
    texto_entero = convertir_parte_entera(int(parte_entera))
    texto_decimal = convertir_parte_decimal(parte_decimal)

    # Combinar ambas partes
    if texto_decimal:
        return f"{texto_entero} pesos con {texto_decimal}"
    else:
        return f"{texto_entero} pesos"
