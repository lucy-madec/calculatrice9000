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
        raise ValueError("Ne pas faire de division par zéro.")

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
            raise ValueError("Opérateur invalide")

        print(resultat)

    except ValueError:
        print("Entrée invalide.")
    except Exception:
        print("Une erreur inattendue s'est produite.")

calculatrice()