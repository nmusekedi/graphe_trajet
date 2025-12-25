import tkinter as tk
from tkinter import scrolledtext
from graph import creer_graphe
from search import dfs
from maps_api import tracer_trajet
from config import DEPART, ARRIVEE, ARRETS


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("🚗 TP IA – Graphe & Google Maps")
        self.geometry("800x600")
        self.configure(bg="#f4f4f4")

        self.create_widgets()

    def create_widgets(self):
        # Titre
        title = tk.Label(
            self,
            text="Trajet Rond-point Victoire → Gare Centrale",
            font=("Arial", 16, "bold"),
            bg="#f4f4f4"
        )
        title.pack(pady=10)

        # Bouton
        btn = tk.Button(
            self,
            text="Calculer le trajet",
            command=self.run,
            bg="#007acc",
            fg="white",
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        btn.pack(pady=10)

        # Zone texte
        self.output = scrolledtext.ScrolledText(
            self,
            width=90,
            height=25,
            font=("Consolas", 10)
        )
        self.output.pack(padx=10, pady=10)

    def run(self):
        self.output.delete(1.0, tk.END)

        # Graphe
        graphe = creer_graphe()
        # Utiliser les noms courts qui correspondent au graphe
        depart_graphe = "Rond-point Victoire"
        arrivee_graphe = "Gare Centrale"
        chemin = dfs(graphe, depart_graphe, arrivee_graphe)

        self.output.insert(tk.END, "🧠 CHEMIN TROUVÉ PAR LE GRAPHE :\n\n")
        for etape in chemin:
            self.output.insert(tk.END, f"{etape}\n")

        self.output.insert(tk.END, "\n📍 TRAJET GOOGLE MAPS :\n\n")

        etapes_maps = tracer_trajet(DEPART, ARRIVEE, ARRETS)
        for depart, arrivee in etapes_maps:
            self.output.insert(tk.END, f"{depart} → {arrivee}\n")
