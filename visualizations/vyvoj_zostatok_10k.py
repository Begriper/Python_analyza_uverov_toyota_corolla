# visualizations/vyvoj_zostatok_10k.py

import pandas as pd
import matplotlib.pyplot as plt
from utils.paths import EXCEL_PATH

print("\n== Spúšťam: visualizations\\vyvoj_zostatok_10k.py ==")

# Načítanie dát
real = pd.read_excel(EXCEL_PATH, sheet_name='uver_10000_real')

# Výpis stĺpcov pre kontrolu
print("Stĺpce v realite:", real.columns)

# Výber dát
zostatky = real['zostatok_real']
extra = real['extra_splatka']
mesiace = list(range(1, len(zostatky) + 1))

# Vizualizácia
plt.figure(figsize=(12, 6))
plt.plot(mesiace, zostatky, marker='o', label='Zostatok úveru (€)')
plt.bar(mesiace, extra, label='Extra splátky (€)', alpha=0.5)

# Úprava grafu
plt.title("Vývoj zostatku a extra splátok – Úver 10 000 €")
plt.xlabel("Mesiac")
plt.ylabel("Suma (€)")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Zobrazenie
plt.show()
