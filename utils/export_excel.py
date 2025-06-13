import pandas as pd
import os

def exportuj_do_excelu(dataframe, filename="suhrny_report.xlsx", sheet_name="Súhrnná Analýza"):
    output_dir = "vystupy"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        dataframe.to_excel(writer, index=True, sheet_name=sheet_name)

        workbook  = writer.book
        worksheet = writer.sheets[sheet_name]

        # Formátovanie hlavičky
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'valign': 'top',
            'align': 'center',
            'fg_color': '#D7E4BC',
            'border': 1
        })

        for col_num, value in enumerate(dataframe.columns.insert(0, dataframe.index.name or '')):
            worksheet.write(0, col_num, value, header_format)

        # Auto šírka stĺpcov
        for i, col in enumerate(dataframe.reset_index().columns):
            max_len = max([len(str(s)) for s in dataframe.reset_index()[col].values] + [len(str(col))]) + 2
            worksheet.set_column(i, i, max_len)
