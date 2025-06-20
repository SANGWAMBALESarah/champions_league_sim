Module 2 : match_simulator.py
# Rôle : Simuler les matchs entre équipes avec gestion des scores, prolongations et tirs au but

🔧 Fonctions principales dans ce module :
1. simuler_match(equipe1, equipe2)
Simule un match de groupe ou d’élimination simple : Prend en entrée deux équipes (dictionnaires)
Calcule un score basé sur la force de chaque équipe
Affiche un commentaire à l’écran + en voix haute
Sauvegarde le résultat du match dans matchs.json
Retourne (score1, score2)
➡️ C’est la fonction cœur de la simulation.

2. simuler_tirs_au_but(equipe1, equipe2)
Gère les séances de tirs au but en cas de match nul

Simule 5 tirs par équipe
En cas d’égalité → rounds supplémentaires jusqu’à décision
Retourne l’équipe gagnante
3. simuler_match_elimination(equipe1, equipe2)
Spécifique aux phases éliminatoires

# Appelle simuler_match() pour avoir les scores
Si match nul → appelle simuler_tirs_au_but()
Sauvegarde aussi dans JSON
Retourne l’équipe vainqueur
💡 Fonctions annexes utiles
4. lire_commentaire(commentaire)
Utilise pyttsx3 pour lire à haute voix les résultats
→ Donne un côté interactif et original à ton projet

5. effet_tir(equipe) + generer_commentaire(...)
Donne un effet visuel quand une équipe tire
→ Rend le programme plus vivant et engageant

🎯 Objectif :
# Ce module permet de simuler un match entre deux équipes , avec : 

Des scores réalistes (basés sur la force)
Des commentaires vocaux (via pyttsx3)
Des effets visuels pendant les tirs au but
Et une sauvegarde complète dans un fichier matchs.json
🔧 Fonctionnement technique :
La force de l’équipe influence le nombre maximum de buts possibles (score_max = force // 20)
On génère des scores aléatoires mais cohérents
On affiche un message visuel et on lit à haute voix
On sauvegarde le match dans matchs.json pour les stats
En phase éliminatoire, si match nul → on passe aux tirs au but
📁 Exemple de données sauvegardées dans matchs.json
{
  "matchs": [
    {
      "type": "groupe",
      "equipe1": "Équipe 1",
      "equipe2": "Équipe 9",
      "score1": 2,
      "score2": 1,
      "vainqueur": "Équipe 1"
    },
    {
      "type": "elimination",
      "equipe1": "Équipe 3",
      "equipe2": "Équipe 7",
      "score1": 1,
      "score2": 1,
      "vainqueur": "Équipe 3"
    }
  ]
}

# LES POINTS FORTS 
Avantages                               Explication
✔️ Gestion des forces                   Score réaliste basé sur la puissance de chaque équipe
✔️ Commentaires vocaux                  Le programme peut parler tout seul (originalité !)
✔️ Effets visuels	                    Affichage progressif des tirs au but (améliore l'expérience utilisateur)
✔️ Persistance des données	            Tous les matchs sont sauvegardés dans matchs.json

# DIFFICULTES
# Défi                                    Solution apportée
Synchroniser les voix et les affichages Utilisation de engine.runAndWait()
Équilibrer les tirs au but              Probabilité de réussite à 70% pour éviter trop de tricherie
Gérer les matchs nuls                   Ajout de rounds supplémentaires jusqu’à décision claire
 