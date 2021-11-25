from modeloContacto import *
from vistaContactos import *

class Controlador():
    
    def __init__(self):
        self.vista = Vista()
        x = self.vista.list
        ocontato = contacto(x[0],x[1],x[2])
        ocontato.save()
        print("fin")

x = Controlador()