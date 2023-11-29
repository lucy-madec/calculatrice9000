def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Erreur : Division par zéro")

def calculatrice():
    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        operateur = input("Entrez l'opération (+, -, *, /) : ")
        nombre2 = float(input("Entrez le deuxième nombre : "))

        if operateur == '+':
            resultat = addition(nombre1, nombre2)
        elif operateur == '-':
            resultat = soustraction(nombre1, nombre2)
        elif operateur == '*':
            resultat = multiplication(nombre1, nombre2)
        elif operateur == '/':
            resultat = division(nombre1, nombre2)
        else:
            raise ValueError("Erreur : Opérateur invalide")

        print(f"Le résultat de {nombre1} {operateur} {nombre2} est : {resultat}")

    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    calculatrice()
