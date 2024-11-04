from taxwise.persistence.taxbracketDAO import TaxBracketDAO
from abc import ABC



class TaxCalculator(ABC):
    def __init__(self):
        self.tax_bracket_dao = TaxBracketDAO()

    def calculate_tax(self, amount: float) -> float:
        pass

    def __str__(self):
        return f"TaxCalculator()"

