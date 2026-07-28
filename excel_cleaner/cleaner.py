import pandas as pd
from excel_cleaner.cleaning.duplicates import remove_duplicates
from excel_cleaner.cleaning.empty_rows import remove_empty_rows
from excel_cleaner.cleaning.empty_columns import remove_empty_columns
from excel_cleaner.cleaning.spaces import remove_extra_spaces
from excel_cleaner.cleaning.casing import normalize_casing


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Orchestre toutes les étapes de nettoyage."""
    print("\n🧹 Début du nettoyage...\n")

    df = remove_empty_rows(df)
    df = remove_empty_columns(df)
    df = remove_duplicates(df)
    df = remove_extra_spaces(df)
    df = normalize_casing(df)

    print("\n✅ Nettoyage terminé !\n")
    return df