from Auto import *
# déclaration de la classe
class Véhicule:
    def __init__(self, p_roues=0, p_immatriculation="", p_annee_fabrication=0, p_prix=0):
        self.roues=p_roues
        self.immatriculation=p_immatriculation
        self.annee_fabrication=p_annee_fabrication
        self.prix=p_prix

    def _get_prix(self, p_prix):
        return p_prix

    def _set_prix(self, p_prix):
        if Auto.type == "berline compacte":
            p_prix>=20000
        elif Auto.type=="berline intermédiaire":
            p_prix>=30000
        elif Auto.type=="berline pleine grandeur":
            if Auto.marque=="Volkswagen" and Auto.modèle=="Arteon":
                p_prix>=50000
            elif Auto.marque=="Toyota" and Auto.modèle=="Avalon":
                p_prix>=45000


    def __str__(self):
        chaine=" "*60+"\n"+"*"*60+"\n\n"+"   Le nombre de roues : "+str(self.roues)+"\n"+\
            " L'immatriculation du véhicule : "+self.immatriculation+"\n"+" L'annee de fabrication : "+\
            +str(self.annee_fabrication)
        return chaine
