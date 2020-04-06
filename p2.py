
"""
class Persona: 
    
    def inicializar(self,nom):
        self.nombre=nom 
        
    def mostrar(self):
        print("Nombre: ", self.nombre)
        

persona1 = Persona() 
persona1.inicializar("Ivan")
persona1.mostrar()
"""

class Alumno: 
    
    
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def mostrar(self):
        print(self.nombre,":",self.nota)
    
    def aprobacion(self):
        
        if(self.nota > 4.0):
            print("Aprobado!")

alumno1 = Alumno()
alumno1.inicializar("Ivan Smith",5)
alumno1.mostrar()
alumno1.aprobacion()