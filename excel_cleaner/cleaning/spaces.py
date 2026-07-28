import pandas as pd


def remove_extra_spaces(df: pd.DataFrame) -> pd.DataFrame:
    """Supprime les espaces en trop dans les cellules texte."""
    colonnes_texte = df.select_dtypes(include="object").columns
    
    for colonne in colonnes_texte:
        df[colonne] = df[colonne].str.strip()
    
    print(f"✅ Espaces nettoyés sur {len(colonnes_texte)} colonne(s) texte")
    return df