def insertion_sort(lista):
    indice = 1
    #itt = 1
    #ind = 0
    # Busqueda desde 1 al largo de la lista
    while indice < len(lista):
        #print('while_externo %s'%(itt))
        #print('i = %d'%(i))
        objetivo_insertar = lista[indice]
        elem_izq = indice - 1
        #it = 0
        # Comparo el "objetivo a insertar" con el "elemento de su izquierda"
        # Y hasta que el elemento izquierdo sea cero o mayor(caiga dentro de la lista)
        while elem_izq >= 0 and (objetivo_insertar < lista[elem_izq]):
            # Cumple la condicion de que el objetivo es menor que su izquierdo
            # Se hace el intercambio
            lista[elem_izq+1] = lista[elem_izq]
            lista[elem_izq] = objetivo_insertar
            #lista[pos_min] = tmp
            #print(lista)
            # decremento el indice para comparar si el siguiente izquierda es menor
            elem_izq -= 1
            #it += 1
            #print('while_inter %s'%(it))
            #print('elemento %s itercambio %s lugar/es'%(objetivo_insertar, it))
        # incrementando en uno al indice
        indice += 1
        #ind += 1
        #print('while_externo %s'%(itt))
        #itt += 1
    return lista
"""
if __name__ == '__main__':
    #lista = [6,7,8,9,3,4,5,2,1]
    #lista = [9,8,7,6,5,4,3,2,1]
    #lista = [1,2,3,4,5,6,7,8,9]
    #lista = [-4,2,8,7]
    #lista = [10,3,2,1]
    #lista = [1, 2, 3, 4, -5, 6, 7, 8, 0]
    #lista = [1, 2, 3, 4]
    lista = [4, 3, 2, 1]
    print(insertion_sort(lista))
"""
