import pandas as pd

def courbe_verticale(pente1, pente2, longueur, elevation_pcr, pas):
    """
    Calcule une courbe verticale pour une route.
    """
    pente1_ratio = pente1 / 100
    pente2_ratio = pente2 / 100
    changement_pente = pente2_ratio - pente1_ratio
    K = changement_pente / longueur
    debut_courbe_distance = -longueur / 2
    fin_courbe_distance = longueur / 2
    elevation_debut_courbe = elevation_pcr + pente1_ratio * debut_courbe_distance
    elevation_fin_courbe = elevation_pcr + pente2_ratio * fin_courbe_distance
    elevation_pcr_debut = elevation_pcr + pente1_ratio * (debut_courbe_distance)
    elevation_pcr_fin = elevation_pcr + pente2_ratio * (fin_courbe_distance)
    points = []
    x = debut_courbe_distance
    while x <= fin_courbe_distance:
        elevation_courbe = (
            elevation_pcr_debut +
            pente1_ratio * (x - debut_courbe_distance) +
            0.5 * K * (x - debut_courbe_distance)**2
        )
        elevation_pente = (
            elevation_pcr + pente1_ratio * x
            if x <= 0 else
            elevation_pcr + pente2_ratio * x
        )
        distance_label = (
            f"DC" if x == debut_courbe_distance else
            f"FC" if x == fin_courbe_distance else
            f"{x:.1f}"
        )
        points.append({
            'Distance': x,
            'Élévation_courbe(m)': elevation_courbe,
            'Élévation_pente(m)': elevation_pente
        })

        # Incrémenter la distance
        x += pas
    if not any(point['Distance'] == 0.0 for point in points):
        elevation_courbe_0 = (
            elevation_pcr_debut +
            pente1_ratio * (0 - debut_courbe_distance) +
            0.5 * K * (0 - debut_courbe_distance)**2
        )
        points.append({
            'Distance': 0.0,
            'Élévation_courbe(m)': elevation_courbe_0,
            'Élévation_pente(m)': elevation_pcr
        })

    points = sorted(points, key=lambda p: p['Distance'])

    return pd.DataFrame(points)