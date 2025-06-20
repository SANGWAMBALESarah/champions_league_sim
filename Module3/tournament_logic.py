# tournament_logic.py

import random
from collections import defaultdict

def tirer_groupes(equipes):
    random.shuffle(equipes)
    groupes = {chr(ord('A') + i): [] for i in range(8)}

    for idx, equipe in enumerate(equipes):
        groupe = chr(ord('A') + (idx // 4))
        groupes[groupe].append(equipe)

    return groupes


def calcul_classement_groupe(matchs, groupe_equipes):
    points = defaultdict(int)
    buts_pour = defaultdict(int)
    buts_contre = defaultdict(int)

    for match in matchs:
        e1 = match['equipe1']
        e2 = match['equipe2']
        score1, score2 = match["score"]

        buts_pour[e1] += score1
        buts_contre[e1] += score2
        buts_pour[e2] += score2
        buts_contre[e2] += score1

        if score1 > score2:
            points[e1] += 3
        elif score2 > score1:
            points[e2] += 3
        else:
            points[e1] += 1
            points[e2] += 1

    classement = sorted(
        groupe_equipes,
        key=lambda eq: (
            points.get(eq["nom"], 0),
            buts_pour.get(eq["nom"], 0) - buts_contre.get(eq["nom"], 0),
            buts_pour.get(eq["nom"], 0)
        ),
        reverse=True
    )
    return classement


def simuler_matches_groupes(groupes):
    from match_simulator import simuler_match

    resultats_groupes = {}

    for nom_groupe, equipes in groupes.items():
        print(f"\n🎮 Matchs du groupe {nom_groupe} :")
        matchs = []

        for i in range(len(equipes)):
            for j in range(i + 1, len(equipes)):
                e1 = equipes[i]
                e2 = equipes[j]
                score1, score2 = simuler_match(e1, e2)
                matchs.append({
                    "equipe1": e1["nom"],
                    "equipe2": e2["nom"],
                    "score": (score1, score2)
                })

        resultats_groupes[nom_groupe] = matchs

    return groupes, resultats_groupes


def selectionner_qualifies(groupes, resultats_groupes):
    qualifies = []
    groupes_qualifies = {}  # Stocke premier/deuxième par groupe

    for groupe_nom, equipes in groupes.items():
        if groupe_nom not in resultats_groupes:
            print(f"⚠ Groupe {groupe_nom} vide ou introuvable")
            continue

        matchs_groupe = resultats_groupes[groupe_nom]
        classement = calcul_classement_groupe(matchs_groupe, equipes)

        if len(classement) >= 2:
            premier = classement[0]["nom"]
            deuxieme = classement[1]["nom"]
            qualifies.extend([premier, deuxieme])
            groupes_qualifies[groupe_nom] = [premier, deuxieme]

    return qualifies, groupes_qualifies

def meme_groupe(equipe1_nom, equipe2_nom, groupes):
    """Vérifie si deux équipes sont dans le même groupe"""
    for groupe in groupes.values():
        if equipe1_nom in groupe and equipe2_nom in groupe:
            return True
    return False


def tirage_huitiemes(groupes_qualifies, resultats_groupes):
    premiers = []
    deuxiemes = []

    for groupe, equipes in groupes_qualifies.items():
        if groupe in resultats_groupes and len(equipes) >= 2:
            premier, deuxieme = equipes[0], equipes[1]
            premiers.append(premier)
            deuxiemes.append(deuxieme)

    random.shuffle(deuxiemes)
    confrontations = []

    for premier in premiers:
        for i, deuxieme in enumerate(deuxiemes):
            if not meme_groupe(premier, deuxieme, groupes_qualifies):
                confrontations.append((premier, deuxieme))
                deuxiemes.pop(i)
                break

    return confrontations
