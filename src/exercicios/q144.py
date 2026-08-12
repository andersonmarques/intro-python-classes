'''Crie um programa que receba dez
 nomes do usuário, armazene-os em 
 um vetor e ao final mostre a 
 listagem, indicando a posição de 
 cada nome'''
import numpy as np

# U21 permite textos de ate 21 caracteres
nomes = np.zeros(10, dtype='U21')
for i in range(1, 11):
    nomes[i - 1] = input(f'{i}º nome:\n')

for i in range(1, 11):
    print(f'{i-1}º - {nomes[i-1]}')