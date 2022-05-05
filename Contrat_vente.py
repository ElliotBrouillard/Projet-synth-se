from Auto import *
from Camion import *
class Contrat_vente(Auto, Camion):
    def __init__(self, p_nb_paiements=0, p_clauses="", p_Véhicule=Véhicule()):
        self.nb_paiements=p_nb_paiements
        self.clauses=p_clauses
        self.Véchicule=p_Véhicule

    def _set_prix(self,p_prix):
        if Auto.type=="berline compacte":
            p_prix>=20000
        elif Auto.type=="berline intermédiaire":
            p_prix>=30000
        elif Auto.type=="berline pleine grandeur":
            if Auto.marque=="Volkswagen" and Auto.modèle=="Arteon":
                p_prix>=50000
            elif Auto.marque=="Toyota" and Auto.modèle=="Avalon"

    def Paiement(self, p_prix, p_nb_paiements):
        paiement_mensuel=p_prix/p_nb_paiements
        return paiement_mensuel

