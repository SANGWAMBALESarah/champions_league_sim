✅ 1. Importations
python
Copier
Modifier
import random
import json
random : permet de générer des nombres aléatoires.

json : permet d’enregistrer et de lire des données au format JSON (très utilisé pour stocker des données dans des fichiers).

✅ 2. Fonction creer_equipes()
python
Copier
Modifier
def creer_equipes():
    equipes = []
    for i in range(1, 33):
        equipe = {
            "nom": f"Équipe {i}",
            "force": random.randint(50, 100)
        }
        equipes.append(equipe)
    return equipes
Cette fonction crée une liste de 32 équipes. Chaque équipe est un dictionnaire avec :

"nom" : par exemple "Équipe 1", "Équipe 2", etc.

"force" : un nombre aléatoire entre 50 et 100 (représente la puissance ou compétence de l’équipe).

👉 Elle retourne une liste de 32 dictionnaires, chaque dictionnaire représentant une équipe.

✅ 3. Fonction sauvegarder_equipes()
python
Copier
Modifier
def sauvegarder_equipes(equipes, filename="equipes.json"):
    with open(filename, "w") as f:
        json.dump(equipes, f, indent=4)
Cette fonction :

Prend la liste equipes générée par creer_equipes() et un nom de fichier (par défaut "equipes.json").

Elle enregistre les équipes dans un fichier JSON, donc tu pourras les retrouver même après avoir fermé ton programme.

✅ 4. Fonction charger_equipes()
python
Copier
Modifier
def charger_equipes(filename="equipes.json"):
    with open(filename, "r") as f:
        return json.load(f)
Cette fonction :

Ouvre le fichier "equipes.json" (ou un autre nom si tu précises).

Elle charge les données JSON et les transforme à nouveau en une liste Python (chaque élément est un dictionnaire d’équipe).

📌 En résumé
Ce code sert à :

Créer 32 équipes avec une force aléatoire.

Sauvegarder ces équipes dans un fichier JSON.

Recharger ces équipes plus tard depuis le fichier.