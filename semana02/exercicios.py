#BINGO

import random

def numero():
    bingo = []
    usedvalues = []
    
    for line in range(5):
        bingo.append([])
        
        for coluna in range(5):
            num = random.randint(0,99)
            
            while num in usedvalues:
                num = random.randint(0,99)
            if num not in usedvalues:
                bingo[line].append(num)
                usedvalues.append(num)
    return bingo
    
def main():
    bingo = numero()
    print(bingo)
main()

#2. Escreva um programa que calcule e imprima a soma de todos os elementos abaixo da diagonal principal de uma matriz.
