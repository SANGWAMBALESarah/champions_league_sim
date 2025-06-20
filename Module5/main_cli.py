# main_cli.py
import random
from team_manager import creer_equipes
from tournament_logic import tirer_groupes, simuler_matches_groupes, selectionner_qualifies, tirage_huitiemes
from stats_generator import calculer_stats_par_equipe, generer_classement, afficher_classement, afficher_stats_completes, sauvegarder_stats
from match_simulator import simuler_match_elimination


def afficher_groupes(groupes):
    print("\n⚽ RÉPARTITION DES GROUPES")
    for groupe, equipes in groupes.items():
        print(f"\nGroupe {groupe}:")
        for equipe in equipes:
            print(f" - {equipe['nom']} (Force: {equipe['force']})")


def afficher_confrontations(confs, titre):
    print(f"\n🔥 {titre}")
    for i, (e1, e2) in enumerate(confs, start=1):
        print(f"{i}. {e1} vs {e2}")


def simuler_phase_elimination(equipes_elim, phase, toutes_les_equipes):
    print(f"\n🔥 PHASE : {phase}")
    qualifies = []

    if not equipes_elim:
        print("❌ Aucune confrontation trouvée — phase annulée")
        return []

    for i, (e1, e2) in enumerate(equipes_elim):
        print(f"\nMatch {i+1} : {e1} vs {e2}")

        equipe1 = next((eq for eq in toutes_les_equipes if eq["nom"] == e1), None)
        equipe2 = next((eq for eq in toutes_les_equipes if eq["nom"] == e2), None)

        if not equipe1 or not equipe2:
            print("⚠ Une équipe manque !")
            continue

        vainqueur = simuler_match_elimination(equipe1, equipe2)
        print(f"✅ Qualifié : {vainqueur['nom']}")

        qualifies.append(vainqueur["nom"])

    # Retourner des paires pour la prochaine phase
    paired_qualifies = []
    for i in range(0, len(qualifies), 2):
        if i + 1 < len(qualifies):
            paired_qualifies.append((qualifies[i], qualifies[i + 1]))
        else:
            print(f"⚠ Équipe {qualifies[i]} passe automatiquement (pas d’adversaire)")
            paired_qualifies.append((qualifies[i],))  # Ajouter quand même en tuple

    return paired_qualifies


if _name_ == "_main_":
    print("🏆 BIENVENUE DANS LA SIMULATION DE LA LIGUE DES CHAMPIONS !\n")

    # Étape 1 : Charger ou créer les équipes
    toutes_les_equipes = creer_equipes()
    print("✅ Équipes créées avec succès.")

    # Étape 2 : Tirage au sort des groupes
    groupes = tirer_groupes(toutes_les_equipes)
    afficher_groupes(groupes)

    # Étape 3 : Simuler les matchs de groupes
    print("\n🎮 SIMULATION DES MATCHS DE GROUPES")
    groupes_seulement, matchs_groupe = simuler_matches_groupes(groupes)

    # Extraire tous les matchs dans une liste plate
    matchs_plats = []
    for groupe in matchs_groupe.values():
        matchs_plats.extend(groupe)

    print(f"✅ {len(matchs_plats)} match(s) de groupe simulés")

    # Nettoyage : garder uniquement les matchs valides
    matchs_plats = [
        m for m in matchs_plats
        if isinstance(m, dict) and "equipe1" in m and "equipe2" in m
    ]

    print(f"✅ {len(matchs_plats)} match(s) valide(s) après nettoyage")

    # Créer un dictionnaire de matchs par groupe
    resultats_groupes = {}
    for groupe_nom in groupes_seulement.keys():
        resultats_groupes[groupe_nom] = []

    for match in matchs_plats:
        for groupe_nom, equipes in groupes_seulement.items():
            noms_equipes = [e["nom"] for e in equipes]
            if match["equipe1"] in noms_equipes and match["equipe2"] in noms_equipes:
                resultats_groupes[groupe_nom].append(match)
                break

    print("✅ Matchs organisés par groupe")

    # Étape 4 : Sélection des équipes qualifiées
    print("\n🎯 SELECTION DES EQUIPES QUALIFIEES")
    qualifies, groupes_qualifies = selectionner_qualifies(groupes_seulement, resultats_groupes)
    print("Équipes qualifiées aux huitièmes de finale :")
    for nom in qualifies:
        print(" -", nom)

    # Étape 5 : Tirage des huitièmes de finale
    print("\n🎱 TIRAGE DES HUITIÈMES DE FINALE")
    huitiemes = tirage_huitiemes(groupes_qualifies, resultats_groupes)

    if not huitiemes:
        print("❌ Impossible de faire le tirage — aucune équipe trouvée.")
    else:
        afficher_confrontations(huitiemes, "HUITIÈMES DE FINALE")

    # Étape 6 : Simuler phases éliminatoires
    if huitiemes:
        print("\n🔥 SIMULATION DES PHASES ÉLIMINATOIRES")
        qualifies_quarts = simuler_phase_elimination(huitiemes, "Quarts de finale", toutes_les_equipes)
        qualifies_demis = simuler_phase_elimination(qualifies_quarts, "Demi-finales", toutes_les_equipes)
        finale = simuler_phase_elimination(qualifies_demis, "Finale", toutes_les_equipes)

        champion = finale[0][0] if finale else "Inconnu"
        print(f"\n🎉 LE GRAND CHAMPION EST : {champion} ! 🏆⚽")
    else:
        print("\n🚫 Aucun tirage possible → simulation annulée.")

    # Étape 7 : Affichage des statistiques finales
    print("\n📊 CALCUL DES STATISTIQUES FINALES")
    try:
        stats_completes = calculer_stats_par_equipe(groupes_seulement, resultats_groupes)

        # Générer et afficher le classement global
        classement_final = generer_classement(stats_completes, groupes_seulement)
        afficher_classement(classement_final)

        # Afficher les détails des stats
        afficher_stats_completes(stats_completes)

        # Sauvegarder les stats
        sauvegarder_stats(stats_completes)

    except Exception as e:
        print(f"\n⚠ Échec de génération des stats : {e}")

    print("\n🔚 FIN DE LA SIMULATION")