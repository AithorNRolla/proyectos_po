import abc, math
class Figura(abc.ABC):
    def __init__(self,color):
        self.color=color
    @abc.abstractmethod
    def superficie():
        pass 
class Circulo(Figura):
    def __init__(self, color,radio):
        super().__init__(color)
        self.radio=radio
    def superficie(self):
        return math.pi*self.radio*self.radio

class Triangulo(Figura):
    def __init__(self, color,base,altura):
        super().__init__(color)
        self.base=base
        self.altura=altura
    def superficie(self):
        return math.pi*self.base*self.altura/2
    
#Enunciado del ejercicio 12:
""" Ejercicio: Sistema de gestión de 
empleados 
1. Enunciado 
Una empresa necesita desarrollar una pequeña aplicación para gestionar diferentes tipos 
de empleados. 
Todos los empleados tienen una serie de características comunes, pero el cálculo de su 
salario depende del tipo de empleado. 
Debes implementar las siguientes clases: 
Clase Empleado (superclase) 
Atributos: 
 nombre: nombre del empleado. 
 edad: edad. 
 salario_base: salario base mensual. 
Métodos: 
 mostrar_informacion(): muestra los datos del empleado. 
 calcular_salario(): devuelve el salario base. 
Clase Desarrollador (hereda de Empleado) 
Atributos adicionales: 
 lenguaje: lenguaje de programación que utiliza. 
 horas_extra: número de horas extraordinarias realizadas durante el mes. 
Métodos: 
 Sobrescribir calcular_salario(): devuelve el salario base más 25 € por cada 
hora extra. 
 Sobrescribir mostrar_informacion(): muestra también el lenguaje de 
programación y las horas extra. 
Clase Gerente (hereda de Empleado) 
Atributos adicionales: 
 departamento: departamento que dirige. 
 bonus: cantidad adicional que recibe mensualmente. 
Métodos: 
 Sobrescribir calcular_salario(): devuelve el salario base más el bonus. 
 Sobrescribir mostrar_informacion(): muestra también el departamento y el 
bonus. 
2. Programa principal 
En el programa principal debes realizar las siguientes operaciones: 
1. Crear dos objetos de tipo Desarrollador. 
2. Crear dos objetos de tipo Gerente. 
3. Guardar los cuatro objetos en una única lista. 
4. Recorrer la lista mostrando la información de cada empleado. 
5. Mostrar el salario calculado de cada empleado. 
6. Calcular y mostrar el importe total de las nóminas de la empresa.  """