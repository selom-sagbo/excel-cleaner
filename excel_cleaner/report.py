import pandas as pd


def generate_report(df_avant: pd.DataFrame, df_apres: pd.DataFrame) -> None:
    """Affiche un rapport comparatif avant/après nettoyage."""
    print("\n" + "=" * 40)
    print("📊 RAPPORT DE NETTOYAGE")
    print("=" * 40)
    print(f"Lignes avant    : {df_avant.shape[0]}")
    print(f"Lignes après    : {df_apres.shape[0]}")
    print(f"Lignes retirées : {df_avant.shape[0] - df_apres.shape[0]}")
    print("-" * 40)
    print(f"Colonnes avant  : {df_avant.shape[1]}")
    print(f"Colonnes après  : {df_apres.shape[1]}")
    print(f"Colonnes retirées: {df_avant.shape[1] - df_apres.shape[1]}")
    print("=" * 40 + "\n")