import pandas as pd


def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Supprime les lignes entièrement vides du DataFrame."""
    avant = len(df)
    df = df.dropna(how="all")
    apres = len(df)
    print(f"✅ Lignes vides supprimées : {avant - apres} ligne(s) retirée(s)")
    return df