# Funciones recursivas sobre árboles

# la siguiente es una implementación de árboles binarios usando clases, tal
# como la trabajamos en el último práctico.

# Lo único que probablemente sea nuevo son las líneas de la forma

# `assert ...`

# que sirven para asegurarse de que una condición necesaria para el correcto
# funcionamiento del código se cumple (es verdadera).

# cuando `assert` es seguida de una condición que no se cumple, nuestro código falla.
# tu tarea es completar este archivo para que nada falle.

class BinaryTree:
    def __init__(self, value):
        self.root_value = value
        self.left_child = None
        self.right_child = None

    def get_root_value(self):
        return self.root_value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_left_child(self, tree):
        error_msg = 'set_left_child espera un BinaryTree como argumento'
        assert isinstance(tree, BinaryTree), error_msg
        error_msg = 'el arbol izquierdo no es vacío'
        assert self.left_child is None, error_msg
        self.left_child = tree

    def set_right_child(self, tree):
        error_msg = 'set_right_child espera un BinaryTree como argumento'
        assert isinstance(tree, BinaryTree), error_msg
        error_msg = 'el arbol derecho no es vacío'
        assert self.right_child is None, error_msg
        self.right_child = tree
        
    @staticmethod
    def is_empty(tree):
        return tree is None

# Ejercicio 1
# ===========

# Escribí el código necesario para que la variable `my_tree` tenga el árbol siguiente árbol:

#           (8)
#        b /   \ c
#       (3)    (10)
#    d /   \ e     \ h
#    (1)   (6)     (14)
#       f /   \g   / i
#       (4)   (7) (13)


my_tree = BinaryTree(8)  # <---- completar
b = BinaryTree(3)
my_tree.set_left_child(b)
c = BinaryTree(10)
my_tree.set_right_child(c)
d = BinaryTree(1)
b.set_left_child(d)
e = BinaryTree(6)
b.set_right_child(e)
f = BinaryTree(4)
e.set_left_child(f)
g = BinaryTree(7)
e.set_right_child(g)
h = BinaryTree(14)
c.set_right_child(h)
i = BinaryTree(13)
h.set_left_child(i)

assert my_tree is not None
assert my_tree.get_root_value() == 8
assert my_tree.get_left_child().get_root_value() == 3
assert my_tree.get_left_child().get_left_child().get_root_value() == 1
assert my_tree.get_right_child().get_left_child() is None

print('Ejercicio 1 completado')
"""
def is_empty(tree):
    return tree is None
"""
# Ejercicio 2
# ===========

# Implementá la función `sum_tree`. Esta función recibe un árbol binario que
# contiene números (por ej, my_tree) y devuelve la sumatoria de todos los números.
# Deberían pasar los tests que se escribieron a continuación.

def sum_tree(tree):
    #if tree is None:
    if BinaryTree.is_empty(tree):
        return 0
    
    else:
        return tree.get_root_value() + sum_tree(tree.get_left_child()) + sum_tree(tree.get_right_child())
        #return BinaryTree.get_root_value(tree) + sum_tree(BinaryTree.get_left_child(tree)) + sum_tree(BinaryTree.get_right_child(tree))
        #return tree.root_value + sum_tree(tree.left_child) + sum_tree(tree.right_child)
        #pass  # <---- completar


# tests:
assert sum_tree(None) == 0  # árbol vacío
assert sum_tree(BinaryTree(10)) == 10

tree = BinaryTree(8)
tree.set_left_child(BinaryTree(4))
tree.set_right_child(BinaryTree(-3))
assert sum_tree(tree) == 9

assert sum_tree(my_tree) == 66

print('Ejercicio 2 completado')

# Ejercicio 3
# ===========

# Implementá la función `tree_contains`.
# Esta función toma un árbol binario y un elemento y devuelve `True`
# si el elemento está en el árbol. De lo contrario, devuelve `False`.

def tree_contains(tree, elem):
    #if tree is None:
    if BinaryTree.is_empty(tree):
        return False
    
    return (tree.get_root_value() == elem) or (tree_contains(tree.get_left_child(),elem)) or (tree_contains(tree.get_right_child(),elem))
        

# tests
assert tree_contains(None, 1) == False  # árbol vacío
assert tree_contains(BinaryTree(10), 10) == True
assert tree_contains(BinaryTree(10), 1) == False

tree = BinaryTree(8)
tree.set_left_child(BinaryTree(4))
tree.set_right_child(BinaryTree(-3))
assert tree_contains(tree, 9) == False
assert tree_contains(tree, 4) == True
assert tree_contains(tree, -3) == True
assert tree_contains(tree, 8) == True

assert tree_contains(my_tree, 7) == True

print('Ejercicio 3 completado')

# Ejercicio 4 (difícil)
# =======================

# A la hora de recorrer un árbol, hay maneras que son particularmente útiles:
#   - preorder:   Primero vistamos el nodo raíz, luego recursivamente hacemos un
#                 recorrido en preorder del subárbol izquierdo, seguido de un recorrido en
#                 preorder del subárbol derecho.
#   - inorder:    Recursivamente hacemos un recorrido inorder del subárbol izquierdo,
#                 luego visitamos la raíz y por último hacemos un recorrido
#                 inorder del subárbol derecho.
#   - postorder:  Recursivamente hacemos un recorrio postorder del subárbol derecho,
#                 luego hacemos un recorrido postorder del subárbol izquierdo y
#                 finalmente visitamos la raíz.

# Implementá las tres maneras de recorrer el árbol. En estas funciones, cuando
# te toque "procesar" el nodo raíz, sólo tenés que imprimir el valor.


def preorder_tree_traversal(tree):
    #print('imprimiendo elementos en preorder')
    if BinaryTree.is_empty(tree):
        return
    else:
        print(tree.get_root_value(), end=' ')
        preorder_tree_traversal(tree.get_left_child())
        preorder_tree_traversal(tree.get_right_child())
print('imprimiendo elementos en preorder')
"""
print(tree.get_root_value(), end=' ')
    if tree.get_left_child() is not None:
        preorder_tree_traversal(tree.get_left_child())
    
    if tree.get_right_child() is not None:
        preorder_tree_traversal(tree.get_right_child())# <--- completar
"""

preorder_tree_traversal(my_tree)
# debería imprimir lo siguientes:
# 8, 3, 1, 6, 4, 7, 10, 14, 13


def inorder_tree_traversal(tree):
    #print('imprimiendo elementos en inorder')
    if BinaryTree.is_empty(tree):
        return
    else:
        inorder_tree_traversal(tree.get_left_child())
        print(tree.get_root_value(), end=' ')
        inorder_tree_traversal(tree.get_right_child())# <--- completar

print('\nimprimiendo elementos en inorder')
inorder_tree_traversal(my_tree)
# debería imprimir lo siguiente:
# 1, 3, 4, 6, 7, 8, 10, 14, 13


def postorder_tree_traversal(tree):
    #print('imprimiendo elementos en postorder')
    if BinaryTree.is_empty(tree):
        return
    else:
        postorder_tree_traversal(tree.get_right_child())
        postorder_tree_traversal(tree.get_left_child())
        print(tree.get_root_value(), end=' ')# <--- completar
print('\nimprimiendo elementos en postorder')
postorder_tree_traversal(my_tree)
# debería imprimir lo siguiente:
# 13, 14, 10, 7, 4, 6, 1, 3, 8

print('\nEjercicio 4 completado')
