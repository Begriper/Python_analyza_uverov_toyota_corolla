import pandas as pd
import matplotlib.pyplot as plt
from utils.paths import EXCEL_PATH

print("\n== Spúšťam: visualizations\\subgraf_10k.py ==")

# Načítanie dát
plan = pd.read_excel(EXCEL_PATH, sheet_name='uver_10000_plan')
real = pd.read_excel(EXCEL_PATH, sheet_name='uver_10000_real')

# Výber dát
mesiace_plan = list(range(1, len(plan) + 1))
mesiace_real = list(range(1, len(real) + 1))
urok_plan = plan['urok_plan']
urok_real = real['urok_real']
zostatok_plan = plan['zostatok_plan']
zostatok_real = real['zostatok_real']
extra = real['extra_splatka']

# Vizualizácia v subgrafoch
fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Subgraf 1: Úroky
axs[0].plot(mesiace_plan, urok_plan, label='Úrok plán (€)', marker='o')
axs[0].plot(mesiace_real, urok_real, label='Úrok realita (€)', marker='o')
axs[0].set_title("Vývoj úroku – Úver 10 000 €")
axs[0].legend()
axs[0].grid(True)

# Subgraf 2: Zostatok
axs[1].plot(mesiace_plan, zostatok_plan, label='Zostatok plán (€)', marker='o')
axs[1].plot(mesiace_real, zostatok_real, label='Zostatok realita (€)', marker='o')
axs[1].set_title("Vývoj zostatku – Úver 10 000 €")
axs[1].legend()
axs[1].grid(True)

# Subgraf 3: Extra splátky
axs[2].bar(mesiace_real, extra, label='Extra splátky (€)', color='green')
axs[2].set_title("Mimoriadne splátky v čase")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()
