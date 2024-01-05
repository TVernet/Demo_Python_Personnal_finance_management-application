import csv

from Data.data_library import expense
from Data.data_library import income


# Writing to a csv file
def csv_export_option():
    export_option = input("\nDésirez vous effectuer un export .csv ? \n").lower()
    if export_option == "oui":
        with open(
            "Finances personnelles.csv", "w", newline="", encoding="utf-8"
        ) as csv_file:
            csv_object = csv.writer(csv_file)
            csv_object.writerow(["Type de donnée", "Nom de la donnée", "Montant"])

            # writing incomes
            for key, value in income.items():
                csv_object.writerow(["Revenus", key, value])

            # writing expenses
            for key, value in expense.items():
                csv_object.writerow(["Dépenses", key, value])

            print("Export .csv réalisé avec succès")
    elif export_option == "non":
        pass
    else:
        pass
