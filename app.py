import streamlit as st
import pandas as pd
from excel_cleaner.cleaner import clean
from io import BytesIO


st.title("🧹 Excel Cleaner")
st.write("Upload ton fichier Excel et télécharge la version nettoyée.")

fichier = st.file_uploader("Choisis un fichier Excel", type=["xlsx"])

if fichier:
    df_avant = pd.read_excel(fichier)
    st.subheader("📄 Données brutes")
    st.dataframe(df_avant)

    if st.button("Nettoyer"):
        df_apres = clean(df_avant.copy())

        st.subheader("✅ Données nettoyées")
        st.dataframe(df_apres)

        buffer = BytesIO()
        df_apres.to_excel(buffer, index=False)
        buffer.seek(0)

        st.download_button(
            label="⬇️ Télécharger le fichier nettoyé",
            data=buffer,
            file_name="fichier_nettoye.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )