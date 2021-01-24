#!/usr/local/bin/python3
from popolazione import fitness, seleziona_individuo, crossover, \
    seleziona_sopravvissuti, popolazione, mutazione, fitness2
import pop
import pandas
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


def run_genetico(n_regine, n_popolazione):
        # n_regine = int(input('Numero regine --> '))
        m = (n_regine * (n_regine-1)) / 2
        # n_popolazione = int(input('Numero popolazione --> '))
        iterazione = 1
        itmax = 100000000000
        prob_mutazione = 0.2
        popolazione_lista = popolazione(n_regine, n_popolazione)

        soluzione = []
        fitness_it_dopo_it = []
        fitness_it_dopo_it.append(0)
        iterazioni_lista = []
        iterazioni_lista.append(iterazione)





        while iterazione < itmax:

            print(f'Iterazione #{iterazione}')
            fit = fitness(popolazione_lista, n_regine)
            fit2 = fitness2(popolazione_lista, n_regine)
            fitness_columns = ['Cromosoma', 'Fitness', 'Posizione']
            fitness_it_dopo_it.append(max(fit2))

            genitori = []
            for i in range(2):
                genitore = seleziona_individuo(fit)
                genitori.append(genitore)

            figlio_fit = crossover(genitori)

            sopravvissuto = seleziona_sopravvissuti(genitori, figlio_fit)

            if (sopravvissuto[1] != -1):
                popolazione_lista[sopravvissuto[1]] = list(sopravvissuto[0][0])

            if (sopravvissuto[0][1] >= m):
                soluzione = sopravvissuto[0]
                fitness_it_dopo_it.append(sopravvissuto[0][1])
                iterazione +=1
                iterazioni_lista.append(iterazione)
                print('*'*50)
                print(sopravvissuto[0])
                break
            

            if (iterazione > 3):
                if (random.uniform(0,1) < prob_mutazione):
                    posizione = random.randint(0, n_regine-1)

                    popolazione_lista[posizione] = mutazione(popolazione_lista, n_regine, posizione)

        

            iterazione +=1
            iterazioni_lista.append(iterazione)


        chessboard = np.zeros((n_regine,n_regine))
        chessboard[1::2, 0::2] = 1
        chessboard[0::2, 1::2] = 1

        contatore = 0
        for elemento in chessboard:
            elemento[sopravvissuto[0][0][contatore]-1] = 1.5
            contatore = contatore +1


        return soluzione



# plt.plot(iterazioni_lista,fitness_it_dopo_it)
# plt.show()


