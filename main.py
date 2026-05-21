#!/usr/bin/env python3
"""Point d'entrée de l'application."""

from calculs.core import additionner, diviser, multiplier, soustraire


def main():
    print("=== Application de Calculs ===")
    print("=== Nouvelle version TP6 déployée automatiquement ===")
    print(f"2 + 3 = {additionner(2, 3)}")
    print(f"10 - 4 = {soustraire(10, 4)}")
    print(f"3 × 4 = {multiplier(3, 4)}")
    print(f"8 / 2 = {diviser(8, 2)}")


if __name__ == "__main__":
    main()
