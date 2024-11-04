from typing import List

from taxwise.model_layer.taxauthority import TaxAuthority
from taxwise.model_layer.taxbracket import TaxBracket


class Datastore:
    def __init__(self):
        self.tax_authorities: List[TaxAuthority] = []
        self.add_canada_brackets()
        self.add_quebec_brackets()

    def add_canada_brackets(self):
        canada = TaxAuthority('Canada', 15705)
        canada.add_tax_bracket(TaxBracket(0.15, 15705, 55867))
        canada.add_tax_bracket(TaxBracket(0.205, 55867, 111733))
        canada.add_tax_bracket(TaxBracket(0.26, 111733, 173207))
        canada.add_tax_bracket(TaxBracket(0.29, 173207, 246752))
        canada.add_tax_bracket(TaxBracket(0.33, 246752, float('inf')))

        self.tax_authorities.append(canada)

    def add_quebec_brackets(self):
        quebec = TaxAuthority('Quebec', 17183)
        quebec.add_tax_bracket(TaxBracket(0.14, 17183, 51780))
        quebec.add_tax_bracket(TaxBracket(0.19, 51780, 103545))
        quebec.add_tax_bracket(TaxBracket(0.24, 103545, 126000))
        quebec.add_tax_bracket(TaxBracket(0.2575, 126000, float('inf')))

        self.tax_authorities.append(quebec)

    def __str__(self):
        return f'bracket(tax_authorities={self.tax_authorities})'