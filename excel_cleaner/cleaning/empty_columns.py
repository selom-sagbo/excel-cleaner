import pandas as pd


def remove_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Supprime les colonnes entièrement vides du DataFrame."""
    avant = len(df.columns)
    df = df.dropna(axis=1, how="all")
    apres = len(df.columns)
    print(f"✅ Colonnes vides supprimées : {avant - apres} colonne(s) retirée(s)")
    return df