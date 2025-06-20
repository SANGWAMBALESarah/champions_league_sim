📄 Projet : Simulation de la Ligue des Champions
Module 5 : Interface en ligne de commande (main_cli.py)
🔧 Objectif :
Ce module coordonne tous les autres modules du projet. Il permet de :

Lancer la simulation
Afficher les résultats étape par étape
Coordonner la logique du tournoi (tirage, matchs, qualifications)
Afficher le vainqueur final
Générer des statistiques détaillées

Ce module utilise toutes les fonctions des autres modules pour créer un tournoi complet. 

🎯 Fonctionnalités principales
1. afficher_groupes(groupes) – Affiche les groupes A à H
python

👉 Cette fonction affiche proprement la composition de chaque groupe avec les équipes et leur niveau de force.

2. afficher_confrontations(confs, titre) – Affichage des phases éliminatoires
python

👉 Permet d'afficher les confrontations (huitièmes, quarts, demis, finale) sous forme lisible.

3. simuler_phase_elimination(...) – Simule une phase à élimination directe
python

👉 Prend les équipes qualifiées et simule les matchs suivants :

Quarts de finale
Demi-finales
Finale
Utilise simuler_match_elimination() pour chaque duel.

    # Étape 1 : Charger ou créer les équipes
✅ Étape 1 : Création des équipes
Appelle creer_equipes() depuis team_manager.py
→ Génère 32 équipes avec "nom" et "force" aléatoire entre 50 et 100

✅ Étape 2 : Tirage au sort des groupes
python

Appelle tirer_groupes() → mélange les équipes et les divise en 8 groupes (A à H)
Puis affiche chaque groupe avec ses équipes
✅ Étape 3 : Simuler les matchs de groupe
python

Joue tous les matchs aller dans chaque groupe
Organise les résultats dans une liste plate pour faciliter le calcul des stats

Supprime les données invalides
Garantit que seuls les vrais matchs sont utilisés pour les statistiques
✅ Répartition des matchs par groupe
python

Associe chaque match à son groupe pour pouvoir faire les classements
Nécessaire pour calculer les points et les stats par groupe
✅ Étape 4 : Sélection des équipes qualifiées
python

Appelle selectionner_qualifies() → récupère les 2 premiers de chaque groupe
Stocke aussi les premiers/deuxièmes pour le tirage des huitièmes
✅ Étape 5 : Tirage des huitièmes de finale
python

Appelle tirage_huitiemes() → évite les matchs intra-groupe
Affiche les paires d’équipes pour les huitièmes
✅ Étape 6 : Phases éliminatoires jusqu’à la finale
python

Lance les phases éliminatoires :
Huitièmes → Quarts → Demi-finale → Finale
En cas d’égalité → tirs au but via simuler_tirs_au_but()
À la fin, affiche le vainqueur du tournoi
✅ Étape 7 : Statistiques finales
python

Génère un classement global
Affiche :
Meilleure attaque
Meilleure défense
Sauvegarde tout dans stats_tournoi.json
