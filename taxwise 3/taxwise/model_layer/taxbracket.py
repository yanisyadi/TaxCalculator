
class TaxBracket:

    def __init__(self, tax_rate, minimum, maximum):
        self.tax_rate = tax_rate
        self.min_income = minimum
        self.max_income = maximum

    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        return f"TaxBracket(min_income={self.min_income}, max_income={self.max_income}, tax_rate={self.tax_rate})"









