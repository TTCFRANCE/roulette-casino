# Jeu de Roulette (Python - Console)

## Description
Ce projet est un mini jeu de roulette en console.  
Le joueur commence avec un capital et doit tenter d'atteindre un objectif en misant sur des numéros.

## Objectif
J'ai réalisé ce projet pour m'entraîner à :
- créer des boucles et conditions complexes
- gérer les entrées utilisateur et vérifier leur validité
- utiliser des nombres aléatoires
- simuler un mini-jeu avec un capital et des gains/pertes

## Fonctionnalités
- Capital initial de 200€
- Objectif : atteindre 1000€
- Système de mise avec vérification du capital
- Choix d’un numéro entre 0 et 20
- Résultat aléatoire de la roulette
- Mise à jour du capital après chaque tour
- Gestion des erreurs (mise trop élevée, nombre hors limites)

## Fonctionnement
1. Le joueur saisit une mise
2. Le joueur choisit un numéro
3. La roulette se lance (nombre aléatoire entre 0 et 20)
4. Si le numéro est correct : le joueur gagne sa mise  
   Sinon : il perd sa mise
5. Le jeu continue jusqu’à ce que le joueur atteigne 1000€ ou perde tout

## Technologies utilisées
- Python
- Module `random`
- Module `time` pour pause dramatique

## Lancer le projet
1. Installer Python
2. Exécuter le fichier :
```bash
python roulette_console.py
