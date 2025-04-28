# Mini-jeux Python

## Structure du projet

python-mini-jeux/
│
├── main.py            # Point d'entrée du programme : menu principal, lancement de partie
├── game_manager.py    # Gère l'enchaînement des mini-jeux, logique de victoire/défaite
│
├── games/             # Dossier contenant les mini-jeux
│   ├── __init__.py
│   ├── game1.py       # Premier mini-jeu
│   ├── game2.py       # Deuxième mini-jeu
│   ├── game3.py       # Troisième mini-jeu
│   ├── game4.py       # Quatrième mini-jeu
│   └── game5.py       # Cinquième mini-jeu
│
├── utils/             # Fonctions utilitaires
│   ├── __init__.py
│   └── input_handler.py   # Par exemple, sécuriser les entrées utilisateur
│
├── requirements.txt   # Dépendances éventuelles
└── README.md          # Explications du projet
