# Deque
# A estrutura de dados deque é uma generalização da fila e da pilha, essencialmente permitindo que se adicione ou remova
# nós do início ou do final da lista. Para evitar confusões, as operações são normalmente identificadas com qual lado da
# fila está sendo alterado. A remoção de um nó do início pode ser chamada de pop_front, enquanto a remoção de um nó ao
# final pode ser chamada de pop_back.

from collections import deque

q = deque()  # cria o deque
q.append('b')  # insere no final
q.append('c')
q.appendleft('a')
print(q)  # imprime o deque
print(q.popleft())  # remove do inicio
print(q.pop())  # remove do final
