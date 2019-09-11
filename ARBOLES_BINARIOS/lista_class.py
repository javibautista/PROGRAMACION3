class BynaryTree:
    def __init__(self, value):
        self.value = value
        self.izq = None
        self.der = None

    def get_left_child(self):
        return self.izq

    def get_right_child(self):
        return self.der

    def get_root_child(self):
        return self.value

    def set_left_child(self, other):
        if not self.is_empty(self.izq):
            raise ValueError('Ya tiene un valor')
        self.izq = other

    def set_right_child(self, other):
        if not self.is_empty(self.der):
            raise ValueError('Ya tiene un valor')
        self.der = other

    @staticmethod
    def is_empty(tree):
        return tree is None
