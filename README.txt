Bonjour, Dans le cadre de la sae 1.02 et 1.01 voici notre jeu "Jeu de Boules" vous avez seulement besoin du module upemtk, le fichier parametre.txt dans le meme dossier. Il se peut qu'il y ait des latences lors  du chargement de la partie, il suffit d'attendre quelques secondes. 
    

— les variantes qui ont été implémentées :
    - Terminaison (Léo)
    - Taille des Boules (Ahmed, Léo)
    - Version dynamique (Ahmed)
    - Obstacles (Léo)
    - Scores (Léo, Ahmed) (évolution du code)
    - Sablier (Ahmed)
 
- Bonus implémentés dans le jeu :
    - Pause et Sauvegarde (Ahmed)
    - Sauvegarde des paramètres (Léo)


— l’organisation du programme :
    notre programme est organisé de cette manière:
      import
      fonctions
        docstring
        variables
        conditions
      main
        variables
        boucle
        conditions
      
   
      
— les choix techniques :
    jeu codé en python 3
    avec le module upemtk
    choix de faire les fontionnalités longue dans des fonctions, l'autre partie dans le main pour les fonctions courtes.
    mise en commun du code avec github.
    IDE : Spyder, Visual Studio Code
    
    
    
— les éventuels problèmes rencontrés:
    création sablier problème avec time.sleep() de 10 seconde par exemple il n'était pas possible de cliquer pour ajouter un cercle car le script s'éxecute dans           l'ordre sans le module tkinter
    Dans une de nos idée de base était de changer la taille de la fenêtre en fonction de l'écran de l'utilisateur malheursement il était impossible d'utiliser tkinter     pour utiliser les méthode pour récuperer les dimensions de l'écran. Nous avions une alternative mais qui ne marchait pas sur  Linux nous avons donc pris la         décision de ne pas récuperer les dimensions de l'écran. Malgré tout notre jeu s'adapte à n'importe quelle dimension de la fenetre il est seulement nécessaire de les mettres dans le fichier parametre. 

Pour jouer :
 Executez le code avec le module upemtk dans le meme dossier et jouez, vous pouvez sauvegarder la partie en cours grace au bouton "pause" pause puis "sauvegarder" et pour reprendre la partie relancer le jeu puis choisir "Charger la sauvegarde". Le bouton "Nouvelle partie" sert a créer une nouvelle partie
 
