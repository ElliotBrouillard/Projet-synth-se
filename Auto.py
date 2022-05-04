from Véhicule import *
# déclaration de la classe
class Auto(Véhicule):
    def __init__(self, p_immatriculation=0, p_annee_fabrication=0, p_prix=0, p_nb_portes=4, p_nb_roues=4, p_freins="", p_moteur="", p_type=""):
        self.immatriculation=p_immatriculation
        self.annee_fabrication=p_annee_fabrication
        self.prix=p_prix
        self.nb_portes=p_nb_portes
