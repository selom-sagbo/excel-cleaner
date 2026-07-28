import sys
from excel_cleaner.loader import load_excel
from excel_cleaner.cleaner import clean
from excel_cleaner.exporter import export_excel
from excel_cleaner.report import generate_report


def main():
    """Point d'entrée principal de l'application."""
    input_path = "data/input/test.xlsx"
    output_path = "data/output/test_nettoye.xlsx"

    # 1. Charger
    df_avant = load_excel(input_path)

    # 2. Nettoyer
    df_apres = clean(df_avant.copy())

    # 3. Exporter
    export_excel(df_apres, output_path)

    # 4. Rapport
    generate_report(df_avant, df_apres)


if __name__ == "__main__":
    main()