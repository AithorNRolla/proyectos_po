
class Empleado:
    def __init__(self,nombre,edad,salario_base):
        self.nombre=nombre
        self._edad=edad
        self.salario_base=salario_base
        
    def calcular_salario(self):
        return self.salario_base
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}|Edad:{self._edad}|Salario:{self.salario_base}€")
    #=========== añadido del profesor ================#
    def edad(self):
        return self._edad #esto es para retornar el valor de la edad. 
    
    def edad(self,valor):
        #if valor<0:
        #    raise ValueError("La edad no puede ser negativa")
        if valor>0:
            self._edad=valor
class Desarrollador(Empleado): #herencia
    def __init__(self, nombre, edad, salario_base,lenguaje,horas_extra):
        super().__init__(nombre, edad, salario_base)
        self.lenguaje=lenguaje
        self.horas_extra=horas_extra
        
    def calcular_salario(self):
        return super().calcular_salario()+(self.horas_extra*25)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lenguaje:{self.lenguaje}|Horas extra:{self.horas_extra}")
        
class Gerente(Empleado): #herencia de nuevo de Empleado. 
    def __init__(self, nombre, edad, salario_base,departamento,bonus):
        super().__init__(nombre,edad,salario_base)
        self.departamento=departamento
        self.bonus=bonus
        
    def calcular_salario(self):
        #super().calcular_salario()+self.bonus (esta línea me sobra)
        return super().calcular_salario()+ self.bonus
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Departamento:{self.departamento}|Bonus:{self.bonus}€")
#Aquí metemos otras movidas inventadas:
#=============================================
dev_1=Desarrollador("Ana", 28, 2200, "Python", 10)
dev_2=Desarrollador("Carlos", 34, 2500, "Java", 4)

ger_1=Gerente("Laura", 42, 3200, "Desarrollo", 600)
ger_2=Gerente("Miguel", 45, 3500, "Sistemas", 800)

lista_1=[dev_1, dev_2, ger_1, ger_2]

total_nominas=0

for emp in lista_1:
    emp.mostrar_informacion()
    salario=emp.calcular_salario()
    print(f"Salario calculado: {salario} €")
    print("-" * 35)
    total_nominas+= salario

print(f"Importe total de las nóminas: {total_nominas} €")

#=============================================
