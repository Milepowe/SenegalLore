
init python:
    from math import sqrt

# Déclarez les personnages utilisés dans le jeu.
define chad = Character('???', color="#d4d4d4")
define mc = Character("[playername]",color="#0084ff")

label start:
    play music "character_creation.mp3" fadein 2.0

    camera:
        perspective True

    show lock_avatar at center with fade:
        zpos -200
        warp sqrt 3.5 zpos 0

    chad "Salut. Tu es en ce moment dans un dimension qui va te\npermettre de rejondre l'autre monde."
    chad "Et pour le rejoindre, tu vas devoir me donner\nquelques informations sur ta personne."
    
    chad "Quel est ton nom ?"

    # input qui donne le nom du joueur 
    python :
        while True :
            playername = renpy.input("Ton nom (sans espaces, 10 charactères max):")
            
            if playername != "" and playername not in " " and len(playername) < 10:
                break

    show lock_avatar :
        warp sqrt 0.5 xpos 350

    chad "Tu viens de rentrer ton nom, merci beaucoup."
    chad "Maintenant, je vais utiliser ma PUISSANCE pour\nte tp dans l'autre monde."

    menu :
        chad "T'es prêt du coup ?"

        "Oui." :
            chad "D'accord. Prépare toi."
        
        "Non" :
            chad "You ARE going to BRAZILLLL !!!"
# a reecrire un jour car en dessous de nos standards ( Note de Ramker : Tkt je gére )

    return
