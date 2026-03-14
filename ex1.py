"""
1. Inversão de string usando pilha 
Escreva um programa que inverta uma palavra usando uma pilha.

Exemplo:

Entrada:
ALGORITMO
Saída Esperada:
OMTIROGLA

Dica:

Empilhar cada caractere
Desempilhar até a pilha esvaziar
"""

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
        elem = self.topo
        self.topo = self.topo.next
        self._size -= 1
        return elem.value
    
    def mostrar(self):
        if self.topo is None:
            return None
        pointer = self.topo

        while (pointer):
            print(pointer.value, end = "")
            pointer = pointer.next

p = Pilha()
p.push("a")
p.push("l")
p.push("g")
p.push("o")
p.push("r")
p.push("i")
p.push("t")
p.push("m")
p.push("o")
p.push("s")
p.mostrar()