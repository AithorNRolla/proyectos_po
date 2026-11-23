class Cuenta:
    def __init__(self,saldo): #constructor
        self.saldo=saldo
    def ingresar(self,cantidad): #metodo
        self.saldo+=cantidad
    def extraer(self,cantidad):
        self.saldo-=cantidad
        
#Crear la clase CuentaLimitada, que será una subclase de cuenta
#y tendrá un atributo con la cantidad máxima a extraer
#Si el valor del atributo es 0, no hay límite. Si es mayor que 0, ese será el límite. 
#No se podrá extraer más dinero que el que marque el límite. 

class CuentaLimitada(Cuenta):                         # 1. Conecta con Cuenta
    def __init__(self,saldo,limite):                  # 2. Pide saldo y limite
        super().__init__(saldo)                       # Guardamos saldo
        self.limite=limite                            # Guardamos límite
        
    def extraer(self,cantidad):                       # 3. Extraemos
        if self.limite>0 and cantidad>self.limite:
            print("Paga tus deudas, límite superado")
        else:
            super().extraer(cantidad)                 # Hacemos que "Cuenta" haga la resta. 
            
# Prueba rápida
cuenta_1 = CuentaLimitada(500, 100)  # Saldo inicial: 500€, Límite: 100€ (los números son elegidos random)

cuenta_1.extraer(150)                # Salta el mensaje: "Paga tus deudas, límite superado"
cuenta_1.extraer(80)                 # Pasa el filtro -> Cuenta hace la resta
print(f"Saldo restante: {cuenta_1.saldo}€")  # Debería mostrar 420€

#Crear una nueva clase, que herede CuentaLimitada, llamada CuentaMovimientos
#Cada vez que se ingrese o extraiga, se deberá registrar dicho movimiento. Un movimiento
#tiene dos propiedades: cantidad y tipo (ingreso o extraccion). La nueva clase clase
#tendrá un método que devuelve la lista de los cinco últimos movimientos 

class CuentaMovimientos (CuentaLimitada):
    def __init__(self, saldo, limite):
        super().__init__(saldo, limite)  # Le pasa saldo y limite a CuentaLimitada
        self.movimientos=[]              # Historial vacío
    def ingresar(self, cantidad):
        super().ingresar(cantidad)       # Suma el dinero usando la lógica heredada
        self.movimientos.append({
            "tipo":"ingreso",
            "cantidad":cantidad
        })
    def extraer(self, cantidad):
        saldo_antes=self.saldo           # Saldo antes de intentar sacar
        super().extraer(cantidad)        # CuentaLimitada comprueba el límite y resta
        if self.saldo<saldo_antes:       # Solo registramos el movimiento si el saldo realmente bajó (no superó el límite)
            self.movimientos.append({
                "tipo":"extraccion",
                "cantidad":cantidad
            })
    def ultimos_movimientos(self):
        return self.movimientos[-5]      # Devuelve los últimos 5 de la lista (no sale)