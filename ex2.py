"""Implemente um verificador de parênteses confirmando se os mesmo estão balanceados.

Exemplo:

Válido:
((A+B) * C)
Inválido:
(A+B))

Teste:

((A+B) * C)
(A+B))
((A+B)"""

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
    
    
emp = Pilha()

abrirParenteses = '('
fecharParenteses = ')'
contAbrir = 0
contFechar = 0

entrada = input("Digite a entrada: ")

for p in entrada:
    emp.push(p)

while emp.topo is not None:
    elemento = emp.pop()
    print(elemento)
    
    for desemp in elemento:
        if desemp == fecharParenteses:
            contFechar += 1 
        if desemp == abrirParenteses:
            contAbrir += 1 

print(contAbrir)
print(contFechar)
if contAbrir == contFechar:
    print("Válido")
else:
    print("Inválido")
        