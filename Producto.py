from Articulo import Articulo

class Producto(Articulo):

    paisProducto = ''
    estado = 0
    impuesto = 0.0

    def __init__(self, idArticulo, nomArticulo, marcaArticulo, costoArticulo, paisProducto, estado, impuesto):
        Articulo.__init__(self, idArticulo, nomArticulo, marcaArticulo, costoArticulo)
        self.paisProducto = paisProducto
        self.estado = estado
        self.impuesto = impuesto

    def calcularImpuesto(self):
        totalImpuesto = (self.impuesto * self.costoArticulo) / 100
        print('Impuestos:',totalImpuesto)
        total = self.costoArticulo + totalImpuesto
        print('Total:',total)
