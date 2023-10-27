class CCarte:
    def __init__(self, valeur, forme):
        self.valeur = valeur
        self.forme = forme

    def __str__(self):
        return f"{self.valeur} de {self.forme}"


class CJeuDeCartes:
    formes = ["Coeur", "Carreau", "Pique", "Trèfle"]
    valeurs = ["As", "2", "3", "4", "5", "6", "7",
               "8", "9", "10", "Valet", "Dame", "Roi"]

    def __init__(self):
        self.cartes = [CCarte(valeur, forme)
                       for forme in CJeuDeCartes.formes 
                       for valeur in CJeuDeCartes.valeurs]

    def nom_carte(self, carte):
        return str(carte)

    def battre(self):
        random.shuffle(self.cartes)

    def afficher(self):
        for carte in self.cartes:
            print(self.nom_carte(carte))

    def tirer(self):
        return self.cartes.pop()
