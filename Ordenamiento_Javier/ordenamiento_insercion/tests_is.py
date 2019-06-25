import unittest
import random
from insertion_sort import insertion_sort

class test_is(unittest.TestCase):
    def test_lista_de_cero_elemento(self):
        l = []
        resultado = insertion_sort(l)
        self.assertListEqual(resultado, [], 'Esperaba ver [] y la función devolvió %s'%(resultado))
    def test_lista_de_un_elemento(self):
        l = [-10]
        resultado = insertion_sort(l)
        self.assertListEqual(resultado, l, 'Esperaba ver %s y la función devolvió %s'%([-10], resultado))
    def test_lista_de_dos_elemento_ord(self):
        l = [100, -10]
        resultado = insertion_sort(l)
        self.assertListEqual(resultado, [-10, 100], 'Esperaba ver %s y la función devolvió %s'%([-10, 100], resultado))
    def test_lista_de_dos_elemento_desord(self):
        l = [-10, 100]
        resultado = insertion_sort(l)
        self.assertListEqual(resultado, [-10, 100], 'Esperaba ver %s y la función devolvió %s'%([-10, 100], resultado))
    def test_lista_de_diez_elemento(self):
        l = [random.randint(-10,100) for _ in range(10)]
        #a = [random.randint(-10,100) for _ in range(10)]
        #print(l)
        resultado = insertion_sort(l)
        #print(a)
        self.assertListEqual(resultado, l, 'Esperaba ver %s y la función devolvió %s'%(l, resultado))
    def test_lista_de_tuplas_elemento(self):
        l = [(9,-10),(8,3),(2,5)]
        resultado = insertion_sort(l)
        #print(l)#[(2, 5), (8, 3), (9, -10)]
        self.assertListEqual(resultado, sorted([(9,-10),(8,3),(2,5)]), 'Esperaba ver %s y la función devolvió %s'%(sorted([(9,-10),(8,3),(2,5)]), resultado))
    def test_lista_de_caracteres_elemento(self):
        l = ['y','d','c','a','z']
        resultado = insertion_sort(l)
        #print(l)# ['a', 'c', 'd', 'y', 'z']
        self.assertListEqual(resultado, sorted(['y','d','c','a','z']), 'Esperaba ver %s y la función devolvió %s'%(sorted(['y','d','c','a','z']), resultado))

if __name__ =='__main__':
    unittest.main()
    
