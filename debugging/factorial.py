#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # <- On décrémente n à chaque itération
    return result

# Vérifier qu'un argument a été fourni
if len(sys.argv) < 2:
    print("Usage: python3 script.py <non-negative integer>")
    sys.exit(1)

# Convertir l'argument en entier
try:
    num = int(sys.argv[1])
    if num < 0:
        raise ValueError("Number must be non-negative")
except ValueError as e:
    print("Invalid input:", e)
    sys.exit(1)

# Calculer et afficher la factorielle
f = factorial(num)
print(f)
