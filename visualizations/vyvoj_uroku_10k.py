# visualizations/vyvoj_uroku_10k.py

import pandas as pd
import matplotlib.pyplot as plt
from utils.paths import EXCEL_PATH

print("\n== Spúšťam: visualizations\\vyvoj_uroku_10k.py ==")

# Načítanie dát
plan = pd.read_excel(EXCEL_PATH, sheet_name='uver_10000_plan')
real = pd.read_excel(EXCEL_PATH, sheet_name='uver_10000_real')

# Výpis stĺpcov pre kontrolu
print("Stĺpce v pláne:", plan.columns)
print("Stĺpce v realite:", real.columns)

# Výber mesačných úrokov
plan_uroky = plan['urok_plan']
real_uroky = real['urok_real']

# Počet mesiacov pre X-os
mesiace_plan = list(range(1, len(plan_uroky) + 1))
mesiace_real = list(range(1, len(real_uroky) + 1))

# Vizualizácia - trend úrokov v čase
plt.figure(figsize=(12, 6))
plt.plot(mesiace_plan, plan_uroky, marker='o', label='Úrok plán (€)')
plt.plot(mesiace_real, real_uroky, marker='o', label='Úrok realita (€)')

# Úprava grafu
plt.title("Vývoj úrokov v čase – Úver 10 000 €")
plt.xlabel("Mesiac")
plt.ylabel("Úrok (€)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
