from Nodo import Node
class list(object):
    def __init__(self):
        self.head=None
        self.cont=0


    def size(self):
        return self.cont

    def empty(self):
        if self.head==None:
            return True
        else:
            return False
    def insert(self,elemento):
        nElemento=Node(elemento)
        if self.cont==0:
            self.head=nElemento
            self.cont=self.cont+1
        else:
            tmp=self.head
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.siguiente=nElemento
            self.cont=self.cont+1

    def searchbyIt(self,id):
        if self.size()>0 and id<=self.size():
            tmp=self.head
            i=0
            while i < id:
                tmp=tmp.siguiente
                i+=1
            return tmp.getElemento()
        else:
            print("No hay un elemento para ese indice")


    def search(self, id):
        if self.size() > 0:

            tmp = self.head
            for i in range(self.cont):
                if int(tmp.getElemento().getTelefono()) == id:
                    return tmp.getElemento()
                else:
                    tmp = tmp.siguiente


    def view(self):
        tmp=self.head
        print(self.cont)
        for i in range(self.cont):
            print("Nombre: ",tmp.getElemento().getNombre()," Telefono: ",tmp.getElemento().getTelefono())
            tmp=tmp.siguiente

    def exist(self,id):
        if self.size()>0:

            tmp=self.head
            for i in range(self.cont):
                if int(tmp.getElemento().getTelefono())==id:

                    return True
                else:
                    tmp=tmp.siguiente




