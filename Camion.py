from Véhicule import *
class Camion(Véhicule):
    def __init__(self, p_nb_roues=0, p_nb_portes=0, p_prix=0, p_type_remorque=""):
        self.roues=p_nb_roues
        self.portes=p_nb_portes
        self.prix=p_prix
        self.type_remorque=p_type_remorque

