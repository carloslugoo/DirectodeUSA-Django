
from ebaysdk.finding import Connection
import requests
from bs4 import BeautifulSoup

#Cotizacion del dia del dolar:
r = requests.get('https://www.cambioschaco.com.py') #Url de donde obtener los datos
soup = BeautifulSoup(r.text, 'html.parser')
cotizacion = soup.find_all('span', class_="sale", limit = 1) #Dolar
#print(cotizacion[0].text.replace('.', ""))
dolar = float(cotizacion[0].text.replace('.', ""))



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
        if item.condition.conditionId == '2020': 
            if product_name in title and not "Locked" in title:
                #print(f"Nombre del artículo: {title}, Precio: {price_value} {currency}")
                if product_name in ["Apple iPhone 11", "Apple iPhone 12", "Apple iPhone 13"]:
                    if product_name + " Pro" in title and not product_name + " Pro Max" in title:
                        modelo2.append([title, price_value])
                    elif product_name + " Pro Max" in title:
                        modelo3.append([title, price_value])
                    elif product_name in title and not product_name + " mini" in title:
                        modelo1.append([title, price_value])
                elif product_name in ["Apple iPhone 14", "Apple iPhone 15"]:
                    #print(f"Nombre del artículo: {title}, Precio: {price_value} {currency}")
                    if product_name + " Pro" in title and not product_name + " Pro Max" in title:
                        modelo3.append([title, price_value])
                    elif product_name + " Pro Max" in title:
                        modelo4.append([title, price_value])
                    elif product_name + " Plus" in title:
                        modelo2.append([title, price_value])
                    elif product_name in title and not product_name + " Pro Max" in title and not product_name + " Pro" in title and not product_name + " Plus" in title:
                        modelo1.append([title, price_value])
                elif product_name in ["Apple iPhone 8 Plus"]:
                    modelo1.append([title, price_value])
                elif product_name in ["Apple iPhone X"]:
                    if "Apple iPhone X" in title:
                        modelo1.append([title, price_value])
    if not modelo1:
        modelo1.append(["Sin existencias!..",  0])
    if not modelo2:
        modelo2.append(["Sin existencias!..",  0])
    if not modelo3:
        modelo2.append(["Sin existencias!..",  0])
    if not modelo2:
        modelo2.append(["Sin existencias!..",  0])    


