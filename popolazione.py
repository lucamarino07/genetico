import numpy as np 
import random

def popolazione(regine, popolazione):
    # random.seed(1000)
    primo = [i+1 for i in range(regine)]
    popolazione_lista = []
    popolazione_lista.append(list(primo))

    for _ in range(popolazione-1):
        random.shuffle(primo)
        popolazione_lista.append(list(primo))

    return popolazione_lista

def fitness(popolazione,regine):
    m = (regine * (regine-1)) / 2
    fitness = []
    position = 0
    for cromosoma in popolazione:
        torti, fit = 0, 0
        for i in range(0, regine-1):
            for j in range(i+1, regine):
                if (abs(cromosoma[i]-cromosoma[j]) == abs(i-j)):
                    torti += 1
        fit = m - torti
        fitness.append([cromosoma, fit, position])
        position += 1
    return(fitness)



def fitness2(popolazione,regine):
    m = (regine * (regine-1)) / 2
    fitness = []
    position = 0
    for cromosoma in popolazione:
        torti, fit = 0, 0
        for i in range(0, regine-1):
            for j in range(i+1, regine):
                if (abs(cromosoma[i]-cromosoma[j]) == abs(i-j)):
                    torti += 1
        fit = m - torti
        fitness.append(fit)
        position += 1
    return(fitness)

def fitness_figlio(figlio):
    regine = len(figlio)
    m = (regine * (regine-1)) / 2
    fitness = 0
    torti = 0
    for i in range(0, regine-1):
            for j in range(i+1, regine):
                if (abs(figlio[i]-figlio[j]) == abs(i-j)):
                    torti += 1
    fitness = m - torti

    return fitness

def ordina_popolazione_per_fitness(fitness):
    fitness.sort(key = lambda x: x[1])
    return fitness

def roulette(fitness):
    fit2 = ordina_popolazione_per_fitness(fitness)
    somma_fit = 0
    somma_prob = 0
    fit3 = []

    for elemento in fit2:
        somma_fit += elemento[1]

    for elemento in fit2:
        prob_i = elemento[1] / somma_fit
        pre_prob = somma_prob
        somma_prob += prob_i
        fit3.append([elemento, [pre_prob, somma_prob]])

    return (fit3)

def seleziona_individuo(fitness):
    probabilità = random.uniform(0,1)
    # print(probabilità)
    res = list(filter(lambda x: x[1][0] < probabilità < x[1][1], roulette(fitness)))
    return res

def crossover(genitori):
    figlio = []
    geni_estratti = []
    numerosità =  len(genitori[0][0][0][0])
    for i in range(0, numerosità):
        if (genitori[0][0][0][0][i] == genitori[1][0][0][0][i]):
            figlio.append(int(genitori[0][0][0][0][i]))
            geni_estratti.append(genitori[0][0][0][0][i])
        else:
            figlio.append(0)
    
    for i in range(0,numerosità):
        if (figlio[i] == 0):
            gene_random = random.randint(1, numerosità)
            while (gene_random in geni_estratti):
                gene_random = random.randint(1, numerosità)
            figlio[i] = int(gene_random)
            geni_estratti.append(gene_random)
    

    fit = fitness_figlio(figlio)
    figlio_fit = [figlio, fit]

    return figlio_fit
    
def seleziona_sopravvissuti(genitori, figlio_fit):
    matrice = []
    for i in range(0,len(genitori)):
        matrice.append(genitori[i][0][0])
    matrice.append(figlio_fit)

    if (matrice[2][1] > matrice[1][1] and matrice[1][1] >= matrice[0][1]):
        position = matrice[0][2]
    elif (matrice[2][1] > matrice[0][1] and matrice[0][1] >= matrice[1][1]):
        position = matrice[1][2]
    else:
        position = -1
        
    return [figlio_fit, position]

def mutazione(popolazione, regine, posizione):
    indice1 = random.randint(0, regine-1)
    indice2 = random.randint(0, regine-1)

    while indice1 == indice2:
        indice2 = random.randint(0, regine-1)  
    
    cromosoma = popolazione[posizione]

    cromosoma[indice1], cromosoma[indice2] = cromosoma[indice2], cromosoma[indice1]
    cromosoma = list(cromosoma)

    return cromosoma

