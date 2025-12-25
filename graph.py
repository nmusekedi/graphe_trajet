def creer_graphe():
    """
    Graphe orienté représentant le trajet
    du Rond-point Victoire vers la Gare Centrale
    en passant par tous les arrêts possibles.
    """

    graphe = {
        "Rond-point Victoire": [
            "Rond Point Gambela/Kasa Vubu"
        ],

        "Rond Point Gambela/Kasa Vubu": [
            "Rond Point Kimpwanza"
        ],

        "Rond Point Kimpwanza": [
            "Enseignement"
        ],

        "Enseignement": [
            "Boulevard Triomphal"
        ],

        "Boulevard Triomphal": [
            "Av. de Kabinda"
        ],

        "Av. de Kabinda": [
            "Rond point huilerie"
        ],

        "Rond point huilerie": [
            "Rue de Kitega"
        ],

        "Rue de Kitega": [
            "Institut National de Recherche Biomédicale"
        ],

        "Institut National de Recherche Biomédicale": [
            "REGIDESO"
        ],

        "REGIDESO": [
            "Ecobank RDC"
        ],

        "Ecobank RDC": [
            "Poste SCPT"
        ],

        "Poste SCPT": [
            "KIN-MART"
        ],

        "KIN-MART": [
            "Gare Centrale"
        ],

        "Gare Centrale": []
    }

    return graphe
