class Empleado:
    # 1. ATRIBUTO DE CLASE (Compartido por TODOS los objetos de este molde)
    empresa = "Tech Data S.L."

    # 2. CONSTRUCTOR (Guarda los datos únicos de CADA objeto)
    def __init__(self, nombre, salario, departamento="General"):
        self.nombre = nombre             # Atributo obligatorio
        self.salario = salario           # Atributo obligatorio
        self.departamento = departamento # Atributo con valor por defecto

    # 3. MÉTODO NORMAL (Acción que lee o modifica datos del objeto)
    def subir_salario(self, porcentaje):
        self.salario += self.salario * (porcentaje / 100)

    # 4. MÉTODO __str__ (Define qué se imprime al hacer print(objeto))
    def __str__(self):
        return f"👤 {self.nombre} | {self.departamento} | {self.salario:.2f}€"

#====================== COMO USAR LA PLANTILLA DE ARRIBA =============================#
# A. Crear objetos (Instanciar)
emp_1 = Empleado("Ana", 28000, "IT")
emp_2 = Empleado("Luis", 24000) # Usa departamento="General" por defecto

# B. Leer y modificar atributos directamente
print(emp_1.nombre)        # Ana
emp_2.departamento = "RRHH"

# C. Llamar a un método (Python pasa 'self' automáticamente por detrás)
emp_1.subir_salario(10)

# D. Imprimir el objeto (Llama automáticamente a __str__)
print(emp_1)               # 👤 Ana | IT | 30800.00€

#======================================== EXTRA ======================================#
# Manager HEREDA todo de Empleado (nombre, salario, subir_salario...)
class Manager(Empleado):
    def __init__(self, nombre, salario, departamento, equipo_a_cargo):
        # super() llama al __init__ del padre para no repetir código
        super().__init__(nombre, salario, departamento)
        self.equipo_a_cargo = equipo_a_cargo # Dato nuevo exclusivo de Manager

    def mostrar_equipo(self):
        print(f"{self.nombre} dirige a {self.equipo_a_cargo} personas.")

# Uso:
jefa = Manager("Laura", 45000, "Datos", 6)
jefa.subir_salario(5)      # Método heredado de Empleado
jefa.mostrar_equipo()      # Método propio de Manager
