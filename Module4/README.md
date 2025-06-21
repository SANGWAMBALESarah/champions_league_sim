🔢 calculer_stats_par_equipe(groupes, resultats_groupes)

Cette fonction :
	•	Parcourt chaque groupe du tournoi.
	•	Pour chaque équipe, elle initialise ses statistiques si ce n’est pas encore fait.
	•	Ensuite, elle parcourt tous les matchs du groupe et :
	•	ajoute les buts marqués et encaissés à chaque équipe,
	•	calcule la différence de buts (buts marqués - buts encaissés),
	•	attribue les points (3 pour une victoire, 1 pour un match nul),
	•	compte le nombre de matchs joués.
	•	À la fin, elle retourne un dictionnaire contenant les stats de toutes les équipes.

⸻

🥇 generer_classement(stats, groupes)

Cette fonction :
	•	Crée une liste de tuples contenant les infos principales de chaque équipe (nom, points, diff. buts, buts marqués).
	•	Trie cette liste selon les règles classiques d’un classement :
	1.	Par nombre de points (du plus grand au plus petit),
	2.	Puis par différence de buts,
	3.	Puis par buts marqués.

Elle retourne cette liste triée, qui représente le classement général.

⸻

🎯 trouver_meilleure_attaque(stats)

Cette fonction :
	•	Cherche l’équipe ayant marqué le plus grand nombre de buts.
	•	Elle retourne le nom de l’équipe et son nombre de buts marqués.

⸻

🛡 trouver_meilleure_defense(stats)

Cette fonction :
	•	Cherche l’équipe ayant encaissé le moins de buts.
	•	Elle retourne le nom de l’équipe et son nombre de buts encaissés.

⸻

📋 afficher_classement(classement)

Cette fonction :
	•	Affiche le classement général des équipes de façon lisible dans la console.
	•	Elle montre le rang, le nom de l’équipe, ses points, sa différence de buts, et ses buts marqués.

⸻

📊 afficher_stats_completes(stats)

Cette fonction :
	•	Affiche les statistiques détaillées de chaque équipe : points, matchs joués, buts marqués, buts encaissés.
	•	Ensuite, elle affiche la meilleure attaque et la meilleure défense.

⸻

💾 sauvegarder_stats(stats, filename="stats_tournoi.json")

Cette fonction :
	•	Sauvegarde toutes les statistiques calculées dans un fichier JSON.
	•	Cela permet de garder les résultats même après la fermeture du programme.
