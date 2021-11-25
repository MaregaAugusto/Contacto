from DB import *

class contacto():

    DB = DB(name="contacto")
    tableName = 'contacto'

    def __init__(self, nombre, telefono, email, id = None):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def save(self):
        query= "INSERT INTO "+self.tableName+"(nombre, telefono, email) VALUES (?,?,?)"
        values= (self.nombre, self.telefono, self.email)
        self.DB.ejecutar(query, values)



