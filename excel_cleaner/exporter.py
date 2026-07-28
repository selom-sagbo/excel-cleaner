import pandas as pd
from pathlib import Path


def export_excel(df: pd.DataFrame, output_path: str) -> None:
    """Exporte le DataFrame nettoyé vers un fichier Excel."""
    try:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        df.to_excel(output_path, index=False)
        print(f"✅ Fichier exporté : {output_path}")
    except Exception as e:
        print(f"❌ Erreur lors de l'export : {e}")
        raise