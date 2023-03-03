# A estrutura de dados pilha tem esse nome porque se assemelha conceitualmente às pilhas
# (de roupas, caixas, livros etc.) do mundo real. Nela, quem chegou primeiro fica embaixo de todos os outros.
# Ora, para você remover uma caixa que está abaixo de várias outras, você precisa remover primeiro as de cima.
from typing import List


class PilhaEncadeada:
    def __init__(self, topo=None):
        self.topo = topo


maxPilha: int = 10
pilha: list[None] = [None] * maxPilha
topoPilha = None


def push(self, novoNo):
    novoNo.proximo = self.topo  # insere o nó
    self.topo = novoNo  # atualiza o topo da pilha


def push(novoNo):
    global pilha
    global topoPilha
    global maxPilha
    if topoPilha == None:  # pilha vazia
        pilha[0] = novoNo  # insere o nó
        topoPilha = 0  # atualiza o topo da pilha
    elif topoPilha:  # pilha cheia
        return -1  # -1 → erro de pilha cheia
    else:
        topoPilha = topoPilha + 1  # atualiza o topo da pilha
        pilha[topoPilha] = novoNo  # insere o nó
    return topoPilha  # saída normal

    def pop(self):
        if self.topo == None:
            return None  # erro pilha vazia
        k = self.topo  # salva o nó removido
        self.topo = self.topo.proximo  # remove o nó
        return k  # retorna o nó removido
