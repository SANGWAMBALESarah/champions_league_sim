# team_manager.py
import random
import json


def creer_equipes():
    equipes = []
    for i in range(1, 33):
        equipe = {
            "nom": f"Équipe {i}",
            "force": random.randint(50, 100)
        }
        equipes.append(equipe)
    return equipes

def sauvegarder_equipes(equipes, filename="equipes.json"):
    with open(filename, "w") as f:
        json.dump(equipes, f, indent=4)

def charger_equipes(filename="equipes.json"):
    with open(filename, "r") as f:
        return json.load(f)