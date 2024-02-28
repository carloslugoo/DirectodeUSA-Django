from django.shortcuts import render
from seaching.seach import buscar_producto_por_vendedor
import re
# Importa el modelo
from products.models import Producto
from products.models import Actualizacion

from datetime import datetime
# Obtén la fecha actual
fecha_actual = datetime.now()
#Variables de precios:
#aux
aux = []
#iphone 8
iphone8plus = []
#iphone x
iphonex = []
##11
iphone11 = []
iphone11pro = []
iphone11promax = []
##12
iphone12 = []
iphone12pro = []
iphone12promax = []
##13
iphone13 = []
iphone13pro = []
iphone13promax = []
##14
iphone14 = []
iphone14plus = []
iphone14pro = []
iphone14promax = []
##15
iphone15 = []
iphone15plus = []
iphone15pro = []
iphone15promax = []

#Parametros de busqueda:
app_id = 'cARLOSLu-Directod-PRD-a2e2968b1-8eb57663'
seller_username = 'Supplytronics'


# views
def index(request):
    product_name = 'Apple iPhone 8 Plus'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone8plus, aux, aux, aux)
    product_name = 'Apple iPhone X'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphonex, aux, aux, aux)
    product_name = 'Apple iPhone 11'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone11, iphone11pro, iphone11promax, aux)
    product_name = 'Apple iPhone 12'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone12, iphone12pro, iphone12promax, aux)
    product_name = 'Apple iPhone 13'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone13, iphone13pro, iphone13promax, aux)
    product_name = 'Apple iPhone 14'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone14, iphone14plus, iphone14pro, iphone14promax)
    product_name = 'Apple iPhone 15'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone15, iphone15plus, iphone15pro, iphone15promax)
    #print(iphone15pro)
    print(iphone11, iphone11pro, iphone11promax)
    print(iphone12)
    return render(request, 'home.html', {
        'iphone8': iphone8plus,
        'iphonex': iphonex,
        'iphone11': iphone11,
        'iphone11pro': iphone11pro,
        'iphone11promax': iphone11promax,
        'iphone12': iphone12,
        'iphone12pro': iphone12pro,
        'iphone12promax': iphone12promax,
        'iphone13': iphone13,
        'iphone13pro': iphone13pro,
        'iphone13promax': iphone13promax,
        'iphone14': iphone14,
        'iphone14pro': iphone14pro,
        'iphone14plus': iphone14plus,
        'iphone14promax': iphone14promax,
        'iphone15': iphone15,
        'iphone15pro': iphone15pro,
        'iphone15plus': iphone15plus,
        'iphone15promax': iphone15promax,
    })

##product view
iphone = []
iphoneplus = []
iphonepro = []
iphonepromax = []

def comp_modelo(producto): #Comprobar tipo de modelo
    if " Pro" in producto and not " Pro Max" in producto:
        return iphonepro
    elif "Plus" in producto:
        return iphoneplus
    elif " Pro Max" in producto:
        return iphonepromax
    else:
        return iphone
def colores_disponibles(num, modelo):
    colores = []
    if num == 8:
        colores = ["blanco", "oro", "negro"]
    elif num == 10:
        colores = ["blanco", "negro"]
    elif num == 11:
        if modelo == "Pro" or modelo == "Pro Max":
            colores = ["oro", "negro", "blanco"]
        else:
            colores = ["rojo", "negro", "blanco", "violeta"]
    elif num == 12:
        if modelo == "Pro" or modelo == "Pro Max":
            colores = ["oro", "negro", "blanco", "azul"]
        else:
            colores = ["rojo", "negro", "blanco", "azul"]
    elif num == 13:
        if modelo == "Pro" or modelo == "Pro Max":
            colores = ["oro", "negro", "blanco"]
        else:
            colores = [ "negro", "azul", "blanco"]
    elif num == 14:

        if modelo == "Pro" or modelo == "Pro Max":
            
            colores = ["oro", "negro", "blanco"]
        else:
            colores = ["rojo", "negro", "blanco", "violeta"]
    elif num == 15:
        if modelo == "Pro" or modelo == "Pro Max":
            colores = ["negro", "blanco", "azul"]
        else:
            colores = [ "negro", "amarillo",  "rosado", "verde"]
    return colores
    
def verproducto(request, producto):
    
    from urllib.parse import unquote
    # Decodificar el nombre del producto
    producto = unquote(producto)
    print(producto)
    #Obtener modelo para busqueda 
    match = re.search(r'\d+', producto)
    if match:
        # Obtener la posición del número
        posicion_numero = match.start()
        # Obtener la parte de la cadena hasta el número
        num = match.group()
        buscar = producto[:posicion_numero + len(match.group())].strip()
        modelo = producto[posicion_numero + len(match.group()):].strip()
        print(buscar)
        print(num, modelo)
    if producto != "Apple iPhone X":
        num = int(num)
        if num == 11 or num == 12 or num == 13:
            buscar_producto_por_vendedor(app_id, seller_username, buscar, iphone, iphonepro, iphonepromax, aux)
        elif num == 14 or num == 15:
            buscar_producto_por_vendedor(app_id, seller_username, buscar, iphone, iphoneplus, iphonepro, iphonepromax)
    if producto == "Apple iPhone 8 Plus":
        buscar = producto
        buscar_producto_por_vendedor(app_id, seller_username, buscar, iphone, iphonepro, iphonepromax, aux)
        data = iphone
    elif producto == "Apple iPhone X":
        num = 10
        modelo = ""
        buscar = producto
        buscar_producto_por_vendedor(app_id, seller_username, buscar, iphone, iphonepro, iphonepromax, aux)
        data = iphone
    else:
        data = comp_modelo(producto)
    print(data, num, modelo)
    colores = colores_disponibles(num, modelo)
    
    print(colores)
    return render(request, 'productview.html', {
        'producto': producto,
        'data': data,
        'modelo': modelo.lower(),
        'num': num,
        'colores': colores,
    })

def preguntas(request):
    return render(request, 'preguntas.html')
    