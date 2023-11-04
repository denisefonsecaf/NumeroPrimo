#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.

def num_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

    
for num in range(1, 101):
    if num_primo(num):
        print(f"{num} é primo")