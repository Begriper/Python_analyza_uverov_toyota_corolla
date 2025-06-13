# Python_analyza_uverov_toyota_corolla

Tento projekt je Python aplikácia, ktorú som vytvoril na reálnu analýzu mojich dvoch bankových úverov použitých na kúpu auta **Toyota Corolla** (2019/2020). Projekt umožňuje porovnať plánované a skutočné splátky, úroky, poistenie, zobraziť úspory vďaka extra splátkam, a vizualizovať vývoj splácania – všetko automaticky, rýchlo a prehľadne.

## Prečo tento projekt vznikol?

Pri kúpe auta som riešil predčasné splácanie úverov a sledoval rozdiely oproti pôvodným plánom banky. Viedol som si vlastné záznamy v Exceli a chcel som si vyskúšať spraviť **automatizovanú analytiku** a vizualizáciu dát v Pythone. V projekte som sa naučil prácu s pandas, grafmi a exportom do Excelu.

## Funkcionality

- **Načítanie dát** z Excelu (`data/Moje_Uvery_Súčty.xlsx`)
- **Automatický výpočet** rozdielov medzi plánovaným a reálnym splácaním
- **Prehľadná súhrnná tabuľka** (plán vs. realita, úspory, extra splátky, skracovanie splácania)
- **Export výsledkov do Excelu** (priečinok `vystupy/`, súbor `suhrny_report.xlsx`)
- **Vizualizácie**: vývoj úrokov, zostatkov, extra splátky a ďalšie grafy

## Štruktúra projektu

- **main.py** – hlavný spúšťací súbor
- **analysis/** – analýzy jednotlivých úverov aj spoločnej súhrnnej tabuľky
- **data/** – vstupné Excel dáta s vlastnými údajmi o splátkach
- **utils/** – pomocné funkcie, export do Excelu
- **visualizations/** – všetky grafy a vizualizácie (automaticky sa zobrazujú pri spustení)
- **vystupy/** – sem sa ukladá výsledný Excel súhrn
- **README.md** – tento popis

## Použité knižnice

- **pandas** – spracovanie dát
- **matplotlib** – vizualizácie
- **tabulate** – tlač súhrnných tabuliek v termináli
- **xlsxwriter** alebo **openpyxl** – export do Excelu

## Ako projekt používať

1. Skopíruj alebo naklonuj repozitár
2. Nainštaluj potrebné knižnice (príkaz `pip install -r requirements.txt`)
3. Priprav si vlastný Excel súbor v priečinku `data/` podľa vzoru
4. Spusti `main.py` (napr. vo VS Code alebo termináli príkazom `python main.py`)
5. Výsledky nájdeš v priečinku `vystupy/` a grafy sa zobrazia v oknách

## Moje skúsenosti a odporúčania

Projekt vznikol na reálnych dátach – kúpa Toyota Corolla, predčasné splácanie, úspory na úrokoch aj poistení. Je vhodný aj pre iných, ktorí chcú analyzovať svoje úvery, alebo si vyskúšať dátovú analytiku v Pythone. Odporúčam si pripraviť vlastné vstupné dáta v rovnakom formáte ako príklad.

Ak máš otázky alebo tipy na vylepšenie, napíš mi, rád si vypočujem spätnú väzbu!

---

Autor: František Stolár (Begriper), 2025
