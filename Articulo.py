class Articulo:

    idArticulo = 0
    nomArticulo = ''
    marcaArticulo = ''
    costoArticulo = 0.0

    def __init__(self, idArticulo, nomArticulo, marcaArticulo, costoArticulo):
        self.idArticulo = idArticulo
        self.nomArticulo = nomArticulo
        self.marcaArticulo = marcaArticulo
        self.costoArticulo = costoArticulo
        

    def imprimirArticulo(self):
        print('ID:',self.idArticulo)
        print('Nombre:',self.nomArticulo)
        print('Marca:',self.marcaArticulo)
        print('Costo:',self.costoArticulo)
        