import os

# === ANALÝZA SPOLU ===
print("\n== ANALÝZA SPOLU ==")
from analysis.analyza_spolu import analyza_spolu
df_spolu = analyza_spolu()

# === ANALÝZA ÚVERU 10 000 € ===
print("\n== ANALÝZA ÚVERU 10 000 € ==")
from analysis.analyza_uveru_10k import analyza_uveru_10k
analyza_uveru_10k()

# === ANALÝZA ÚVERU 4 000 € ===
print("\n== ANALÝZA ÚVERU 4 000 € ==")
from analysis.analyza_uveru_4k import analyza_uveru_4k
analyza_uveru_4k()

# === BAR CHART – Porovnanie hodnôt ===
print("\n== BAR CHART – Porovnanie hodnôt ==")
exec(open("visualizations/vizualizacie.py", encoding="utf-8").read())

# === ÚROKOVÉ TRENDY 10K & 4K ===
print("\n== ÚROKOVÉ TRENDY 10K & 4K ==")
exec(open("visualizations/vyvoj_uroku_10k.py", encoding="utf-8").read())
exec(open("visualizations/vyvoj_uroku_4k.py", encoding="utf-8").read())

# === ZOSTATKY & EXTRA SPLÁTKY 10K & 4K ===
print("\n== ZOSTATKY & EXTRA SPLÁTKY 10K & 4K ==")
exec(open("visualizations/vyvoj_zostatok_10k.py", encoding="utf-8").read())
exec(open("visualizations/vyvoj_zostatok_4k.py", encoding="utf-8").read())

# === SUBGRAFY 10K & 4K ===
print("\n== SUBGRAFY 10K & 4K ==")
exec(open("visualizations/subgraf_10k.py", encoding="utf-8").read())
exec(open("visualizations/subgraf_4k.py", encoding="utf-8").read())

# === EXPORT DO EXCELU ===
from utils.export_excel import exportuj_do_excelu
exportuj_do_excelu(df_spolu, filename="suhrny_report.xlsx", sheet_name="Súhrnná Analýza")

print("\n✅ Všetko hotové. Výpočty a grafy úspešne dokončené.")
