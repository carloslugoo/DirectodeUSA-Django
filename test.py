from ebaysdk.finding import Connection
import requests
from bs4 import BeautifulSoup
#Cotizacion del dia del dolar:
r = requests.get('https://www.cambioschaco.com.py') #Url de donde obtener los datos
soup = BeautifulSoup(r.text, 'html.parser')
cotizacion = soup.find_all('span', class_="sale", limit = 1) #Dolar
#print(cotizacion[0].text.replace('.', ""))
dolar = float(cotizacion[0].text.replace('.', ""))

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

if __name__ == "__main__":
    #parametros de busqueda:
    app_id = 'cARLOSLu-Directod-PRD-a2e2968b1-8eb57663'
    seller_username = 'Supplytronics'
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
    #Iphone 8 pricing
    product_name = 'Apple iPhone 8 Plus'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone8plus, aux, aux, aux)
    print("8")
    print(iphone8plus)
    print("--------")
    #Iphone 10 pricing
    #Iphone 8 pricing
    product_name = 'Apple iPhone X'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphonex, aux, aux, aux)
    print("X")
    print(iphonex)
    print("--------")
    #Iphone 11 pricing
    product_name = 'Apple iPhone 11'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone11, iphone11pro, iphone11promax, aux)
    print("11")
    print(iphone11)
    print("--------")
    print(iphone11pro)
    print("--------")
    print(iphone11promax)
    #Iphone 12 pricing
    product_name = 'Apple iPhone 12'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone12, iphone12pro, iphone12promax, aux)
    print("12")
    print(iphone12)
    print("--------")
    print(iphone12pro)
    print("--------")
    print(iphone12promax)
    ##Iphone 13 pricing
    product_name = 'Apple iPhone 13'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone13, iphone13pro, iphone13promax, aux)
    print("13")
    print(iphone13)
    print("--------")
    print(iphone13pro)
    print("--------")
    print(iphone13promax)
    ##Iphone 14 pricing
    product_name = 'Apple iPhone 14'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone14, iphone14plus, iphone14pro, iphone14promax)
    print(iphone14)
    print("--------")
    print(iphone14plus)
    print("--------")
    print(iphone14pro)
    print("--------")
    print(iphone14promax)
    product_name = 'Apple iPhone 15'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone15, iphone15plus, iphone15pro, iphone15promax)
    print(iphone15)
    print("--------")
    print(iphone15plus)
    print("--------")
    print(iphone15pro)
    print("--------")
    print(iphone15promax)