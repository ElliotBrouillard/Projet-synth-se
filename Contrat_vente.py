from Auto import *
class Contrat_vente(Auto):
    def __init__(self, p_prix=0, p_nb_paiements=0, p_clauses="", p_Véhicule=""):
        self.prix=p_prix
        self.nb_paiements=p_nb_paiements
        self.clauses=p_clauses
        self.Véchicule=p_Véhicule

    def _get_prix(self, p_prix):
        return p_prix

    def _set_prix(self,p_prix):

    def Paiement(self, p_prix, p_nb_paiements):
        paiement_mensuel=p_prix/p_nb_paiements