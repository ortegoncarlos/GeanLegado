#encoding:utf-8
from random import choice
frases  =   ['No alabes a el hombre por su bello aspecto,ni desprecies a alguno por lo que parece',
             'La vida es aquello que te va sucediendo mientras te empeñas en hacer  otros planes',
             'Dar el ejemplo no es la principal manera de influir sobre los demás, sino es la única'
             ]

def mostrarfrase(request):
    return {'frase':choice(frases)}