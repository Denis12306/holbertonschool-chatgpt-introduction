#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Vérification du nombre d'arguments
if len(sys.argv) != 2:
    print("Usage: ./factorial.py <non-negative integer>")
    sys.exit(1)

# Conversion et validation de l'argument
try:
    num = int(sys.argv[1])
    if num < 0:
        raise ValueError("Number must be non-negative")
except ValueError as e:
    print("Invalid input:", e)
    sys.exit(1)

# Calcul et affichage
print(factorial(num))
