from taxwise.data_layer.data_store import Datastore
from taxwise.model_layer.taxauthority import TaxAuthority
from taxwise.model_layer.taxbracket import TaxBracket


class TaxBracketDAO:
    def __init__(self):
        self.db = Datastore()

    def find_all_brackets(self, name: str) -> list[TaxBracket]:
        for aut in self.db.tax_authorities:
            if aut.name == name:
                return aut.tax_brackets
        return []

    def find_applicable_brackets(self, name: str, amount) -> list[TaxBracket]:
        applicable_brackets = []
        all_brackets = []
        for aut in self.db.tax_authorities:
            if aut.name == name:
                all_brackets = aut.tax_brackets
        for br in all_brackets:
            if br.min_income <= amount:
                applicable_brackets.append(br)
        return applicable_brackets

    def find_threshold(self, name: str):
        for aut in self.db.tax_authorities:
            if aut.name == name:
                return aut.free_threshold
        return 0.0


    def __str__(self):
        return [TaxBracketDAO]
