import random
import json
import time
import os
# Initialisation une seule fois du moteur TTS (meilleure performance)
import pyttsx3
engine = pyttsx3.init()

def lire_commentaire(commentaire):
    #Lit à voix haute le commentaire du match
    engine.say(commentaire)
    engine.runAndWait()

def effet_tir(equipe):
    #Effet visuel d'un tir au but
    print(f"{equipe['nom']} tire", end='' , flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print("⚙", end='', flush=True)
    print()

def sauvegarder_match(type_match, equipe1, equipe2, score1, score2, vainqueur):
    # Sauvegarder les résultats d'un match dans un fichier JSON
    data = {
        "type": type_match,
        "equipe1": equipe1["nom"],
        "equipe2": equipe2["nom"],
        "score1": score1,
        "score2": score2,
        "vainqueur": vainqueur ["nom"] if vainqueur else "Nul"
    }
    # Charger ou créer l'historique des matchs
    if os.path.exists("matchs.json"):
        with open("matchs.json","r", encoding="utf-8") as f:
            historique = json.load(f)
    else:
        historique = {"matchs":[]}
    historique["matchs"].append(data)
    with open("matchs.json", "w", encoding="utf-8") as f:
        json.dump(historique, f, indent=4, ensure_ascii=False)
    
def generer_commentaire(e1, e2, s1, s2):
    #Génère un commentaire basé sur le résultat du match
    if s1 > s2:
        return f"🏆{e1['nom']} bat {e2['nom']} sur le score de {s1} - {s2} !"
    elif s2 > s1:
        return f"🏆{e2['nom']} bat {e1['nom']} sur le score de {s2}-{s1} !"
    else:
return f"🤝 Match nul entre {e1['nom']} et {e2['nom']} ({s1}-{s2})"

def simuler_match(equipe1, equipe2):
    #Simule un match entre deux équipes et retiurne les scores
    force1 = equipe1['force']
    force2 = equipe2['force']
    #Calcule des scores en fonction de la force divisé par 20, limité à 5 buts max  
    score_max1 = max(0, min(5, round(force1 / 20)))
    score_max2 = max(0, min(5, round(force2 / 20)))

    score1 = random.randint(0, score_max1)
    score2 = random.randint(0, score_max2)

    commentaire = generer_commentaire(equipe1, equipe2, score1,score2)
    print(commentaire)
    lire_commentaire(commentaire)

    if score1 > score2:
        vainqueur = equipe1
    elif score2 > score1:
        vainqueur = equipe2
    else:
        vainqueur = None
    sauvegarder_match("groupe" , equipe1, equipe2, score1, score2, vainqueur)
    return score1, score2

def simuler_tirs_au_but(equipe1, equipe2):
    #Simule une séance de tirs au but jusqu'à désigner un vainqueur
    print("⚔ Tirs au but !")
    score1 = 0
    score2 = 0

    for i in range(5):
        effet_tir(equipe1)
        if random.random() < 0.7:
            score1 += 1
            print("⚽ BUT !")
        else:
            print("❌ RATE !")
        effet_tir(equipe2)
        if random.random() < 0.7:
            score2 += 1
            print("⚽ BUT !")
        else:
            print("❌ RATE !")
    print(f"Tirs au but : {equipe1['nom']} {score1} - {score2} {equipe2['nom']}")
    if score1 > score2:
        return equipe1
    elif score2 > score1:
        return equipe2
    else:
        print("Round supplémentaire...")
        while True:
            effet_tir(equipe1)
            but1 = random.random() < 0.7
            print("⚽" if but1 else "❌")

            effet_tir(equipe2)
            but2 =random.random() < 0.7
            print("⚽" if but2 else "❌")

            if but1 != but2:
                return equipe1 if but1 else equipe2
def simuler_match_elimination(equipe1, equipe2):
    #Simule un match en phase élimination avec prolongations et tirs au but si nécessaire
    score1, score2 = simuler_match(equipe1, equipe2)

    if score1 == score2:
        print("Match nul, on passe aux tirs au but...")
        vainqueur = simuler_tirs_au_but(equipe1, equipe2)
    else :
            vainqueur = equipe1 if score1 > score2 else equipe2
        
    sauvegarder_match("elimination", equipe1, equipe2, score1, score2, vainqueur)
    return vainqueur
