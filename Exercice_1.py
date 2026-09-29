#Exercice 1 : Détermination de l'IMC (Indice de Masse Corporelle) en fonction de la masse et de la taille


def indice_de_masse_corporelle(masse,taille):

    """Calcule et affiche l'IMC à partir de la masse et de la taille."""

    imc = masse / taille**2

    print("IMC = {:0.1f}".format(imc))
    if imc <= 18.5:
        print("Valeur d'IMC indiquant une maigreur")
    elif 18.5 < imc <= 25 :
        print("Valeur d'IMC normal")
    elif 25 < imc <= 30 :
        print("Valeur d'IMC indiquant un surpoids")
    elif 30 < imc <= 40 :
        print("Valeur d'IMC indiquant un obésité")
    else :
        print("Valeur d'IMC indiquant une obésité massive")
    return imc

imc = indice_de_masse_corporelle(60, 1.80)
