#Crear una subclase de list para el almacenamiento de números con las siguientes características:
#Incluirá los métodos:
# sum(). Devuelve la suma de los números almacenados
# mean(). Devuelve la media de los números almacenados
#Además de esos métodos, recibirá eñ constructor un parámetro booleano que en caso de ser True, 
#impedirá que se añadan números repetidos. 

#BLOQUE 1
class Lista_Numerica(list): #Constructor. 
    def __init__(self, sin_repetidos=False):
        super().__init__() #esto es la lista heredada
        self.sin_repetidos=sin_repetidos #Esto debe de guardar para true o false. 
    
    def append(self, numero):
        if self.sin_repetidos and numero in self: #esto nos indica hacia la lista (true/false)
            print(f"El número {numero} ya existe, no se añadirá")
        else:
            super().append(numero) #append original de la lista. 
#BLOQUE 2
    def sum(self):
        total=0
        for numero in self:     # Recorremos cada elemento de la propia lista (self)
            total+=numero
        return total

    def mean(self):
        if len(self)==0:      # Evitamos dividir entre 0 si la lista está vacía
            return 0
        return self.sum()/len(self)   # Reutilizamos nuestro propio método self.sum()
#BLOQUE 3
lista_1=Lista_Numerica(False) #aquí permitimos repetidas
lista_1.append(10)
lista_1.append(10)
lista_1.append(20)
print(lista_1)          
print(lista_1.sum())     
print(lista_1.mean())    
#apartir de aquí ya no permitimos repetidas:
lista_2=Lista_Numerica(True)
lista_2.append(10)
lista_2.append(10)       # Salta el aviso y no lo mete!!!
lista_2.append(20)
print(lista_2)          
print(lista_2.sum())     
print(lista_2.mean())