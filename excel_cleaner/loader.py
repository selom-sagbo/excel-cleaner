import pandas as pd


def load_excel(filepath: str) -> pd.DataFrame:
    """Charge un fichier Excel et retourne un DataFrame."""
    try:
        df = pd.read_excel(filepath)
        print(f"✅ Fichier chargé : {filepath}")
        print(f"   {df.shape[0]} lignes | {df.shape[1]} colonnes")
        return df
    except FileNotFoundError:
        print(f"❌ Fichier introuvable : {filepath}")
        raise
    except Exception as e:
        print(f"❌ Erreur lors du chargement : {e}")
        raise