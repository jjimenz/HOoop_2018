class Fila(object):
    """Clase base de fila"""

    def __init__(self):
        """constructor de la clase Fila """
        self.enfila= 0
        self.fila = []

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
    
    def abrircajanueva(self,maxenfila,filanueva):
        """S"""
        
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        
    def atender(self):
        """Atiende al proximo cliente prederencial"""
             
class cliente(object):
    """clase cliente """
    
    def __init__(self,dni):
        """ constructor de la clase cliente """
        self.dni=dni
 #       self.categoria=None
    
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria=categoria
        if __name__ == "__main__":
            """ simular una fila en una entidad bancaria"""
    
    def testcliente(self,cliente):
        """ constructor de la clase cliente """
        print (self.dni, self.categoria)
    
