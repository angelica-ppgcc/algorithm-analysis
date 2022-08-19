import numpy as np
from random import shuffle, randint

class Objeto:
    
    def __init__(self, value, key, prev, prox):
        self.value = value
        self.key = key
        self.prox = prox
        self.prev = prev
            
def insert(x):
    global T, h, livre
    
    if x.key not in T:
        return ("Chave inexistente!")
    
    m = len(h)
    flag = T[x.key][1] #Valor da flag do objeto x
    
    flags = np.array(T.values()) #Captura todas os elementos da tabela da forma [objeto, flag]
    flags = flags[:,1] #Captura somente as flags de todos os objetos
    
    if np.sum(flags) == 0: #Verifica se a tabela hash esta vazia (Ou seja, todas as flags iguais a 0)
        livre = 0        
        key = x.key
        if livre == h.index(x.key):
            livre = T[key][0].prox

        
    elif flag == 1: #Se a posicao da chave de x eh igual ao livre / Se posicao ocupada 
        key = h[livre]     
        livre = T[h[livre]][0].prox
        
    elif flag == 0: #Se a posicao esta vazia 
        key = x.key 
        
        if h.index(key) <= livre:
            livre = T[h[livre]][0].prox

        
    T[key][0].value = x.value #Adicione o elemento na chave
    T[key][1] = 1 #Altere o valor da flag
    T[h[T[key][0].prev]][0].prox = T[key][0].prox #Atuallza o proximo do anterior
    aux = T[h[T[key][0].prox]][0].prev
    T[h[T[key][0].prox]][0].prev = T[key][0].prev #Atualiza o anterior do proximo
    T[key][0].prox = aux #Faz o proximo do objeto apontar para si mesmo
        
    
def delete(x):
    global livre
    flag = T[x.key][1]
    print "flag ", flag
    print T[x.key][0].value
    if flag == 1:
        T[x.key][0].value = None
        T[x.key][1] = 0
        aux = T[h[T[x.key][0].prev]][0].prox
        T[h[T[h[T[x.key][0].prev]][0].prox]][0].prev = T[x.key][0].prox
        T[h[T[x.key][0].prev]][0].prox = T[x.key][0].prox
        T[x.key][0].prox = aux
    
        if h.index(x.key) < livre:
            livre = h.index(x.key)  
    else:
        print("Erro na remocao")
        
def search(k):
    global T
    return T[k][0]

def showHashTable():
    global T, h
    
    t = []
    for k in h:
        t.append(T[k][0].value)
    
    print(t)
    

if __name__ == "__main__":
    
    m = 4 #Tamanho da Tabela hash
    livre = None
    
    T = {}
    
    keys = range(1,m+1)
    shuffle(keys)
    
    h = keys[:] #hashes of Hash Table
    print("Chaves: ", h) #Valores das chaves 
    
    #Procedimento de mapeamento das chaves na tabela Hash
    for k in h:
    
        prev = (h.index(k)-1)%m
        prox = (h.index(k)+1)%m
        print (prev, prox)

        x = Objeto(None, k, prev, prox)
        T[k] = [x, 0] #Adiciona o objeto e a flag 0
        
    #Criacao dos objetos  que serao adicionados
    x1 = Objeto(5, 2, m-1, 1)
    x2 = Objeto(4, 2, 0, 2)
    x3 = Objeto(3, 4, 1, 3)
    x4 = Objeto(2, 3, 2, 0)
    
    #Insercao dos objetos na tabela 
    insert(x1)
    print("Adicionar o 5 na chave 2")
    showHashTable()
    insert(x2)
    print("Adicionar o 4 na chave 2")
    showHashTable()
    insert(x3)
    print("Adicionar o 3 na chave 4")
    showHashTable()
    insert(x4)
    print("Adicionar o 2 na chave 3")
    showHashTable()
    y1 = search(1)
    delete(y1)
    print("Remover elemento de chave 1")
    showHashTable()
    y2 = search(4)
    delete(y2)
    print("Remover elemento de chave 4")
    showHashTable()
        