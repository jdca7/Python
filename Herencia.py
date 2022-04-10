#clase padre o clase base
class Producto:
    def __init__(self, Art, Nombre, Marca, Costo) :
        
        self.IdArticulo = Art
        self.NomArticulo = Nombre
        self.MarcaArticulo = Marca
        self.CostoArticulo = Costo

    def ImprimirArticulo(self):
       print("ID Articulo: " , self.IdArticulo ) 
       print("Nombre Articulo: " , self.NomArticulo)
       print("Marca Articulo: " , self.MarcaArticulo)
       print ("Costo: " , self.CostoArticulo)

#Esta es la clase hija
class Articulo (Producto):
    def __init__(self,Art, Nombre, Costo, Marca, procedencia, state, imp):
        super().__init__(Art, Nombre, Costo, Marca)
        self.paisProducto = procedencia
        self.Estado = state
        self.Impuesto = imp

    def CalcularImpuesto(self):
        pass
        '''ImpTotal = (self.Impuesto * self.CostoArticulo)/100
        print ("Impuesto total: " , ImpTotal)
        ProdTotal = (self.CostoArticulo + Impuesto)
        print ("Total a pagar: " , ProdTotal)
        '''



