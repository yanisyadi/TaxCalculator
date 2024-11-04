from taxwise.control.taxcalculator import TaxCalculator

class CanadaTaxCalculator(TaxCalculator):

    def __init__(self):
        super().__init__()

    def calculate_tax(self,amount: float) -> float:

        amount = amount - self.tax_bracket_dao.find_threshold("canada")
        applicable_brackets = self.tax_bracket_dao.find_applicable_brackets("canada".capitalize(),amount)
        tax = 0.0
        for bracket in applicable_brackets:
            if amount > bracket.max_income:
                tax = tax + (bracket.max_income - bracket.min_income) * bracket.tax_rate
            else:
                tax = tax + (amount - bracket.min_income) * bracket.tax_rate
        return tax

    def fetch_applicable_brackets(self,amount):
        return self.tax_bracket_dao.find_applicable_brackets('Canada'.capitalize(),amount)

