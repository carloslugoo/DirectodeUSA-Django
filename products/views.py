from django.shortcuts import render
from seaching.seach import buscar_producto_por_vendedor
import re
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
    
def test(request):
    product_name = 'Apple iPhone 8 Plus'
    buscar_producto_por_vendedor(app_id, seller_username, product_name, iphone8plus, aux, aux, aux)
    print()
    return render(request, 'test.html', {
        'iphone8': iphone8plus,
        })