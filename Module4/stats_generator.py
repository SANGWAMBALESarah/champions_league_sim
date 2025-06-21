# stats_generator.py
import json
from collections import defaultdict


def calculer_stats_par_equipe(groupes, resultats_groupes):
    stats = {}

    for groupe_nom, equipes in groupes.items():
        if groupe_nom not in resultats_groupes:
            continue

        matchs_groupe = resultats_groupes[groupe_nom]

        for equipe in equipes:
            nom = equipe["nom"]
            if nom not in stats:
                stats[nom] = {
                    "buts_marques": 0,
                    "buts_encaisses": 0,
                    "points": 0,
                    "diff_buts": 0,
                    "matches_joues": 0
                }

        for match in matchs_groupe:
            e1 = match["equipe1"]
            e2 = match["equipe2"]
            score1, score2 = match["score"]

            # Mise à jour des buts marqués/encaissés
            stats[e1]["buts_marques"] += score1
            stats[e1]["buts_encaisses"] += score2
            stats[e1]["diff_buts"] = stats[e1]["buts_marques"] - stats[e1]["buts_encaisses"]

            stats[e2]["buts_marques"] += score2
            stats[e2]["buts_encaisses"] += score1
            stats[e2]["diff_buts"] = stats[e2]["buts_marques"] - stats[e2]["buts_encaisses"]

            # Points
            if score1 > score2:
                stats[e1]["points"] += 3
            elif score2 > score1:
                stats[e2]["points"] += 3
            else:
                stats[e1]["points"] += 1
                stats[e2]["points"] += 1

            # Matches joués
            stats[e1]["matches_joues"] += 1
            stats[e2]["matches_joues"] += 1

    return stats


def generer_classement(stats, groupes):
    #Génère un classement basé sur les stats réelles"""
    classement = []

    for groupe in groupes.values():
        for equipe in groupe:
            nom = equipe["nom"]
            if nom in stats:
                data = stats[nom]
                classement.append((nom, data["points"], data["diff_buts"], data["buts_marques"]))

    # Tri par points, diff buts, buts marqués
    classement.sort(key=lambda x: (-x[1], -x[2], -x[3]))
    return classement


def trouver_meilleure_attaque(stats):
    #Retourne l'équipe avec le plus de buts marqués
    return max(stats.items(), key=lambda x: x[1]["buts_marques"])


def trouver_meilleure_defense(stats):
    #Retourne l'équipe avec le moins de buts encaissés
    return min(stats.items(), key=lambda x: x[1]["buts_encaisses"])


def afficher_classement(classement):
    print("\n🏆 Classement général des équipes")
    print("{:<5} {:<15} {:<7} {:<8} {:<10}".format("Rang", "Équipe", "Points", "Diff", "Buts"))
    for i, (equipe, points, diff, buts) in enumerate(classement, start=1):
        print("{:<5} {:<15} {:<7} {:<8} {:<10}".format(i, equipe, points, diff, buts))


def afficher_stats_completes(stats):
    print("\n📊 Statistiques détaillées par équipe")
    print("{:<15} {:<7} {:<7} {:<7} {:<10}".format("Équipe", "Points", "Matches", "Buts", "Encaissés"))

    for equipe, data in stats.items():
        print("{:<15} {:<7} {:<7} {:<7} {:<10}".format(
            equipe,
            data["points"],
            data["matches_joues"],
            data["buts_marques"],
            data["buts_encaisses"]
        ))

    meilleure_attaque = trouver_meilleure_attaque(stats)
    meilleure_defense = trouver_meilleure_defense(stats)

    print(f"\n🔥 Meilleure attaque : {meilleure_attaque[0]} ({meilleure_attaque[1]['buts_marques']} buts)")
    print(f"🔒 Meilleure défense : {meilleure_defense[0]} ({meilleure_defense[1]['buts_encaisses']} buts encaissés)")


def sauvegarder_stats(stats, filename="stats_tournoi.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4, ensure_ascii=False)
