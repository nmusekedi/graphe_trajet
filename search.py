def dfs(graphe, debut, fin, chemin=None):
    if chemin is None:
        chemin = []

    chemin = chemin + [debut]

    if debut == fin:
        return chemin

    for voisin in graphe[debut]:
        if voisin not in chemin:
            nouveau = dfs(graphe, voisin, fin, chemin)
            if nouveau:
                return nouveau
    return None
