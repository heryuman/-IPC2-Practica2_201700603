import  graphviz

def grafico(lista):
     d=graphviz.Digraph('structs',filename="Agenda.gv",node_attr={'shape': 'record'})
     d.node("0","Agenda")
     for i in range(lista.size()):
         d.node(str(i+1),'<f0> nombre: '+str(lista.searchbyIt(i).getNombre())+'|<f1> Apellido: '+str(lista.searchbyIt(i).getApellido())+'|<f2> telefono: '+str(lista.searchbyIt(i).getTelefono()))


     for i in range(lista.size()+1):

         if i<lista.size():
             d.edge(str(i), str(i + 1))

     d.view()

