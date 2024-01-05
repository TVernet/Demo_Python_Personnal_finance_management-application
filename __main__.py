from Data.data_management import management
from Data.Calculation import Calculation
from display_ratio_expenses_category import statement_of_expenses
from export_option import csv_export_option


def main_func():
    print("Bonjour ! \n")

    # Asks if user wants to manage data
    management()

    # Create an instance of the Calculation class
    calc = Calculation()

    # Calculating total income and expenses
    calc.tt_income()
    calc.tt_expense()

    # Warning if expenses are too high
    calc.overspending()

    # Debt ratio
    calc.indebtedness()

    # saving capacity
    calc.cash_flow()

    # Statement of expenses
    statement_of_expenses()

    # csv export option
    csv_export_option()

    # other action
    other_action = input("\nVoulez-vous effectuer une autre action ? \n")
    if other_action == "oui":
        return main_func()
    else:
        pass

    # End of script
    print("\nBonne journée ! \n")


# main function
if __name__ == "__main__":
    main_func()
