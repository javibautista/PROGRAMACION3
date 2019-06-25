def selection_sort(array):
    i=0
    #itt = 1
    #ind = 0
    while i < len(array)-1:
        #print('i = %d',%(i))
        #print('while_externo %s'%(itt))
        j = i+1
        pos_min = i
        #it = 0
        while j < len(array):
            #objetivo descubrir la posicion minima
            # j es la posicion actual
            # pos_min es la que yo creo que es la menor
            if array[j] < array[pos_min]:
                # estaba equivocado, así que .....
                pos_min = j
            j += 1
            #it += 1
            #print('while_inter %s'%(it))
        # ahora estoy seguro que pos_min es el minimo
        # intercambio
        tmp = array[i]
        array[i] = array[pos_min]
        array[pos_min] = tmp
        
        i += 1
        #ind += 1
        #print('while_externo %s'%(itt))
        #itt += 1
    return array

if __name__ == '__main__':
    #array = [6,7,8,9,3,4,5,2,1]
    #array = [9,8,7,6,5,4,3,2,1]
    #array = [1,2,3,4,5,6,7,8,9]
    #array = [10,11,4]
    #array = [-4,2,8,7]
    #array = [1,2,3,4]
    array = [4,3,2,1]
    print(selection_sort(array))

