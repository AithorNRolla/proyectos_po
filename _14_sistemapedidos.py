class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        

    def consultar_datos(self):
        print(f"[{self.codigo}]{self.nombre}- Precio:{self.precio}€|Stock:{self.stock}")
        

    def modificar_stock(self, cantidad):
        #self.cantidad=cantidad
        if self.stock+cantidad>=0:
            self.stock+=cantidad
        else:
            print(f"No hay stock de {self.nombre}")
        
class LineaPedido:
    def __init__(self, producto, cantidad):
        self.producto=producto
        self.cantidad=cantidad
        

    def calcular_importe(self):
        return self.producto.precio*self.cantidad
#======= PEDIDO =========#       
class Pedido:
    def __init__(self, numero_pedido, cliente):
        self.numero_pedido=numero_pedido
        self.cliente=cliente
        self.lineas=[]
        self.estado="pendiente"

    def agregar_producto(self, producto, cantidad):
        if producto.stock>=cantidad:
            nueva_linea=LineaPedido(producto,cantidad)
            self.lineas.append(nueva_linea)
            producto.modificar_stock(-cantidad)
        else:
            print(f"No hay stock suficiente de {producto.nombre}")
            
        
    def eliminar_producto(self, codigo_producto):
         for linea in self.lineas:
            if linea.producto.codigo==codigo_producto:
                linea.producto.modificar_stock(linea.cantidad)
                self.lineas.remove(linea)
                break

    def calcular_total(self):
        total=0
        for linea in self.lineas:
            total+=linea.calcular_importe()
        return total 

    def mostrar_pedido(self):
        print(f"Pedido:{self.numero_pedido}|Cliente:{self.cliente}|Estado:{self.estado}")
        for linea in self.lineas:
            print(f"- {linea.producto.nombre} x{linea.cantidad}={linea.calcular_importe()} €")
        print(f"Total del pedido: {self.calcular_total()} €")

#======= DESCUENTOS =======#
class Descuento:
    def aplicar(self, importe):
        # Por defecto (Sin descuento), devuelve el importe tal cual
        return importe

class DescuentoPorcentual(Descuento):
    def __init__(self, porcentaje):
        self.porcentaje=porcentaje
        
    def aplicar(self, importe):
        return importe-(importe*self.porcentaje/100)
        #Devuelve importe

class DescuentoFijo(Descuento):
    def __init__(self, cantidad_fija):
        self.cantidad_fija=cantidad_fija
        
    def aplicar(self, importe):
        return max(0, importe - self.cantidad_fija)
        #self.cantidad_fija (asegúrate de que no sea menor que 0)
        pass

#======= PAGOS =======#
class FormaPago:
    def pagar(self, importe):
        pass

class TarjetaCredito(FormaPago):
    def pagar(self, importe):
        total=round(importe * 1.01, 2)
        print(f"Pagado con Tarjeta de Crédito (1% comisión): {total} €")
        return total

class PayPal(FormaPago):
    def pagar(self, importe):
        total=round(importe * 1.02, 2)
        print(f"Pagado con PayPal (2% comisión): {total} €")
        return total

class Transferencia(FormaPago):
    def pagar(self, importe):
        total=round(importe, 2)
        print(f"Pagado por Transferencia Bancaria (sin comisión): {total} €")
        return total
#======= PROGRAMA PRINCIPAL (PRUEBA COMPLETA) =======#
prod_1=Producto("P01", "Teclado Mecánico", 80, 10)
prod_2=Producto("P02", "Ratón Gaming", 45, 5)
prod_3=Producto("P03", "Monitor 27''", 250, 3)

pedido_1=Pedido(101, "Laura")
pedido_1.agregar_producto(prod_1, 2)
pedido_1.agregar_producto(prod_2, 1)
pedido_1.agregar_producto(prod_3, 1)

pedido_1.mostrar_pedido()
print("-" * 40)

#Quitamos el ratón (P02) para comprobar que devuelve el stock (sugerencia de IA)
pedido_1.eliminar_producto("P02")
pedido_1.mostrar_pedido()
print("-" * 40)

#Aplicamos descuento (independiente) y pagamos
descuento = DescuentoPorcentual(10) # 10% de descuento!!!
importe_con_descuento = descuento.aplicar(pedido_1.calcular_total())
print(f"Importe tras descuento: {importe_con_descuento} €")

pago=PayPal()
pago.pagar(importe_con_descuento)
pedido_1.estado = "pagado"
print(f"Estado final del pedido: {pedido_1.estado}")