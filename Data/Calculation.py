from Data.data_library import expense
from Data.data_library import income
from optimizing import optimization_advice


class Calculation:
    # Performs all calculations on data entered
    def __init__(self) -> None:
        self.income_values = income.values()
        self.total_income = int(sum(self.income_values))
        self.expense_values = expense.values()
        self.total_expense = int(sum(self.expense_values))
        self.debt_ratio = int((self.total_expense / self.total_income) * 100)
        self.tt_cash_flow = int(self.total_income - self.total_expense)
        self.ratios = {
            key: value / self.total_expense for key, value in expense.items()
        }

    # Display total income
    def tt_income(self):
        print(f"\nTotal revenus = {self.total_income} € par an")
        print(f"Total revenus = {int(self.total_income/12)} € par mois")

    # Display total expense
    def tt_expense(self):
        print(f"\nTotal dépenses = {self.total_expense} € par an")
        print(f"Total dépenses = {int(self.total_expense/12)} € par mois")

    # Display alert if overspending
    def overspending(self):
        if self.total_expense > self.total_income:
            print("\n!! ATTENTION, VOUS AVEZ TROP DE DÉPENSES POUR VOS REVENUS !!")

    # Display debt ratio
    def indebtedness(self):
        print(f"\nTaux d'endettement = {self.debt_ratio} %")

    # Display cash flow calculation
    @optimization_advice
    def cash_flow(self):
        print(f"\nCash flow annuel = {self.tt_cash_flow} €")
        print(f"Cash flow mensuel = {int(self.tt_cash_flow/12)} €")

    # Display expenses by category
    def expenses_category(self):
        return self.ratios
