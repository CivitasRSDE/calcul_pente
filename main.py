import streamlit as st
from courbe_verticale import courbe_verticale

st.title("Résultats de la courbe verticale:")


pente1 = st.text_input(label = "Entrez la pente en % de la première rue (ex. 2 pour 2%):")
pente2 = st.text_input(label = "Entrez la pente en % de la seconde rue (ex. -3 pour -3%):")
longueur = st.text_input(label = "Entrez la longueur de la courbe verticale (en mètres):")
elevation_pcr = st.text_input(label = "Entrez l'élévation au pofloat de rencontre des pentes (en mètres):")
pas = st.text_input(label = "Entrez le pas souhaité pour les calculs (en mètres, ex. 5):")


if st.button("Lancer"):
    st.dataframe(data = courbe_verticale(float(pente1), float(pente2), float(longueur), float(elevation_pcr), float(pas)))
    st.line_chart(data = courbe_verticale(float(pente1), float(pente2), float(longueur), float(elevation_pcr), float(pas)),
                  x = "Distance", 
                  y = ["Élévation_courbe(m)","Élévation_pente(m)"],
                  use_container_width=True)


              