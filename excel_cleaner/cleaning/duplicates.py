import pandas as pd


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Supprime les lignes dupliquées du DataFrame."""
    avant = len(df)
    df = df.drop_duplicates()
    apres = len(df)
    print(f"✅ Doublons supprimés : {avant - apres} ligne(s) retirée(s)")
    return df