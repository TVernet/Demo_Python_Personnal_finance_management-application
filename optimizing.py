from Data.data_library import expense
from operator import mod


# Using decorators to give optimization advice linked to the output 
# of the Calculation.cash_flow() method
def optimization_advice(method):
    def wrapper(self):
        # call for original method
        target = method(self)
        # access to attributes of "self"
        if self.tt_cash_flow > mod(20, self.total_income):
            invest = int((self.tt_cash_flow * 100) / self.total_income)
            print(
                f"\n** Votre cash_flow est de {invest}%."
                "\n** Vous devriez penser à investir"
            )
        if self.tt_cash_flow < mod(20, self.total_income):
            hightest_expense = max(expense, key=expense.get)
            print(
                f"\n** Votre dépense la plus élevée est : {hightest_expense}."
                "\n** Envisagez une alternative sur ce poste de dépense"
            )
        if self.debt_ratio > mod(30, self.total_income):
            print(
                f"\n** Votre taux d'endettement est de {self.debt_ratio}%."
                "\n** Envisagez de prendre des mesures afin de ne pas atteindre les 35%"
            )
        else:
            pass

        return target

    return wrapper
