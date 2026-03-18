class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Pilha:
    def __init__(self):
        self.topo = None
        self._size = 0
    
    def push(self, value):
        node = Node(value)
        node.next = self.topo
        self.topo = node
        self._size += 1
        
    def pop(self):
        if self.topo is None:
            return None
        aux = self.topo
        self.topo = self.topo.next
        self._size -= 1
        return aux.value

def verificar_parenteses(value):
    p = Pilha()
    valido = True

    for elem in value:
        if elem == '(':
            p.push(elem)
        elif elem == ')':
            if p.topo is None:
                valido = False
            p.pop()

    if p.topo is not None:
        valido = False
    
    return valido
        
entrada = input("Digite a entrada: ")

if verificar_parenteses(entrada):
    print('Válido')
else: 
    print('Inválido')
        
