from taxwise.control.taxcalculator import TaxCalculator
from taxwise.persistence.taxbracketDAO import TaxBracketDAO
from taxwise.control.canada_tax_calculator import CanadaTaxCalculator
from taxwise.control.quebec_tax_calculator import QuebecTaxCalculator


class UI:
    def __init__(self):
        pass

    def run(self):
        print(
            "Hi, please input the province that you want to calculate your taxes for, or type canada for federal taxes")
        province = input()
        print("How much money did you make this year?")
        income = float(input())
        if province == "canada":
            tax_calculator = CanadaTaxCalculator()
        else:
            tax_calculator = QuebecTaxCalculator()
        tax = tax_calculator.calculate_tax(income)
        print(f"The amount of tax to pay is: {tax}")
        print(f"The applicable brackets are :")
        for bracket in tax_calculator.fetch_applicable_brackets(income):
            print(bracket)


    def run2(self):
        income = 200000
        calculator = CanadaTaxCalculator()
        tax = calculator.calculate_tax(income)
        print(f"The amount of tax to pay is: {tax}")
        print(f"The applicable brackets are :")
        for bracket in calculator.fetch_applicable_brackets(income):
            print(bracket)

if __name__ == "__main__":
    ui = UI()
    ui.run()

