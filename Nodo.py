class Node(object):
    def __init__(self, elemento):
        self.siguiente=None
        self.anterior=None
        self.elemento=elemento

    def getElemento(self):
        return self.elemento
