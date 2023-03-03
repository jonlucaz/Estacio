# Até o momento, você lidou com estruturas de dados que permitiam inserção e remoção de nós em quaisquer posições.
# Entretanto, para algumas aplicações, queremos utilizar uma estrutura de dado que remova nós
# (também chamada de consumir os nós) na mesma ordem em que esses nós foram adicionados. Para isso, usamos a fila.

# A estrutura de dados fila tem esse nome porque se assemelha conceitualmente às filas do mundo real. Nela, quem chegou
# primeiro está aguardando mais tempo e também é atendido primeiro. Você pode pensar na fila como uma fila única de um
# mercado ou banco.

class FilaEncadeada:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = inicio


maxFila: int = 10
fila = [None] * maxFila
inicioFila = None
finalFila = None

