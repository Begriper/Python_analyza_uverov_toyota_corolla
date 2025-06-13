import pandas as pd
import os

def analyza_uveru_4k():
    print("\n== Spúšťam: analysis/analyza_uveru_4k.py ==")

    excel_path = os.path.join("data", "Moje_Uvery_Súčty.xlsx")
    plan = pd.read_excel(excel_path, sheet_name='uver_4000_plan')
    real = pd.read_excel(excel_path, sheet_name='uver_4000_real')

    urok_plan = round(plan["urok_plan"].sum(), 2)
    urok_real = round(real["urok_real"].sum(), 2)
    usetrene_urok = round(urok_plan - urok_real, 2)

    poist_plan = round(plan["poistenie_plan"].sum(), 2)
    poist_real = round(real["poistenie_real"].sum(), 2)
    usetrene_poist = round(poist_plan - poist_real, 2)

    extra = round(real["extra_splatka"].sum(), 2)
    skratenie = len(plan) - len(real)

    print("\n------ Úver 4 000 € ------")
    print(f"Úrok plán: {urok_plan} €, realita: {urok_real} €, ušetrené: {usetrene_urok} €")
    print(f"Poistenie plán: {poist_plan} €, realita: {poist_real} €, ušetrené: {usetrene_poist} €")
    print(f"Extra splátky spolu: {extra} €")
    print(f"Skrátenie splácania: o {skratenie} mesiacov")

    return {
        "urok_plan": urok_plan, "urok_real": urok_real, "usetrene_urok": usetrene_urok,
        "poistenie_plan": poist_plan, "poistenie_real": poist_real, "usetrene_poistenie": usetrene_poist,
        "extra_splatky": extra, "skratenie_mesiace": skratenie
    }
