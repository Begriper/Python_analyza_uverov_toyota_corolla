import pandas as pd
import os
from tabulate import tabulate

def analyza_spolu():
    print("\n== Spúšťam: analysis/analyza_spolu.py ==\n")

    excel_path = os.path.join("data", "Moje_Uvery_Súčty.xlsx")

    plan_10k = pd.read_excel(excel_path, sheet_name='uver_10000_plan')
    real_10k = pd.read_excel(excel_path, sheet_name='uver_10000_real')

    plan_4k = pd.read_excel(excel_path, sheet_name='uver_4000_plan')
    real_4k = pd.read_excel(excel_path, sheet_name='uver_4000_real')

    def vypocitaj_udaje(plan, real):
        return {
            "Úrok plán (€)": round(plan["urok_plan"].sum(), 2),
            "Úrok real (€)": round(real["urok_real"].sum(), 2),
            "Ušetrené úrok (€)": round(plan["urok_plan"].sum() - real["urok_real"].sum(), 2),
            "Poistenie plán (€)": round(plan["poistenie_plan"].sum(), 2),
            "Poistenie real (€)": round(real["poistenie_real"].sum(), 2),
            "Ušetrené poistenie (€)": round(plan["poistenie_plan"].sum() - real["poistenie_real"].sum(), 2),
            "Extra splátky (€)": round(real["extra_splatka"].sum(), 2),
            "Mesiace plán": len(plan),
            "Mesiace real": len(real),
            "Skrátené mesiace": len(plan) - len(real),
            "Ušetrené spolu (€)": round(
                (plan["urok_plan"].sum() - real["urok_real"].sum()) +
                (plan["poistenie_plan"].sum() - real["poistenie_real"].sum()), 2
            )
        }

    udaje_10k = vypocitaj_udaje(plan_10k, real_10k)
    udaje_4k = vypocitaj_udaje(plan_4k, real_4k)

    df = pd.DataFrame([udaje_10k, udaje_4k], index=["10 000 €", "4 000 €"])

    print("\n=== 💡 Súhrnná tabuľka plán vs. realita ===\n")
    print(tabulate(df, headers="keys", tablefmt="fancy_grid"))

    return df
