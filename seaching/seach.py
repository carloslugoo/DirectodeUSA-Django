
from ebaysdk.finding import Connection
import requests
from bs4 import BeautifulSoup
import re

try:
    #Cotizacion del dia del dolar:
    r = requests.get('https://www.cambioschaco.com.py') #Url de donde obtener los datos
    soup = BeautifulSoup(r.text, 'html.parser')
    cotizacion = soup.find_all('span', class_="sale", limit = 1) #Dolar
    #print(cotizacion[0].text.replace('.', ""))
    dolar = float(cotizacion[0].text.replace('.', ""))
except:
    dolar = 7370


# Expresión regular para extraer la capacidad
pattern = r'(\d+)GB'
    
def ordenar_modelo(modelo):
    if not modelo:
        modelo.append(["Sin existencias!..",  0])
    else:
        # Expresión regular para extraer la capacidad
        pattern = r'(\d+)GB'

        # Función para obtener la capacidad
        def obtener_capacidad(nombre):
            match = re.search(pattern, nombre)
            if match:
                return int(match.group(1))
            elif '1TB' in nombre:
                return 1000  # Asignar un valor grande para "1TB" para que vaya al final
            return 0

        modelo = sorted(modelo, key=lambda x: obtener_capacidad(x[0]))

    return modelo

#Funcion de cambiar a guaranies con puntos y todo el chiche
def pre_puntos(precio):
    a = list(precio)
    nr = ""
    cont = len(precio)
    for j in range(0, len(precio)):
        if j > 3:
            nr = nr + "0"
        else:
            nr = nr + a[j]
        cont -= 1
        if cont % 3 == 0 and j != len(precio) - 1:
            nr = nr + "."
    #print(nr)
    return nr

#Funcion de buscar productos
def buscar_producto_por_vendedor(app_id, seller_username, product_name, modelo1, modelo2, modelo3, modelo4):
    
    modelo1.clear()
    modelo2.clear()
    modelo3.clear()
    modelo4.clear()
    
    api = Connection(appid=app_id, config_file=None)

    request_data = {
        'keywords': product_name,
        'itemFilter': [
            {'name': 'Seller', 'value': seller_username},
            {'name': 'Network', 'value': 'Unlocked'},
            {'name': 'Model', 'value': product_name},
            {'name': 'LH_ItemCondition', 'value': '2020'},
            {'name': '_ssn', 'value': seller_username},
            {'name': 'store_name', 'value': seller_username},
            {'name': 'store_cat', 'value': '76876575013'}
        ]
    }

    response = api.execute('findItemsAdvanced', request_data)
    items = response.reply.searchResult.item

    # Manejar la respuesta según tus necesidades
    for item in items:
        title = item.title
        price_value = pre_puntos(str(int(float(item.sellingStatus.currentPrice.value) * dolar)+ 450000))
        # Buscar la capacidad en el título original
        capacidades = ['64GB','128GB', '1TB', '256GB', '512GB']
        capacidad = next((capacidad for capacidad in capacidades if capacidad in title), None)
        if item.condition.conditionId == '2020': 
            if product_name in title and not "Locked" in title:
                #print(f"Nombre del artículo: {title}, Precio: {price_value} {currency}")
                if product_name in ["Apple iPhone 11", "Apple iPhone 12", "Apple iPhone 13"]:
                    if product_name + " Pro" in title and not product_name + " Pro Max" in title:
                        modelo2.append([title, price_value, capacidad])
                    elif product_name + " Pro Max" in title:
                        modelo3.append([title, price_value, capacidad])
                    elif product_name in title and not product_name + " mini" in title:
                        modelo1.append([title, price_value, capacidad])
                elif product_name in ["Apple iPhone 14", "Apple iPhone 15"]:
                    #print(f"Nombre del artículo: {title}, Precio: {price_value} {currency}")
                    if product_name + " Pro" in title and not product_name + " Pro Max" in title:
                        modelo3.append([title, price_value, capacidad])
                    elif product_name + " Pro Max" in title:
                        modelo4.append([title, price_value, capacidad])
                    elif product_name + " Plus" in title:
                        modelo2.append([title, price_value, capacidad])
                    elif product_name in title and not product_name + " Pro Max" in title and not product_name + " Pro" in title and not product_name + " Plus" in title:
                        modelo1.append([title, price_value, capacidad])
                elif product_name in ["Apple iPhone 8 Plus"]:
                    modelo1.append([title, price_value, capacidad])
                elif product_name in ["Apple iPhone X"]:
                    if "Apple iPhone X" in title:
                        modelo1.append([title, price_value, capacidad])
    # Llamadas a la función para ordenar los modelos
    modelo1 = ordenar_modelo(modelo1)
    modelo2 = ordenar_modelo(modelo2)
    modelo3 = ordenar_modelo(modelo3)
    modelo4 = ordenar_modelo(modelo4)

