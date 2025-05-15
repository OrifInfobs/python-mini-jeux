import os

Clear = lambda: os.system("cls") # Clear console function

def introduction(): # Main game function and boot to game manager
    Clear()
    print("""
============================================================
            🎉 BIENVENUE DANS LE MINI JEUX WORDLE 🎉
============================================================

Devinez un mot secret de 5 lettres parmi une liste en 6 essais.
Ces mots sont choisis aléatoirement et sont toujours des mots
du dictionnaire valides.

Voici les symboles que vous verrez dans les résultats de vos essais:

    ✔ = Lettre correcte et bien placée
    ❌ = Lettre incorrecte (non présente dans le mot)
    ➕ = Lettre correcte mais mal placée
    ➖ = Lettre correcte mais toutes les occurrences ont déjà été comptées

    Bonne chance! 
============================================================
""")