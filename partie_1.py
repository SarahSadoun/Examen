# -*- coding: utf-8 -*-
"""Partie 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gQBTf4sntDvKUkMyQYjhrdPU-sb1CmWu

1. Création de fonction mathématique simple en Python

Implémenter la fonction polynomiale ci-dessous :
"""

def polynome(x):
  return x**3-1.5*x**2-6*x+5

polynome(5)

"""Implémenter la fonction factorielle (approche recursive)"""

def factorielle(n):
  if n == 0 : 
    return 1 
  if n == 1 : 
    return 1  
  elif n<0: 
    return print("insérer un nombre positif ")
  else : 
    return n*factorielle(n-1)

factorielle(-2)

"""Implémenter la fonction fibonnaci 

"""

n = int(input("Entrer un nombre entier supérieur à 1:"))

fibo0=0
fibo1=1

print("\n la suite fibonacci est :")
print(fibo0,",", fibo1,end=", ")

for i in range (2,n):
  i= fibo0+fibo1
  print(i, end=",")
  fibo0=fibo1
  fibo1=i