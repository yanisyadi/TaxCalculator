#revenu
#determiner le montant annuel d'impot --> credit d'impot, les taux d'imposition et le seuil de revenu non immposable
#donnee relative de l'autorite --> nom et seuil de revenu exonoere d"impot, tranche de taxation--> montant minimum et maximum soumis a l'impot
#montant de l'impot peut etre +,-
from typing import List

# 1er tax authority, tax bracket et tax calculator

from taxwise.model_layer.taxbracket import TaxBracket

class TaxAuthority:
    def __init__(self, name, free_threshold,):
        self.name = name
        self.free_threshold = free_threshold
        self.tax_brackets: List[TaxBracket]= []


    def add_tax_bracket(self, tax_bracket):
        self.tax_brackets.append(tax_bracket)

    def __str__(self):
        return f'TaxAuthority(name={self.name}, threshold={self.free_threshold}, tax_brackets={self.tax_brackets})'



