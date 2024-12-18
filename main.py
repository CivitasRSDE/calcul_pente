import streamlit as st
from courbe_verticale import courbe_verticale
import matplotlib.pyplot as plt

st.title("Résultats de la courbe verticale:")


pente1 = st.text_input(label = "Entrez la pente en % de la première rue (ex. 2 pour 2%):")
pente2 = st.text_input(label = "Entrez la pente en % de la seconde rue (ex. -3 pour -3%):")
longueur = st.text_input(label = "Entrez la longueur de la courbe verticale (en mètres):")
elevation_pcr = st.text_input(label = "Entrez l'élévation au pofloat de rencontre des pentes (en mètres):")
pas = st.text_input(label = "Entrez le pas souhaité pour les calculs (en mètres, ex. 5):")


if st.button("Lancer"):
    df = courbe_verticale(float(pente1), float(pente2), float(longueur), float(elevation_pcr), float(pas))
    fig, ax = plt.subplots()
    ax.plot(df['Distance'], df['Élévation_courbe(m)'], label='Courbe verticale', linewidth=2)
    ax.plot(df['Distance'], df['Élévation_pente(m)'], label='Élévation pente', linestyle='--', color='orange')

    ax.set_title("Courbe Verticale")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Élévation (m)")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)
    st.dataframe(df)


              