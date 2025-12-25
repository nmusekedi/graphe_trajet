from graph import creer_graphe
from search import dfs
from maps_api import tracer_trajet
from gui import Application
from config import DEPART, ARRIVEE, ARRETS

def main():
    graphe = creer_graphe()

    chemin = dfs(
        graphe,
        "Rond-point Victoire",
        "Gare Centrale"
    )

    print("🧠 Chemin trouvé par le graphe :")
    print(" → ".join(chemin))

    tracer_trajet(DEPART, ARRIVEE, ARRETS)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
