import pandas as pd


def normalize_casing(df: pd.DataFrame) -> pd.DataFrame:
    """Uniformise le texte en mettant la première lettre en majuscule."""
    colonnes_texte = df.select_dtypes(include="object").columns

    for colonne in colonnes_texte:
        df[colonne] = df[colonne].str.capitalize()

    print(f"✅ Casse uniformisée sur {len(colonnes_texte)} colonne(s) texte")
    return df