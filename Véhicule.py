# déclaration de la classe
class Véhicule:
    def __init__(self, p_roues=0, p_immatriculation=0, p_annee_fabrication=0, p_prix=0):
        self.roues=p_roues
        self.immatriculation=p_immatriculation
        self.anne_fabrication=p_annee_fabrication
        self.prix=p_prix


    def Démarrer(self):
        print("Le véhicule démarre")

    def Accélérer(self):
        print("Le véhicule accélère")

    def __str__(self):
        chaine=" "*60+"\n"+"*"*60+"\n\n"+"   Le nombre de roues : "+self.roues+"\n"+\
            " L'immatriculation du véhicule : "+self.immatriculation
