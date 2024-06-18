from Data.Calculation import Calculation

import matplotlib.pyplot as plt
import ascii_magic
from io import BytesIO


def statement_of_expenses():
    # Calculating expenditure by category
    calc = Calculation()
    ratios = calc.expenses_category()
    for category, ratio in ratios.items():
        display_ratio = f"{category}: {ratio:.2%}"
        print(f"\nDépenses par catégorie sur pourcentage total : {display_ratio}")

    # Print expenditure by category in ASCII Art
    ratios = calc.expenses_category()
    category = list(ratios.keys())
    values = list(ratios.values())
    fig, ax = plt.subplots(figsize=(3, 1))
    ax.pie(values, labels=category, startangle=140)
    ax.axis("equal")
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    ascii_img = ascii_magic.AsciiArt.from_image(buf)
    ascii_img.to_terminal(char=str("*"))
    buf.close()
    plt.close()
