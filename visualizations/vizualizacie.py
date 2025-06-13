import matplotlib.pyplot as plt
import pandas as pd

def vykresli_bar_chart(data_dict):
    df = pd.DataFrame(data_dict)

    # Rozloženie údajov pre vizualizáciu
    kategorie = df['Úver']
    x = range(len(kategorie))

    bar_width = 0.1

    plt.figure(figsize=(14, 6))

    # Stĺpce
    plt.bar([p - 2.5*bar_width for p in x], df["Úrok plán (€)"], width=bar_width, label="Úrok plán", color="#e74c3c")
    plt.bar([p - 1.5*bar_width for p in x], df["Úrok real (€)"], width=bar_width, label="Úrok real", color="#3498db")
    plt.bar([p - 0.5*bar_width for p in x], df["Poistenie plán (€)"], width=bar_width, label="Poistenie plán", color="#9b59b6")
    plt.bar([p + 0.5*bar_width for p in x], df["Poistenie real (€)"], width=bar_width, label="Poistenie real", color="#95a5a6")
    plt.bar([p + 1.5*bar_width for p in x], df["Extra splátky (€)"], width=bar_width, label="Extra splátky", color="#f1c40f")
    plt.bar([p + 2.5*bar_width for p in x], df["Ušetrené spolu (€)"], width=bar_width, label="Ušetrené spolu", color="#2ecc71")

    # Popisy
    plt.xticks(x, kategorie)
    plt.xlabel("Úver")
    plt.ylabel("EUR")
    plt.title("Porovnanie plánovaných a reálnych hodnôt")
    plt.legend()
    plt.grid(True, axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()
