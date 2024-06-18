from Data.data_management import management
from Data.Calculation import Calculation
from display_ratio_expenses_category import statement_of_expenses
from export_option import csv_export_option


def main_func():
    print("Bonjour ! \n")

    # asks if the user wants to manage his data. 
    #If so, he'll be asked to choose the type of action he wants to take: 
    #add data, delete data, list data or skip this step.
    management()

    # Create an instance of the Calculation class to display the data table
    calc = Calculation()

    # Calculates and displays total income and expenses
    calc.tt_income()
    calc.tt_expense()

    # Displays a warning if expenses are too high
    calc.overspending()

    # Display debt ratio
    calc.indebtedness()

    # Displays savings capacity
    calc.cash_flow()

    # Display statement of expenses
    statement_of_expenses()

    # Offers csv export 
    csv_export_option()

    # Propose another action
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
