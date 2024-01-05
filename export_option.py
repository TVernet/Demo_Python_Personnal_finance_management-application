import csv

from Data.data_library import expense
from Data.data_library import income

# si tourne dans une app web, transmettre le document au client du serveur
# (navigateur web de l'utilisateur) pour téléchargement. Dans ce cas utiliser
#  'Flask' ou 'Django'. Exemple :
# from flask import Flask, send_file
# app = Flask(__name__
# @app.route('/download-csv')
# def download_csv():
#     # création du fichier CSV
#     csv_export_option()
#     # Envoi du fichier pour téléchargement
#     return send_file("Finances personnelles.csv", as_attachment=True)


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
