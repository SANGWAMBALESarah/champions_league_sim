 Ce fichier Python tournament_logic.py contient la logique principale d’un tournoi de football de type Ligue des Champions, depuis le tirage des groupes jusqu’au tirage des huitièmes de finale. Voici une explication claire et sectionnée de chaque fonction :


---

🔁 1. tirer_groupes(equipes)

But : répartir 32 équipes en 8 groupes (A à H), 4 équipes par groupe.
Processus :

Mélange aléatoire de la liste d’équipes.

Répartition cyclique des équipes dans les groupes A → H.


✅ Retourne un dictionnaire groupes = { "A": [...], ..., "H": [...] }


---

📊 2. calcul_classement_groupe(matchs, groupe_equipes)

But : calculer le classement d’un groupe selon :

les points (3 victoire, 1 nul, 0 défaite)

la différence de buts

les buts marqués


Entrée :

matchs : liste de matchs (avec scores)

groupe_equipes : liste d'équipes du groupe


✅ Retourne une liste triée des équipes du groupe (du 1er au dernier).


---

⚽ 3. simuler_matches_groupes(groupes)

But : simuler tous les matchs de groupe entre les équipes (6 matchs par groupe).
Fonction utilisée : simuler_match importée de match_simulator.py.

✅ Retourne :

groupes (inchangé)

resultats_groupes = dictionnaire des résultats des matchs de chaque groupe



---

🎟 4. selectionner_qualifies(groupes, resultats_groupes)

But : déterminer les 2 équipes qualifiées par groupe (1er et 2e).
Utilise la fonction calcul_classement_groupe.

✅ Retourne :

qualifies = liste de 16 équipes qualifiées (2 par groupe)

groupes_qualifies = dictionnaire {"A": [1er, 2e], ...}



---

❓ 5. meme_groupe(equipe1_nom, equipe2_nom, groupes)

But : vérifier si deux équipes sont dans le même groupe.
Utilisée pour éviter les confrontations entre équipes du même groupe en huitièmes.


---

🧮 6. tirage_huitiemes(groupes_qualifies, resultats_groupes)

But : tirer les confrontations des huitièmes de finale :

1er contre 2e

Pas du même groupe

Tirage aléatoire des deuxièmes


✅ Retourne une liste de matchs huitièmes sous forme de tuples :
[("Real Madrid", "AC Milan"), ...]


---

✅ Résumé visuel

1. tirer_groupes       ➜ groupes A à H
2. simuler_matches     ➜ scores des matchs
3. calcul_classement   ➜ ordonner les équipes
4. selectionner_qualifies ➜ top 2 par groupe
5. tirage_huitiemes    ➜ confrontations 1/8
6.
