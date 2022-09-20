'''Classes'''
class Node:
    def __init__(self,j1,j2,j3):
        self.father = None
        self.j1 = j1
        self.j2 = j2
        self.j3 = j3
        self.child = []
        self.gen = 0

    def copy(self):
        father = self.father
        jx = self.j1.copy()
        jy = self.j2.copy()
        jz = self.j3.copy()
        gen = self.gen
        return Node(jx,jy,jz)

    def transf(self,jx,jy):
        if (jx.at + jy.at) <= jy.cap: # Transfere toda a capacidade
            jy.at = jy.at+jx.at
            jx.at = 0
        else: # Transfere capacidade parcialmente
            x = jy.cap - jy.at
            jx.at -= x
            jy.at += x

    def addChild(self,child):
        self.child.append(child)

    def __str__(self) -> str:
        return str([tuple([self.j1.at,self.j1.tgt]),tuple([self.j2.at,self.j2.tgt]),tuple([self.j3.at,self.j3.tgt])])

class GeneralTree:
    def __init__(self):
        self.nodes = []
    def add(self,Node) -> Node:
        self.nodes.append(Node)

class jarro:
    def __init__(self,cap,at,tgt):
        self.cap = cap
        self.at = at
        self.tgt = tgt

    def copy(self):
        cap = self.cap
        at = self.at
        tgt = self.tgt
        return jarro(cap,at,tgt)

    def __str__(self):
        return f'Cap: {self.cap} - At: {self.at} - Tgt: {self.tgt}\n'

'''Functions'''
def poss(root) -> Node: #Verifica se há possibilidade de solução
    if ((root.j1.at+root.j2.at+root.j3.at)==(root.j1.tgt+root.j2.tgt+root.j3.tgt)):
        return 1
    else:
        return -1

def nextGen(node,gen) -> Node: # Dado um nó, cria as próximas gerações
    child = []

    cd1 = node.copy()
    cd1.father = node
    cd1.gen = gen

    cd2 = node.copy()
    cd2.father = node
    cd2.gen = gen
    
    cd3 = node.copy()
    cd3.father = node
    cd3.gen = gen

    cd4 = node.copy()
    cd4.father = node
    cd4.gen = gen

    cd5 = node.copy()
    cd5.father = node
    cd5.gen = gen

    cd6 = node.copy()
    cd6.father = node
    cd6.gen = gen

    cd1.transf(cd1.j1,cd1.j2)
    child.append(cd1)
    cd2.transf(cd2.j1,cd2.j3)
    child.append(cd2)
    cd3.transf(cd3.j2,cd3.j1)
    child.append(cd3)
    cd4.transf(cd4.j2,cd4.j3)
    child.append(cd4)
    cd5.transf(cd5.j3,cd5.j1)
    child.append(cd5)
    cd6.transf(cd6.j3,cd6.j2)
    child.append(cd6)
    return cd1,cd2,cd3,cd4,cd5,cd6 # Retorna 6 nós com as possibilidade de transferência
    
def verify(N) -> Node: # Verifica se o nó possui a solução do problema
    j1 = (N.j1.at,N.j1.tgt)
    j2 = (N.j2.at,N.j2.tgt)
    j3 = (N.j3.at,N.j3.tgt)

    if (j1[0] == j1[1] and j2[0] == j2[1] and j3[0] == j3[1]):
        return 1
    else:
        return -1

def write_log(j1_c,j2_c,j3_c,j1_a,j2_a,j3_a,j1_t,j2_t,j3_t,mov):
    with open("saida_exemplo_T1.txt","a") as log:
        log.write(f'{j1_c} {j2_c} {j3_c}\n{j1_a} {j2_a} {j3_a}\n{j1_t} {j2_t} {j3_t}\nMovimentos: {mov}\n')

def main(): # Função principal
    if __name__ == '__main__':
        with open("entrada_exemplo_T1.txt","r") as file:
            aux = file.readlines()

            c_file = []

            for line in aux: #Cria os jarros lendo as linhas do arquivo até encontrar a pala 'Movimentos'
                if line.splitlines()[0] != 'Movimentos: ':
                    c_file.append(line.split())
                else:
                    j1_c = int(c_file[0][0])
                    j2_c = int(c_file[0][1])
                    j3_c = int(c_file[0][2])

                    j1_a = int(c_file[1][0])
                    j2_a = int(c_file[1][1])
                    j3_a = int(c_file[1][2])

                    j1_t = int(c_file[2][0])
                    j2_t = int(c_file[2][1])
                    j3_t = int(c_file[2][2])

                    j1 = jarro(j1_c,j1_a,j1_t)
                    j2 = jarro(j2_c,j2_a,j2_t)
                    j3 = jarro(j3_c,j3_a,j3_t)

                    if j1_c > 40:
                        mov = 'Capacidade de j1 maior que 40'
                        write_log(j1_c,j2_c,j3_c,j1_a,j2_a,j3_a,j1_t,j2_t,j3_t,mov)
                        exit

                    if j2_c > 40:
                        mov = 'Capacidade de j2 maior que 40'
                        write_log(j1_c,j2_c,j3_c,j1_a,j2_a,j3_a,j1_t,j2_t,j3_t,mov)
                        exit

                    if j3_c > 40:
                        mov = 'Capacidade de j3 maior que 40'
                        write_log(j1_c,j2_c,j3_c,j1_a,j2_a,j3_a,j1_t,j2_t,j3_t,mov)
                        exit

                    c_file = []

                    fila = []
                    steps = []
                    mov = None

                    root = Node(j1,j2,j3) # Cria a raiz
                    if poss(root) == -1:  # Verifica se é possível resolver
                        mov = 'Impossível resolver'
                        write_log(j1_c,j2_c,j3_c,j1_a,j2_a,j3_a,j1_t,j2_t,j3_t,mov)

                    tree = GeneralTree() # Cria a árvore
                    tree.add(root) # Adiciona o elemento inicial como raíz

                    for n in tree.nodes: # Adiciona o elemento à fila de procura 
                        fila.append(n)

                    while len(fila) != 0:
                        mov = None
                        naux = fila[0] # Pega o primeiro elemento da fila
                        fila.remove(naux)
                        if verify(naux) == 1: # Verifica se este elemento é a solução
                            mov = naux.gen # Verifica qual de qual geração é o elemento
                            print(naux)
                            print(f'Movimentos:{mov}')
                            write_log(j1_c,j2_c,j3_c,j1_a,j2_a,j3_a,j1_t,j2_t,j3_t,mov)
                            break
                        else:
                            cd1,cd2,cd3,cd4,cd5,cd6 = nextGen(naux,naux.gen+1) # Cria a próxima geração passando como arg. o nó atual e geração + 1.
                            if (cd1.j1.at,cd1.j2.at,cd1.j3.at) not in steps: # Para cada um dos filhos, verifica se o estado já foi avaliado ou não
                                steps.append((cd1.j1.at,cd1.j2.at,cd1.j3.at)) # Se não está na lista de estados, adiciona
                                naux.addChild(cd1) # Adiciona como filho do nó
                                fila.append(cd1) #Adiciona à fila de busca
                            if (cd2.j1.at,cd2.j2.at,cd2.j3.at) not in steps:
                                steps.append((cd2.j1.at,cd2.j2.at,cd2.j3.at))
                                naux.addChild(cd2)
                                fila.append(cd2)
                            if (cd3.j1.at,cd3.j2.at,cd3.j3.at) not in steps:
                                steps.append((cd3.j1.at,cd3.j2.at,cd3.j3.at))
                                naux.addChild(cd3)
                                fila.append(cd3)
                            if (cd4.j1.at,cd4.j2.at,cd4.j3.at) not in steps:
                                steps.append((cd4.j1.at,cd4.j2.at,cd4.j3.at))
                                naux.addChild(cd4)
                                fila.append(cd4)
                            if (cd5.j1.at,cd5.j2.at,cd5.j3.at) not in steps:
                                steps.append((cd5.j1.at,cd5.j2.at,cd5.j3.at))
                                naux.addChild(cd5)
                                fila.append(cd5)
                            if (cd6.j1.at,cd6.j2.at,cd6.j3.at) not in steps:
                                steps.append((cd6.j1.at,cd6.j2.at,cd6.j3.at))
                                naux.addChild(cd6)
                                fila.append(cd6)

main()