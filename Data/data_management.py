from Data.data_library import expense
from Data.data_library import income

import re


def management():
    # User data management
    while True:
        user_action = input(
            "Voulez-vous effectuer des opérations sur vos données ? \n"
            "Renseignez votre besoin : ajouter des données, supprimer des données, les lister ou passer \n"
        ).lower()
        # Adding data
        if "ajo" in user_action:
            add_type = input(
                "Quelle type d'ajout souhaitez vous faire ? Dépenses ou revenus \n"
            ).lower()
            # Adding expense data
            if re.search(r"dép|dep", add_type):
                name_expense = input("Saisissez le nom de votre nouvelle dépense : \n")
                amount_expense = int(
                    input("Saisissez le montant annuel de votre nouvelle dépense : \n")
                )
                expense[name_expense] = amount_expense
                print(
                    f"{name_expense} d'un montant de {amount_expense}€ a été ajouté à vos dépenses \n"
                )
            # Adding income data
            elif "rev" in add_type:
                name_income = input("Saisissez le nom de votre nouveau revenu : \n")
                amount_income = int(
                    input("Saisissez le montant annuel de votre nouveau revenu : \n")
                )
                income[name_income] = amount_income
                print(
                    f"{name_income} d'un montant de {amount_income}€ a été ajouté à vos revenus \n"
                )
            # Error adding data
            else:
                if add_type == "":
                    print("Saisie incorrect \n")
                    return management()
        # Removing data
        elif "sup" in user_action:
            remove_type = input(
                "Quelle type de suppression souhaitez vous faire ? \n"
                "Dépenses ou revenus \n"
            ).lower()
            # Removing expense data
            if re.search(r"dép|dep", remove_type):
                remove_name_expense = input(
                    "Saisissez le nom de la dépense que vous voulez supprimer : \n"
                )
                if remove_name_expense in expense:
                    del expense[remove_name_expense]
                    print(
                        f"La dépense {remove_name_expense} a bien été supprimé de vos dépenses \n"
                    )
                else:
                    print("Le nom renseigné n'existe pas \n")
                    return management()
            # Removing income data
            elif "rev" in remove_type:
                remove_name_income = input(
                    "Saisissez le nom du revenu que vous voulez supprimer : \n"
                )
                if remove_name_income in income:
                    del income[remove_name_income]
                    print(
                        f"Le revenu {remove_name_income} a bien été supprimé de vos revenus \n"
                    )
                else:
                    print("Le nom renseigné n'existe pas \n")
                    return management()
        # List data
        elif "lis" in user_action:
            display_type = input(
                "Voulez-vous lister les dépenses annuelles, les revenus annuels ou l'ensemble des données ? \n"
            ).lower()
            if re.search(r"dép|dep", display_type):
                print(expense)
            elif "rev" in display_type:
                print(income)
            elif "ens" in display_type:
                print(expense, income)
            else:
                print("Choix invalide")
                return management()
        # No action required
        elif "pas" in user_action:
            break
        # Error action
        else:
            break
