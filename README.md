# 🏆
 champions_league_sim
Simulation de la ligue des champions en Python

# 👪 Membres du projet

| Nom complet               |              Role / Module
|---------------------------|---------------------------------------------
|SANGARA BACIDOSE FRANCOIS  |Module1: Gestion des équipes ("team_manager.py)
|SANGWA MBALE SARAH         |Module2: Simulation de matchs("match_simulator.py)
|SALIMA NDAY DIMERCIA       |Module3: Gestion des groupes et qualifications ("tournament_logic.py)
|SANGWA MUYUMBA RYAN B5     |Module4: Statistiques et classement ("stats_generator.py")
|SANDE KUYELA SAMMY B4      |Module5:Interface principale / orchestration ("main_cli.py)

## DESCRIPTION DU PROJET 
Cette application simule un tournoi de football avec :

- 32 équipes générées automatiquement avec un niveau de force aléatoire.
- Un tirage au sort pour les 8 groupes (A à H).
- Simulation des matchs de groupe et des matchs à élimination directe.
- Affichage du classement, des résultats et des statistiques détaillées.
- Sauvegarde des données en JSON.

## STRUCTURE DU PROJET

champions_league_sim/
|____main_cli.py         #Lancement principal du tournoi
|____team_manager.py     #Création et gestion des équipes
|____tournament_logic.py #Groupes, tirages et qualifications
|____match_simulator.py  #Simulation de matchs et tirs au but
|____tats_generator.py  #Statistiques, classement,sauvegarde
|____equipes.json        #Fichier JSON des équipes
|____stats_tournoi.json  # Statistique sauvegardées

---

## ⚙ Installation

1. *Cloner le projet*
bash
git clone https://github.com/votre-utilisateur/champions_league_sim.git
cd champions_league_sim

3.	Installer Python (si ce n’est pas fait)
Assurez-vous que vous utilisez Python 3.8 ou plus : python --version
```
🚀 Lancement de la simulation

Dans le terminal, lancez simplement : python main_cli.py

Vous verrez apparaître toutes les étapes :
	•	Création des équipes
	•	Tirage des groupes
	•	Simulation des matchs
	•	Phase éliminatoire
	•	Affichage des classements et statistiques

🧪 Exemple d’exécution
```
🏆 BIENVENUE DANS LA SIMULATION DE LA LIGUE DES CHAMPIONS !

✅ Équipes créées avec succès.

⚽ RÉPARTITION DES GROUPES
Groupe A:
 - Équipe 1 (Force: 87)
 - Équipe 2 (Force: 73)
...

🎮 SIMULATION DES MATCHS DE GROUPES
...

🎯 SELECTION DES EQUIPES QUALIFIEES
 - Équipe 1
 - Équipe 5
...

🔥 PHASE : Quarts de finale
Match 1 : Équipe 1 vs Équipe 5
✅ Qualifié : Équipe 1
...

🎉 LE GRAND CHAMPION EST : Équipe 1 ! 🏆⚽

📊 Résultats générés
	•	equipes.json : Contient les 32 équipes et leur force.
	•	stats_tournoi.json : Contient toutes les statistiques finales (buts, points, matchs joués…).

🛠 Technologies utilisées
	•	Python 3.x
	•	JSON (fichiers de données)
	•	Module random
	•	Ligne de commande (CLI)

📌 Remarques
	•	Tous les tirages et résultats sont aléatoires à chaque exécution.
	•	Le code peut être facilement adapté pour utiliser de vrais noms d’équipes ou une interface graphique plus tard.

# 📧 Contact

Pour toute question, contactez l’un des membres du projet ou ouvrez une issue sur GitHub.



