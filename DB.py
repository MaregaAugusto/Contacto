import pyodbc

class DB():

    def __init__(self, name, server = 'localhost'
        , driver = "MySQL ODBC 8.0 ANSI Driver"):

        self.name = name
        self.server = server
        self.driver = driver
        self.datos = None 

    def conectar(self):
        try:
            self.conexion = pyodbc.connect("DRIVER={"+self.driver+"};"
                                            "Server="+self.server+";"
                                            "DATABASE="+self.name+";"
                                            "UID=root;"
                                            "PWD=root")
            
        except Exception as e:
            print("Error connecting to: ", e)
    
    def cursor(self):
        self.__cursor = self.conexion.cursor()

    def consulta(self,q,v):
        if v:
            self.__cursor.execute(q,v)
        else:
            self.__cursor.execute(q)

    def commit(self, query):
        cont = query.count('SELECT')
        if cont == 0:
            self.conexion.commit()
    
    def close(self):
        self.conexion.close()
    
    def obtenerDatos(self, query):
        cont = query.count('SELECT')
        if cont > 0:
            self.datos = self.__cursor.fetchall()
    
    def ejecutar (self, query, values=None):
        self.conectar()
        self.cursor()
        self.consulta(query, values)
        self.commit(query)
        self.obtenerDatos(query)
        self.close()
        return self.datos

