from taxwise.persistence.taxbracketDAO import TaxBracketDAO
from abc import ABC
from typing import List


class TaxCalculator2(ABC):
    def __init__(self):
        self.tax_bracket_dao = TaxBracketDAO()

    def calculate_tax(self,authority, amount: float) -> float:
        amount = amount - self.tax_bracket_dao.find_threshold(authority)
        applicable_brackets = self.tax_bracket_dao.find_applicable_brackets(authority.capitalize(),amount)
        tax = 0.0
        for bracket in applicable_brackets:
            if amount > bracket.max_income:
                tax = tax + (bracket.max_income - bracket.min_income) * bracket.tax_rate
            else:
                tax = tax + (amount - bracket.min_income) * bracket.tax_rate
        return tax

    def fetch_applicable_brackets(self,authority,amount):
        return self.tax_bracket_dao.find_applicable_brackets(authority.capitalize(),amount)

    def __str__(self):
        return f"TaxCalculator()"

    def show_tax_bracket(self, tax_bracket):
        return List[tax_bracket]