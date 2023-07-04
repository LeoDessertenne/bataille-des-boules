 # -----------------import-----------------
from upemtk import *
import time
from math import sqrt
import random
import os
#-----------------Fonctions--------------

        
# Liste qui contient toutes les couleurs qui peuvent etre jouable
lst_col = ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',
         'beige', 'bisque', 'blanchedalmond', 'blue',
         'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse',
         'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson',
         'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray',
         'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta',
         'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 
         'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray',
         'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink',
         'deepskyblue', 'dimgray', 'dodgerblue', 'firebrick',
         'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 
         'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 
         'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 
         'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 
         'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen',
         'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue',
         'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen',
         'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue',
         'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue',
         'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue',
         'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace',
         'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 
         'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff',
         'peru', 'pink', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 
         'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna',
         'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow',
         'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 
         'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']


def Accueil(LongueurFenetre, LargeurFenetre) :
    
    """
    Permet de créer l'écran d'accueil du jeu avec les choix de couleur
    """
    
#Coordonées des polygones qui permetent le changement de couleurs des boules
    poly_620 = 0.3875 * LargeurFenetre
    poly_480 = 0.48 * LongueurFenetre
    poly_520 = 0.52 * LongueurFenetre
    poly_645 = 0.403 * LargeurFenetre
    poly_500 = 0.5 * LongueurFenetre
    poly_180 = 0.1125 * LargeurFenetre
    poly_155 = 0.097 * LargeurFenetre
    poly_1320 = 0.825 * LargeurFenetre
    poly_1345 = 0.84 * LargeurFenetre
    poly_880 = 0.55 * LargeurFenetre
    poly_855 = 0.534 * LargeurFenetre
    
# indice i qui permet de changer la couleur de la boule du joueur 1
    i = 8
# indice j qui permet de changer la couleur de la boule du joueur 1
    j = 115
# Rectangle de fond de l'écran d'accueil
    rectangle( 0, 0, LargeurFenetre, LongueurFenetre, remplissage='dimgrey')
    
# Permet de placer des petits triangles en fond pour la décoration:
        
# Liste qui contient les petits triangles de fond
    lst_com_pol = []
    # Couleur joueur 1
    for k in range (0, int(LargeurFenetre/2) - int(0.01875*LargeurFenetre), 30) :
        for l in range(0, int(LongueurFenetre), 30) :
            pol = polygone([(k, l), (k+30, l), (k+15, l+30)], remplissage=lst_col[i])
            lst_com_pol.append(pol)
            
    # Couleur joueur 1
    for k in range (int(LargeurFenetre/2) - int(0.01875*LargeurFenetre), int(LargeurFenetre), 30) :
        for l in range(0, int(LongueurFenetre), 30) :
            pol = polygone( [(k, l), (k+30, l), (k+15, l+30)], remplissage=lst_col[j])
            lst_com_pol.append(pol)
            
# Rectangle centré qui contient la selectio des couleurs de boules
    rec1 = rectangle( 1/10.5 * LargeurFenetre, 1/13.5 * LongueurFenetre
    , 5.05/6 * LargeurFenetre, 10/13.5 * LongueurFenetre
    , remplissage='goldenrod')
    
# Polygone qui permettent de changer de couleurs à l'écran d'accueil 
    pol1 = polygone( [(poly_620,poly_480), (poly_620,poly_520), (poly_645,poly_500)], remplissage='White')
    pol2 = polygone( [(poly_180,poly_480), (poly_180,poly_520), (poly_155,poly_500)], remplissage='White')
    pol3 = polygone( [(poly_1320,poly_480), (poly_1320,poly_520), (poly_1345,poly_500)], remplissage='White')
    pol4 = polygone( [(poly_880,poly_480), (poly_880,poly_520), (poly_855,poly_500)], remplissage='White')
    
# Intitulé de notre jeu qui s'aafiche à l'écran d'accueil
    tex1 = texte( LargeurFenetre / 2.52 , 0.150 * LongueurFenetre
    , "Bataille d", taille = int(0.03125 * LargeurFenetre)
    , ancrage = "center", couleur = lst_col[i])
    
    tex2 = texte( LargeurFenetre / 1.77, 0.150 * LongueurFenetre
    , "e Boules", taille = int(0.03125 * LargeurFenetre)
    , ancrage = "center", couleur = lst_col[j])
    
# Cercle qui indique la couleur selectioné par le joueur :
    cer1 = cercle( 0.25 * LargeurFenetre, 0.5 * LongueurFenetre, 0.125 * LargeurFenetre, remplissage = str(lst_col[i]))
    cer2 = cercle( 0.6875 * LargeurFenetre, 0.5 * LongueurFenetre, 0.125 * LargeurFenetre, remplissage = str(lst_col[j]))
    
# Cercle du bouton suivant de l'écran d'accueil ainsi que le texte
    cer3 = cercle( 0.468175 * LargeurFenetre, 0.35 * LongueurFenetre, 0.06125 * LargeurFenetre, remplissage = 'dimgrey')
    cer4 = cercle( 0.468175 * LargeurFenetre, 0.35 * LongueurFenetre, 0.05125 * LargeurFenetre, remplissage = 'goldenrod')
    tex3 = texte( 0.468175 * LargeurFenetre, 0.355 * LongueurFenetre, 'Continuer', ancrage = "center", taille = int(0.015625 * LargeurFenetre))

# Permet aux joueurs de selectionné la couleurs qu'ils souhaitent tant que le bouton "suivant" n'est pas cliqué
    while True :
        x1, y1, type_clique = attente_clic()
        
        if len(lst_com_pol) > 0 :
            for m in lst_com_pol :
                efface(m)
                
        lst_com_pol = []
        
        efface(rec1)
        rec1 = rectangle( 1/10.5 * LargeurFenetre, 1/13.5 * LongueurFenetre
        , 5.05/6 * LargeurFenetre, 10/13.5 * LongueurFenetre, remplissage = 'goldenrod')

# Verifie si un bouton est cliqué
        if inter_rect(0, x1, y1, poly_620, poly_480, poly_645, poly_520) :
            if i == len(lst_col) - 1 :
                i = 0
            else :
                i += 1
  
        elif inter_rect(0 ,x1 ,y1 ,poly_155 ,poly_480 ,poly_180 ,poly_520) :
            if i == 0 :
                 i = len(lst_col) - 1
            else :
                i -= 1
        
        if inter_rect(0, x1, y1, poly_1320, poly_480, poly_1345, poly_520):
            if j == len(lst_col) - 1 :
                j = 0
            else :
                j += 1

        elif inter_rect(0, x1, y1, poly_855, poly_480, poly_880, poly_520) :
            if j == 0 :
                j = len(lst_col) - 1
            else :
                j -= 1
                
        if inter_in(0, x1, y1,[[0.468175 * LargeurFenetre, 0.35 * LongueurFenetre, 0.05125 * LargeurFenetre]]) :
            efface_tout()
            return lst_col[i], lst_col[j]
          
# Permet d'éviter que les deux joueurs puissent choisir la meme couleur          
        if i == j :
            if i == 0 :
                j = len(lst_col) - 1
                
            elif i == len(lst_col) - 1 :
                j = len(lst_col) - 2
                
            else :
                i += 1
                
# Pour changer la couleur des petits triangles de fond tout doit etre supprimés
# et tout replacer sinon les petits triangles passent au premier plan
        efface(tex1)
        efface(tex2)
        efface(tex3)
        efface(cer1)
        efface(cer2)
        efface(cer3)
        efface(cer4)
        efface(pol4)
        efface(pol1)
        efface(pol2)
        efface(pol3)
            
        for k in range (0, int(LargeurFenetre/2) - int(0.01875*LargeurFenetre), 30) :
                for l in range (0, int(LongueurFenetre), 30) :
                    pol = polygone([(k, l), (k+30, l), (k+15, l+30)], remplissage=lst_col[i])
                    lst_com_pol.append(pol)
                    
        for k in range (int(LargeurFenetre/2) - int(0.01875*LargeurFenetre), int(LargeurFenetre), 30) :
            for l in range (0, int(LongueurFenetre), 30) :
                pol = polygone( [(k, l), (k+30, l), (k+15, l+30)], remplissage=lst_col[j])
                lst_com_pol.append(pol)
                    
        rec1 = rectangle( 1/10.5 * LargeurFenetre, 1/13.5 * LongueurFenetre
        , 5.05/6 * LargeurFenetre, 10/13.5 * LongueurFenetre
        , remplissage='goldenrod')
        
        pol1 = polygone( [(poly_620,poly_480), (poly_620,poly_520), (poly_645,poly_500)], remplissage='White')
        pol2 = polygone( [(poly_180,poly_480), (poly_180,poly_520), (poly_155,poly_500)], remplissage='White')
        pol3 = polygone( [(poly_1320,poly_480), (poly_1320,poly_520), (poly_1345,poly_500)], remplissage='White')
        pol4 = polygone( [(poly_880,poly_480), (poly_880,poly_520), (poly_855,poly_500)], remplissage='White')
        
        tex1 = texte( LargeurFenetre / 2.52 , 0.150 * LongueurFenetre
        , "Bataille d", taille = int(0.03125 * LargeurFenetre)
        , ancrage = "center", couleur = lst_col[i])
        
        tex2 = texte( LargeurFenetre / 1.77, 0.150 * LongueurFenetre
        , "e Boules", taille = int(0.03125 * LargeurFenetre)
        , ancrage = "center", couleur = lst_col[j])
        
        cer1 = cercle( 0.25 * LargeurFenetre, 0.5 * LongueurFenetre, 0.125 * LargeurFenetre, remplissage = str(lst_col[i]))
        cer2 = cercle( 0.6875 * LargeurFenetre, 0.5 * LongueurFenetre, 0.125 * LargeurFenetre, remplissage = str(lst_col[j]))
        cer3 = cercle( 0.468175 * LargeurFenetre, 0.35 * LongueurFenetre, 0.06125 * LargeurFenetre, remplissage = 'dimgrey')
        cer4 = cercle( 0.468175 * LargeurFenetre, 0.35 * LongueurFenetre, 0.05125 * LargeurFenetre, remplissage = 'goldenrod')
        tex3 = texte( 0.468175 * LargeurFenetre, 0.355 * LongueurFenetre, 'Continuer', ancrage = "center", taille = int(0.015625 * LargeurFenetre))
############################################################# Fin de fonction Accueil #############################################################


def Reprendre() :
    
    """
    Permet de créer l'écran Reprendre du jeu
    """
    
# Rectangle de fond de l'écran reprendre
    rectangle( 0, 0, LargeurFenetre, LongueurFenetre, remplissage = 'dimgrey')
# Petit triangle de fond de l'écran reprendre
    alt = random.randint( 0, len(lst_col) - 1)
    for k in range (0, LargeurFenetre , 30) :
        for l in range (0, int(LongueurFenetre), 30) :
            pol = polygone( [(k, l), (k+30, l), (k+15, l+30)], remplissage = 'white')
            
# Rectangle qui contient les bouton carger la sauvegarde et nouvelle partie         
    rec1 = rectangle( 1/10.5 * LargeurFenetre, 1/15.5 * LongueurFenetre, 5.05/6 * LargeurFenetre, 10/13.5 * LongueurFenetre, remplissage = 'goldenrod')

# Intitulé de notre jeu qui s'aafiche à l'écran Reprendre
    tex1 = texte( LargeurFenetre / 2.52 , 0.110 * LongueurFenetre
    , "Bataille d", taille = int(0.03125 * LargeurFenetre)
    , ancrage = "center", couleur = 'white')
    
    tex2 = texte( LargeurFenetre / 1.77, 0.110 * LongueurFenetre
    , "e Boules", taille = int(0.03125 * LargeurFenetre)
    , ancrage = "center", couleur = 'white')
    
# Cercles et textes des boutons charger la sauvegarde et nouvelle partie
    boule1 = cercle( 0.28 * LargeurFenetre, 0.4 * LongueurFenetre, 0.15125 * LargeurFenetre, remplissage = 'dimgrey')
    boule12 = cercle( 0.28 * LargeurFenetre, 0.4 * LongueurFenetre, 0.13 * LargeurFenetre, remplissage = 'white')
    texte1 = texte( 0.28 * LargeurFenetre, 0.405 * LongueurFenetre, 'Nouvelle Partie', ancrage = "center", taille = int(0.015625 * LargeurFenetre))
    boule2 = cercle( 0.655 * LargeurFenetre, 0.4 * LongueurFenetre, 0.15125 * LargeurFenetre, remplissage = 'dimgrey')
    boule22 = cercle( 0.655 * LargeurFenetre, 0.4 * LongueurFenetre, 0.13 * LargeurFenetre, remplissage = 'white')
    texte2 = texte( 0.65 * LargeurFenetre, 0.405 * LongueurFenetre, 'Charger la sauvegarde', ancrage = "center", taille = int(0.015625 * LargeurFenetre))

# Permet de voir si un des deux bouton est cliqué
    while True :
        x1, y1, type_clique = attente_clic()
        
        # Bouton Nouvelle Partie
        if inter_in(0, x1, y1, [[0.28 * LargeurFenetre, 0.4 * LongueurFenetre, 0.13 * LargeurFenetre]]) :
            efface_tout()
            return False
        
        # Bouton Charger la sauvegarde
        if inter_in(0, x1, y1, [[0.655 * LargeurFenetre, 0.4 * LongueurFenetre, 0.13 * LargeurFenetre]]) :
            efface_tout()
            return True
############################################################### Fin de fonction Reprendre ###############################################################


def choix_fonction() :
    """
    Affiche les différents choix de fonctionnalité 
     et permet de lancer ceux qio ont été selectionnés.
    """
    
# Rectangle de fond de l'écran reprendre
    rectangle( 0, 0, LargeurFenetre, LongueurFenetre, remplissage = 'dimgrey')
# Petit triangle de fond de l'écran reprendre
    alt = random.randint( 0, len(lst_col) - 1)
    for k in range (0, LargeurFenetre , 30) :
        for l in range (0, int(LongueurFenetre), 30) :
            pol = polygone( [(k, l), (k+30, l), (k+15, l+30)], remplissage = 'white')
            
# Rectangle qui contient les bouton carger la sauvegarde et nouvelle partie         
    rec1 = rectangle( 1/10.5 * LargeurFenetre, 1/13.5 * LongueurFenetre, 5.05/6 * LargeurFenetre, 10/13.5 * LongueurFenetre, remplissage = 'goldenrod')

# Intitulé de notre jeu qui s'aafiche à l'écran Selection d'Option    
    texte( LargeurFenetre / 2.52 , 0.150 * LongueurFenetre
    , "Bataille d", taille = int(0.03125 * LargeurFenetre)
    , ancrage = "center", couleur = 'white')
    
    texte( LargeurFenetre / 1.77, 0.150 * LongueurFenetre
    , "e Boules", taille = int(0.03125 * LargeurFenetre)
    , ancrage = "center", couleur = 'white')
    
    
    liste_nom_variante = ["Sablier", "Scores", "Taille des \nboules", "Version\ndynamique", "Terminaison", "Obstacles"]
    coor_cercle = []
    com_nom_variante = 0
    dict_carre_grise = dict()
    dict_texte_grise = dict()
    lst_coor=[]

# Permet de placer les boutons et les textes pour selectionner les Options
    for i in range (1, 4) :
        for j in range (1, 3) :
            
            cercle( (i * (LargeurFenetre / 6) ) - (LargeurFenetre / 12 + 0.046875 * LargeurFenetre) + 0.28125 * LargeurFenetre
            , (j * 1.25 * LongueurFenetre / 6) - (LongueurFenetre / 12 - 0.2 * LongueurFenetre)
            , 0.06125 * LargeurFenetre, epaisseur = 3, remplissage = 'dimgrey')
 
            coor_cercle.append( [(i * (LargeurFenetre / 6)) - (LargeurFenetre / (6 * 2) + 0.046875 * LargeurFenetre) + 0.28125 * LargeurFenetre
            , (j * 1.25 * LongueurFenetre / 6) - (LongueurFenetre / 12 - 0.2 * LongueurFenetre)])
            
            texte( (i * (LargeurFenetre / 6)) - (LargeurFenetre / (6 * 2) + 0.046875 * LargeurFenetre) + 0.28125 * LargeurFenetre
            , (j * 1.25 * LongueurFenetre / 6) - (LongueurFenetre / (6 * 2) - 0.2 * LongueurFenetre)
            , liste_nom_variante[com_nom_variante], ancrage = "center", taille = int(0.015625 * LargeurFenetre))

            lst_coor.append((i,j))
            com_nom_variante+=1
            
    com_nom_variante = 0
    liste_fonction = []

# Place le bouton continuer avec un texte et un fond
    fond_bt_continuer = rectangle( 0.69 * LargeurFenetre, 0.64 * LongueurFenetre, 0.81 * LargeurFenetre
    , 0.71 * LongueurFenetre, couleur = "black", remplissage = "dimgrey")
    
    bt_continuer = rectangle( 0.7 * LargeurFenetre, 0.65 * LongueurFenetre, 0.8 * LargeurFenetre
    , 0.7 * LongueurFenetre, couleur = "black", remplissage = "white")
    
    texte( 0.75 * LargeurFenetre, 0.675 * LongueurFenetre, "Continuer", "Black"
    , taille = int(0.0125) * LargeurFenetre, ancrage = "center")

# Permet de voir si une option est sélectionné ou si le joueur veut continuer
    while True :
        x, y, type_clique = attente_clic()
        
        if inter_rect(0, x, y, 0.7 * LargeurFenetre, 0.65 * LongueurFenetre, 0.8 * LargeurFenetre, 0.7 * LongueurFenetre) :
            break
        
        for i in range (len(coor_cercle)) :
            
            if ((coor_cercle[i][0] - x) ** 2) + ((coor_cercle[i][1] - y) ** 2) < (0.06125 * LargeurFenetre) ** 2 :

                if i in liste_fonction :
                    liste_fonction.remove(i)
                    efface(dict_carre_grise[i])
                    efface(dict_texte_grise[i])
                    dict_carre_grise.pop(i)
                    
                else :
                    k, j = lst_coor[i]
                    
                    cercle_tempo = cercle(coor_cercle[i][0], coor_cercle[i][1]
                    , 0.06125 * LargeurFenetre, epaisseur = 3, remplissage = 'white')
                    
                    tex = texte( (k * (LargeurFenetre / 6)) - (LargeurFenetre / (6 * 2) + 0.046875 * LargeurFenetre) + 0.28125 * LargeurFenetre
                    , (j * 1.25 * LongueurFenetre / 6) - (LongueurFenetre / (6 * 2) - 0.2 * LongueurFenetre)
                    , liste_nom_variante[i], ancrage = "center", taille = int(0.015625 * LargeurFenetre))
                    
                    liste_fonction.append(i)
                    dict_carre_grise[i] = cercle_tempo
                    dict_texte_grise[i] = tex
                    
        else:
            continue  
        
    efface_tout()
    return  liste_fonction
############################################################# Fin de fonction choix_fonction #############################################################


def inter_in(r, x, y, lst) :
    """
    Permet de vérifier si un cercle est contenu dans 
     un cercle ou non.
    
    :param int r : rayon cercle
     :param int x : abcisse centre cercle
     :param int y : ordonnée centre cercle
     :param list lst : [[abcisse, ordonnée]] 
    """
    for i in range (len(lst)) :
        if ((lst[i][0] - x)**2) + ((lst[i][1] - y)**2) < (lst[i][2])**2:
            return True
    return False
############################################################# Fin de fonction inter_in #############################################################


def inter_out( r, x, y, lst) :
    """
    Determine si il y a une intersection entre deux cercles
    
    :param int r : raron cercle
     :param int x : abcisse cercle
     :param int y : ordonnée cercle
     :param list lst : [[abcisse, ordonnée]] 
    """
    com = 0 # compteur qui permet de compter le nombre d'intersection en dehors du cercle
    for i in range (len(lst)) :
        x_a = lst[i][0]
        y_a = lst[i][1]
        r_a = lst[i][2]
        a = 2 * (x-x_a)
        b = 2 * (y-y_a)
        c = ((x - x_a)**2) + ((y - y_a)**2) - (r**2) + (r_a**2)
        delta = ((2 * a * c)**2) - 4 * ((a**2) + (b**2)) * ((c**2) - (b**2) * (r_a**2))
        if delta >= 0 : 
            com += 1
    if com > 0 :
        return True
    else :
        return False
############################################################# Fin de fonction inter_out #############################################################

        
def inter_rect(r, x, y, ax, ay, bx, by) :
    """
    Permet de vérifier si un cercle est contenu dans 
     un rectangle ou non.
    
    :param int r : rayon du cercle
     :param int x : abcisse centre cercle
     :param int y : ordonné centre cercle
     :param int ax : abcisse premier coin du rectangle
     :param int ay : ordonné premier coin du rectangle
     :param int bx : abcisse deuxième coin du rectangle
     :param int by : ordonné deuxième coin du rectangle
    """
    X = ax + r < x < bx - r
    Y = ay + r < y < by - r
    if Y == True and X == True :
        return True
    else :
        return False 
############################################################# Fin de fonction inter_rect #############################################################    


def inter_obstacle(r, x, y, lst) :
    """
    vérifie les intersection entre les obstacles et les boules
    """
    com = 0
    for i in lst :
        if inter_out(r, x, y, lst) == False and inter_in(r, x1, y1, lst) == False :
            com += 1 
    if com == 4 :
        return True
    else:
        return False
############################################################# Fin de fonction inter_obstacle #############################################################    


def remplace_boule(com, r, x, y, lst, lst_com, lst_score) :
    """
    Permet de supprimer un cercle si le clic est a l'interieur 
     de celui-ci et de le diviser en deux autres cercles tangents, 
     l'emplacement du clic représente le centre du premier cercle. 
     Les coordonnées du cercle initial seront supprimées de la liste lst
     et celles des deux nouveaux cercle y seront ajoutées.
     
    :param int com : compteur 
     :param int r : rayon cercle
     :param int x : abcisse centre cercle
     :param int y : ordonnée centre cercle
     :param list lst : [[abcisse, ordonnée, ordonné]] 
     :param list lst_com :[boule1,..,boulen] 
    """
    com2 = 1 # compteur qui permet de compter le nombre d'intersection a l'interieur d'un cercle
    for i in range (len(lst)) :
        # Permet de voir avec combien de cercle de la couleur opposée le cercle placé est en intersection
        if ((lst[i][0] - x)**2) + ((lst[i][1] - y)**2) < (lst[i][2])**2 :
           com2 += 1 
    # Partie qui permet d'ittérer sur le nombre d'intersection obtenue précedemment
    for i in range (com2) :
        # Partie qui permet de remplacer un cercle par deux cercles tangents et inscrit dans le cercle supprimé
        for i in range (len(lst)) :
            if len(lst) > 0 :
                r = lst[i][2]
                x_a = lst[i][0]
                y_a = lst[i][1]
                if x == x_a and y == y_a :
                    continue
                if ((lst[i][0] - x)**2) + ((lst[i][1] - y)**2) < r**2 : 
                    efface(lst_com[i])
                    lst.pop(i)
                    lst_com.pop(i)
                    lst_score = ajouter_score(lst_score, x, y, r, None)
                    r_p = r - (sqrt(((x_a - x)**2) + ((y_a - y)**2))) # rayon du cercle dont les coordonnées du centre sont les coordonnées du clic
                    r_g = r - r_p # le rayon du cercle tangeant a un autre cercle et tout deux contenus dans un cercle 
                    s = r - (2 * r_p)
                    t = s - r_g
                    v_x = (x - x_a) / (sqrt(((x - x_a)**2) + ((y - y_a)**2)))
                    v_y = (y - y_a) / (sqrt(((x - x_a)**2) + ((y - y_a)**2)))
                    x_g = x_a + (t * v_x)
                    y_g = y_a + (t * v_y)
                    
                    # Permet de creer les nouveaux cercles du joueur 1
                    if com % 2 == 0 :
                        boule = cercle(x, y, r_p, remplissage = col_j2)
                        lst.append([x, y, r_p])
                        lst_com.append(boule)
                        lst_score = ajouter_score(lst_score, x, y, r_p, col_j1)
                        boule = cercle(x_g, y_g, r_g, remplissage = col_j2)
                        lst.append([x_g, y_g, r_g])
                        lst_com.append(boule)
                        break
                    
                    # Permet de creer les nouveaux cercles du joueur 2
                    else:
                        boule = cercle(x, y, r_p, remplissage = col_j1)
                        lst.append([x, y, r_p])
                        lst_com.append(boule)
                        lst_score = ajouter_score(lst_score, x, y, r_p, col_j2)
                        boule = cercle(x_g, y_g, r_g, remplissage = col_j1)
                        lst.append([x_g, y_g, r_g])
                        lst_com.append(boule)
                        break
############################################################# Fin de fonction remplace_boule #############################################################                        


def sablier(com, r, ax, ay, bx, by, com2) :
    """
    Créée un sablier tant bien visuel que fonctioel
    
    :param int com : compteur (compte les tours des joueurs)
     :param int r : rayon cercle
     :param int ax : abcisse coin superieur gauche rectangle de l'aire de jeu
     :param int ay : ordonnée coin superieur gauche rectangle de l'aire de jeu
     :param int bx : abcisse coin inferieur droit rectangle de l'aire de jeu
     :param int by : ordonnée coin inferieur droit rectangle de l'aire de jeu
     :param int com2 : Compteur qui permet de limiter le nombre d'apppui sur une option
    """
    
    # permet d'afficher le sablier
    text = texte(0.15 * LargeurFenetre, 0.195 * LongueurFenetre, com, ancrage = 'center', taille = int(0.0125 * LargeurFenetre))
    cer = cercle(0.15 * LargeurFenetre, 0.195 * LongueurFenetre, 0.03125 * LargeurFenetre, remplissage = 'snow', epaisseur = 3)
    
    # permet de faire le décompte du sablier
    while com > 0.1 :
        com -= 0.1
        time.sleep(0.06)
        efface(text)
        text = texte(0.15 * LargeurFenetre, 0.195 * LongueurFenetre, round(com, 3), ancrage = 'center', taille = int(0.0125 * LargeurFenetre))
        mise_a_jour()
        
        # permet de voir pendant le décompte si un evenement clic ou touche a lieu
        x = donne_evenement()
        # permet de placer un cercle suivant les différente condition ci-dessous
        if x[0] == 'ClicGauche' or x[0] == 'ClicDroit' :
            
            # Compteur qui permet de ne pas réafficher les fonctions si elles ont déja été seléctionné
            if com2 == 0:
                x1,y1 = coor_timer(str(x[1]))
                
                # Bouton du Numpad
                if inter_rect(r, x1, y1, ax, ay, bx, by) :
                    return str(x[1]), 0
                
                # Bouton quitter 
                if inter_rect(0, x1, y1, ax_rect2, ay_rect2, bx_rect2, by_rect2) == True : # permet de voir si le bouton quitter est cliqué
                    ferme_fenetre()
                    
                # Bouton Pause
                if inter_rect(0, x1, y1, ax_pause, ay_pause, bx_pause, by_pause) == True :
                    Sauvegarder()
                    
                if 4 in lst_fonction :
                    # permet de voir si le bouton terminaison est déclanché
                    if inter_rect(0 ,x1, y1, ax_rect_terminaison, ay_rect_terminaison, bx_rect_terminaison, by_rect_terminaison) == True: 
                        return str(x[1]), com
                    
                if 2 in lst_fonction :
                        # Bouton Taille Boule
                        if inter_rect(0, x1, y1, ax_Tb, ay_Tb, bx_Tb, by_Tb) == True :
                            return str(x[1]), com
                        
            # cas ou on ne peut pas recliquer sur les boutons taille boule et terminaison
            else :
                 x1,y1 = coor_timer(str(x[1]))
                 
                 if inter_rect(r, x1, y1, ax, ay, bx, by) :
                     return str(x[1]), 0
                 
                 if inter_rect(0, x1, y1, ax_rect2, ay_rect2, bx_rect2, by_rect2) == True : # permet de voir si le bouton quitter est cliqué
                     ferme_fenetre()
                     
        # Permet d'afficher le score avec la touche s dans la variante Sablier
        if 1 in lst_fonction :
            while x[0] == "Touche" :
                x1, y1 = coor_timer(str(x[1]))
                scores(lst_j1, lst_j2,  coor_timer2(str(x[1])))
                break
            
        if  round(com, 2) == 0 :
            return 0, 0
############################################################# Fin de fonction remplace_boule #############################################################                        


def coor_timer(chaine) :
    """
    Permet d'extraire dans une liste les coordonées d'un clics '
    
    :param str chaine : chaine qui contient des coordonées x et y
    """
    chaine2 = ' <>'
    lst = []
    reti = ''
    for i in chaine :
        if i not in chaine2 :
            reti += i
        else : 
            if 'x=' in reti or 'y=' in reti:
                lst.append(int(reti[2:]))
                reti = ''
            reti = ''
    return lst
############################################################# Fin de fonction coor_timer #############################################################


def coor_timer2(chaine) :
    """
    Permet d'extraire le nom d'une touche cliquée '
    
    :param str chaine : chaine qui contient des coordonées x et y
    """
    debut = chaine.find("char='")+6
    fin = chaine.index("'", debut)
    return chaine[debut:fin]
############################################################# Fin de fonction coor_timer2 #############################################################     


def scores(lst_j1, lst_j2, touche) :
    """
    fonctions qui permet d'afficher le score actuel pendant une partie
    
    :param str touche : permet de connaitre la touche selectionner sur le clavier
     :param list lst_j1 : liste de tuples (abscisse_centre, ordonnée_centre, rayon)
     :param list lst_j2 : liste de tuples (abscisse_centre, ordonnée_centre, rayon) 
    """
    # Peret d'afficher les scores si le bouton s est cliqué
    if touche == "s":
        a = func_somme_aire(lst_score ,col_j1,col_j2, r, lst_j1, lst_j2)
        timer = 2
        rec_score = rectangle(0.3125 * LargeurFenetre, 0.200 * LongueurFenetre, 0.625 * LargeurFenetre, 0.600 * LongueurFenetre, couleur = "black", remplissage = "white")
        score_j1 = texte(0.46875 * LargeurFenetre, 0.300 * LongueurFenetre, "score joueur 1 : " + str(round(a[0], 1)), ancrage = "center", couleur = col_j1, taille = int(0.0125 * LargeurFenetre))
        score_j2 = texte(0.46875 * LargeurFenetre, 0.500 * LongueurFenetre, "score joueur 2 : " + str(round(a[1], 1)), ancrage = "center", couleur = col_j2, taille = int(0.0125 * LargeurFenetre))
        mise_a_jour()
        while timer != 0:
            time.sleep(1)
            mise_a_jour()
            timer -= 1
    else:
        return None
    efface(rec_score)
    efface(score_j1)
    efface(score_j2)
    return [a[0], a[1]]
############################################################# Fin de fonction score #############################################################


def ajouter_score(lst_score, x, y, r, col_j) :
    """
    Permet d'atribuer une couleur a des coordonnées
    
    :param list lst_score : Liste de tuples (x, y, couleur)
     :param int x : Abscisse du clic (ou abscisse du centre du cercle)
     :param int y : Ordonnée du clic (ou ordonnée du centre du cercle)
     :param int r : Rayon du cecle
     :param int col_j : Couleur du joueur
    """
    for i in range (len(lst_score)) :
        if ((lst_score[i][0] - x) <= r and (lst_score[i][0] - x) >= 0) and ((lst_score[i][1] - y) <= r and (lst_score[i][1] - y) >= 0) :
            lst_score[i] = (lst_score[i][0], lst_score[i][1], col_j)
    return lst_score
############################################################# Fin de fonction ajouter_score #############################################################


def func_somme_aire(lst_score, col_j1, col_j2, r, lst_j1, lst_j2) :
    """
    Calcul le score total de chaque joueur
    
    :param list lst_score : Liste de tuples (x, y, couleur)
     :param str col_j1 : Couleur du joueur 1
     :param str col_j2 : Couleur du joueur 2
     :param int r : Rayon du cecle au debut du jeu
     :param list lst_j1 : liste de tuples (abscisse_centre, ordonnée_centre, rayon)
     :param list lst_j2 : liste de tuples (abscisse_centre, ordonnée_centre, rayon) 
    """
    somme_aire_1, somme_aire_2  = compte_score(lst_score,col_j1, col_j2)
    for i in lst_j1:
        if i[2] > r :
            somme_aire_1 += (i[2]-r)*10
    for i in lst_j2:
        if i[2] > r :
            somme_aire_2 += (i[2] - r)*10
    if somme_aire_2 > somme_aire_1 :
        gagnant = col_j2
    if somme_aire_2 == somme_aire_1 :
        gagnant = "grey"
    if somme_aire_2 < somme_aire_1 :
        gagnant = col_j1
    
    return [somme_aire_1, somme_aire_2, gagnant]
############################################################# Fin de fonction func_somme_aire #############################################################


def compte_score(lst_score, col_j1, col_j2) :
    """
    Parcour la liste de score pour calculer le score de chaque joueurs
    
    :param list lst_score : Liste de tuples (x, y, couleur)
     :param str col_j1 : Couleur du joueur 1
     :param str col_j2 : Couleur du joueur 2
    """
    com_j1 = 0
    com_j2 = 0
    for i in lst_score :
        if i[2] == col_j1 :
            com_j1 += 1
        elif i[2 ] == col_j2 :
            com_j2 += 1
    return com_j1, com_j2
############################################################# Fin de fonction compte_score #############################################################

def Affiche_TailleB(com, budget1, budget2, couleur1, couleur2, x1, y1) :
     """
     Permet d'agrandir le rayon d'un cercle
     
     :param int com : compteur qui permet de compter les tours
      :param int budget1 : Budget joueur 1 (pour limiter l'aggrnadissement des boules)
      :param int budget1 : Budget joueur 2 (pour limiter l'aggrnadissement des boules)
      :param str col_j1 : Couleur du joueur 1
      :param str col_j2 : Couleur du joueur 2
      :param int x1 : Abscisse du clic (ou abscisse du centre du cercle)
      :param int y1 : Ordonnée du clic (ou ordonnée du centre du cercle)
     """
     lst = [[ ], [ ]]
     
     # Permet d'afficher le numpad pour que le joueur 1 puisse aggrandir le cercle
     # Permet également de gérer le budget du joueur 1
     if com % 2 == 0 :
        if budget1 != 0 :
            lst = affiche_numpad(numpad())
        txt = texte(0.75 * LargeurFenetre, 0.14 * LongueurFenetre, "Budget joueur 1 :", couleur1, taille = int(0.01125 * LargeurFenetre))
        txt1 = texte(0.7875 * LargeurFenetre, 0.170 * LongueurFenetre, budget1, taille = int(0.011875 * LargeurFenetre))
        mise_a_jour()
        if budget1 == 0 :
            time.sleep(2)
            efface(txt)
            efface(txt1)
            for i in lst[0] :
                efface(i)
            for i in lst[1] :
                efface(i)
            return 0
        tarif = numpad_fonc()
        
        # Permet d'éviter que le joueur ne puisse depasser le budget
        while tarif < 0 or tarif > budget1 :
            tarif=numpad_fonc()
            
    # Permet d'afficher le numpad pour que le joueur 2 puisse aggrandir le cercle
    # Permet également de gérer le budget du joueur 2
     else :
        if budget2 != 0 : 
            lst = affiche_numpad(numpad()) 
        txt = texte(0.75 * LargeurFenetre, 0.140 * LongueurFenetre, "Budget joueur 2 :", couleur2, taille = int(0.01125 * LargeurFenetre))
        txt1 = texte(0.7875 * LargeurFenetre, 0.17 * LongueurFenetre, budget2, taille = int(0.01125 * LargeurFenetre))
        mise_a_jour()
        if budget2 == 0 :
            time.sleep(2)
            efface(txt)
            efface(txt1)
            for i in lst[0] :
                efface(i)
            for i in lst[1] :
                efface(i)
            return 0
        tarif = numpad_fonc()
        
        # Permet d'éviter que le joueur ne puisse depasser le budget
        while tarif < 0 or tarif > budget2 :
            tarif = numpad_fonc()
    
     for i in lst[0] :
         efface(i)
     for i in lst[1] :
         efface(i)
     efface(txt)
     efface(txt1)
     return tarif
 ############################################################# Fin de fonction Affiche_TailleB #############################################################


def affiche_numpad(lst) :
    """
    Permet de placer les boutons et texte su Numpad
    
    :param list lst : Liste qui contient les coordonnées des boutons qui constituent le Numpad
    """
    # Rectangle contenant tout le Numpad
    rec = rectangle(0.734375 * LargeurFenetre, 0.200 * LongueurFenetre, 0.854375 * LargeurFenetre, 0.500 * LongueurFenetre, remplissage = 'lightgrey')
    
    # Rectangle qui représente l'écran du Numpad
    rec2 = rectangle(0.7375 * LargeurFenetre, 0.205 * LongueurFenetre, 0.85125 * LargeurFenetre, 0.245 * LongueurFenetre, remplissage = 'beige')
    
    # Listes qui contienent tout les les éléments du Numpad, permettront de les effacers par la suite
    lst2 = [rec, rec2]
    lsttxt = []
    
    # Permet de placer les élements du Numpad
    for i in lst :
        ax = i[0]
        bx = i[1]
        ay = i[2]
        by = i[3]
        rec = rectangle(ax, ay, bx, by, remplissage = "beige")
        lst2.append(rec)
        
    x_texte = 0.75625 * LargeurFenetre
    y_texte = 0.275 * LongueurFenetre
    numpad_element = ["1", "4", "7", "Supr", "2", "5", "8", "0" ,"3", "6", "9", "Entrer"]
    com = 0
    
    # Permet de placer le texte du Numpad
    for j in range (3) :
        for i in range (4) :
            text = texte(x_texte, y_texte, numpad_element[com], ancrage = "center", taille = int(0.008125 * LargeurFenetre))
            lsttxt.append(text)
            y_texte += 0.065 * LongueurFenetre
            com += 1
        x_texte += 0.0375 * LargeurFenetre
        y_texte = 0.275 * LongueurFenetre
        
    return lst2, lsttxt
 ############################################################# Fin de fonction affiche_numpad #############################################################


def numpad() :
    """
    Permet de creer une liste conetenant les coordonnées des boutons du Numpad
    """
    liste_coor_numpad = []
    l_numpad = 0.1125 * LargeurFenetre
    L_numpad = 0.270 * LongueurFenetre
    ax = 0.7375 * LargeurFenetre
    ay = 0.250 * LongueurFenetre
    bx = (0.73125 * LargeurFenetre)+(L_numpad / 4)
    by = (0.220 * LongueurFenetre) + (l_numpad / 2.2)
    
    # Permet de créer les rectangles
    for j in range (3) :
        for i in range (4) :
            liste_coor_numpad.append([ax, bx, ay, by])
            ay += 0.065 * LongueurFenetre
            by += 0.065 * LongueurFenetre
        ax += 0.038125 * LargeurFenetre
        bx += 0.038125 * LargeurFenetre
        ay = 0.250 * LongueurFenetre
        by = (0.220 * LongueurFenetre) + (l_numpad / 2.2)
        
    return liste_coor_numpad
############################################################# Fin de fonction numpad #############################################################


def numpad_fonc() :
    """
    Permet de creer la partie fonctionnelle du Numpad
    """
    chiffre = ""
    lst = (numpad())
    lst2 = [1, 4, 7, None, 2, 5, 8, 0, 3, 6, 9, 0]
    text = texte(0.50625 * LargeurFenetre, 0.530 * LongueurFenetre, chiffre, ancrage = "center", taille = int(0.009375 * LargeurFenetre))
    
    # Boucle qui permet de voir si un bouton est cliqué
    while True :
        x1, y1, type_clique = attente_clic()
        efface(text)
        mise_a_jour()
        
        while inter_rect(0, x1, y1, 0.734375 * LargeurFenetre, 0.200 * LongueurFenetre, 0.854375 * LargeurFenetre, 0.500 * LongueurFenetre) == False :
            x1, y1, type_clique = attente_clic()
        
        # Boucle qui va permettre de voir si un bouton est cliqué s'arrete si le bouton enter est cliqué
        for i in range (len(lst)) :
                if chiffre != '' :
                        if inter_rect(0, x1, y1, lst[11][0], lst[11][2], lst[11][1], lst[11][3]) :
                            return int(chiffre)
                        
                if inter_rect(0, x1, y1, lst[i][0], lst[i][2], lst[i][1], lst[i][3]) :
                    if lst2[i] != None :
                        chiffre += str(lst2[i])
                        
                    else :
                        chiffre = chiffre[:-1]
                    text = texte(0.79375 * LargeurFenetre, 0.225 * LongueurFenetre, chiffre, ancrage = 'center', taille = int(0.009375 * LargeurFenetre))
                    mise_a_jour()
############################################################# Fin de fonction numpad_fonc #############################################################              
                    

def Version_dynamique(lst, lst_com, lst2, color) :
    """
    Option version dynamique qui aggrandie les boules progressivement
    
    :param list lst : [[abcisse, ordonnée, rayon]] 
     :param list lst_com :[boule_1,..,boule_n]
     :param list lst2 : [[abcisse, ordonnée, rayon]] 
     :param str  color : couleur des boules de la couleur qui s'aggrandie
    """
    # Permet de faire grandir les cercles du joueur 1 et 2 en meme temps
    k = len(lst)
    if len(lst) > len(lst2) :
        k = len(lst2) 
    
    # Permet de faire grandir les cercles petit a petit jusqu'a atteindre grossissement
    # si les conditions ne les en empeches pas
    grossisement = param_dict["grossisement"]
    for j in range(grossisement) :
        for i in range(k):
            x = lst[i][0]
            y = lst[i][1]
            r = lst[i][2]
            if inter_out(lst[i][2], x, y, lst2) == False and inter_in(lst[i][2], x, y, lst2) == False and inter_rect(lst[i][2], x, y, ax_rect, ay_rect, bx_rect, by_rect) == True :
                
                if 5 in lst_fonction and inter_obstacle(lst[i][2], x, y, lst_cercle) == True :
                    lst[i][2] = lst[i][2] + 1
                    efface(lst_com[i])
                    lst_com.pop(i)
                    boule = cercle(x, y, r, remplissage = color)
                    lst_com.insert(i, boule)
                    
                elif 5 not in lst_fonction :
                    lst[i][2] = lst[i][2] + 1
                    efface(lst_com[i])
                    lst_com.pop(i)
                    boule = cercle(x, y, r, remplissage = color)
                    lst_com.insert(i, boule) 
############################################################# Fin de fonction Version_dynamique #############################################################


def obstacles() :
    """
    permet de mettre des obstacles sur l'aire de jeu qui poujrrons entraver les clic de l'utilisateur
    """
    # Permet de creer aléatoirement des obstacles uniquement circulaire tout en restant dans l'aire de jeu
    ax_rect = int(0.2125 * LargeurFenetre)
    ay_rect = int(0.001 * LongueurFenetre)
    bx_rect = int(0.73125 * LargeurFenetre)
    by_rect = int(0.830 * LongueurFenetre)
    r1 = random.randint(0, 75)
    r2 = random.randint(0, 75)
    r3 = random.randint(0, 75)
    r4 = random.randint(0, 75)
    xb1, yb1 = random.randint(ax_rect + r1, bx_rect - r1), random.randint(r1, by_rect - r1)
    xb2, yb2 = random.randint(ax_rect + r2, bx_rect - r2), random.randint(r2, by_rect - r2)
    xb3, yb3 = random.randint(ax_rect + r3, bx_rect - r3), random.randint(r3, by_rect - r3)
    xb4, yb4 = random.randint(ax_rect + r4, bx_rect - r4), random.randint(r4, by_rect - r4)
    cercle1 = cercle(xb1, yb1, r1, remplissage = "black")
    cercle2 = cercle(xb2, yb2, r2, remplissage = "black")
    cercle3 = cercle(xb3, yb3, r3, remplissage = "black")
    cercle4 = cercle(xb4, yb4, r4, remplissage = "black")
    return [[xb1, yb1, r1], [xb2, yb2, r2],[xb3, yb3, r3],[xb4, yb4, r4]]
############################################################# Fin de fonction Obstacles #############################################################


def Sauvegarder() :
    """
    Permet de sauvegarder la partie avec un menu pause
    """
    # Permet de creer le menu pause
    menu_pause = rectangle(0.3125 * LargeurFenetre, 1/5 * LongueurFenetre, 0.625 * LargeurFenetre, 3/5 * LongueurFenetre, couleur = "black", remplissage = "dimgrey")
    bouton1 = rectangle(0.38 * LargeurFenetre, 1.5/5 * LongueurFenetre, 0.550 * LargeurFenetre, 1.8/5 * LongueurFenetre, couleur = "black", remplissage = "goldenrod")
    bouton2 = rectangle(0.38 * LargeurFenetre, 2.2/5 * LongueurFenetre, 0.550 * LargeurFenetre, 2.5/5 * LongueurFenetre, couleur = "black", remplissage = "goldenrod")
    texte1 = texte((0.465) * LargeurFenetre, 1.65/5 * LongueurFenetre, 'Reprendre', ancrage = 'center')
    texte2 = texte((0.465) * LargeurFenetre, 2.35/5 * LongueurFenetre, 'Sauvegarder', ancrage = 'center')
    
    # Permet à l'utilisateur de recliquer tant qu'il ne clique pas sur reprendre ou sauvegarder
    while True :
        x2, y2, type_clique = attente_clic()
        while inter_rect(0 ,x2, y2, 0.3125 * LargeurFenetre, 1/5 * LongueurFenetre, 0.625 * LargeurFenetre, 3/5 * LongueurFenetre) == False :
            x2, y2, type_clique = attente_clic()
        
        if inter_rect(0 ,x2, y2, 0.4125 * LargeurFenetre, 1.5/5 * LongueurFenetre, 0.525 * LargeurFenetre, 1.8/5 * LongueurFenetre) == True :
            efface(menu_pause)
            efface(bouton1)
            efface(bouton2)
            efface(texte1)
            efface(texte2)
            return 0
        
        if inter_rect(0 ,x2, y2, 0.4125 * LargeurFenetre, 2.2/5 * LongueurFenetre, 0.525 * LargeurFenetre, 2.5/5 * LongueurFenetre) == True :
            with open("save.txt",'w') as fich_s :
                fich_s.write("lst_j1:" + str(lst_j1) + "\n")
                fich_s.write("lst_j2:" + str(lst_j2) + "\n")
                fich_s.write('lst_fonction:' + str(lst_fonction) + "\n")
                fich_s.write("com:" + str(com) + "\n")
                fich_s.write("com2:" + str(com2) + "\n")
                fich_s.write("nb_tour:"+ str(nb_tour) + "\n")
                fich_s.write("lst_score:" + str(lst_score) + "\n")
                if 5 in lst_fonction :
                    fich_s.write("lst_cercle:" + str(lst_cercle) + "\n")
                    
                if 2 in lst_fonction :
                    fich_s.write("budget1:" + str(budget1) + "\n")
                    fich_s.write("budget2:" + str(budget2) + "\n")
                
                    
                efface(menu_pause)
                efface(bouton1)
                efface(bouton2)
                efface(texte1)
                efface(texte2)
                return 0
############################################################# Fin de fonction Sauvegarder #############################################################


def fenetre_de_fin(gagnant_jeu, col_j1, col_j2) :
    """
    Fenetre de fin qui permet d'afficher le vainqueur avec sa couleur
    :param list gagnant : gagnant de la partie
    """
    efface_tout()
    rectangle(0, 0, 1600, 1000, remplissage = "black")
    

    texte(LargeurFenetre / 2, LongueurFenetre / 2.5, "Le vainqueur est : "
    , ancrage = "center", taille = int(0.031 * LargeurFenetre), couleur = "white")

    for i in range(3, 0, -1) : # compte a rebours de 3 secondes pour le suspens ! 

        compte_a_rebours = texte(LargeurFenetre / 2, LongueurFenetre / 2 + (0.020 * LongueurFenetre)
        , str(i), ancrage = "center", taille = int(0.031 * LargeurFenetre), couleur = "white")
        
        mise_a_jour()
        time.sleep(1)
        efface(compte_a_rebours)
    rectangle(0, 0, 1600, 1000, remplissage = gagnant_jeu[2]) # couleur en fond de qui a gagné 
    texte(LargeurFenetre / 2, LongueurFenetre / 2 * LongueurFenetre, "Le vainqueur est : "
    , ancrage = "center", taille = int(0.031 * LargeurFenetre), couleur = "white")
    
    # Cas ou le joueur 2 gagne
    if gagnant_jeu[2] == col_j2 :
        texte(LargeurFenetre / 2, LongueurFenetre / 2-0.1*LongueurFenetre, col_j2
        , ancrage = "center", taille = int(0.031 * LargeurFenetre), couleur = "white")
        
        texte(LargeurFenetre / 2, LongueurFenetre / 2 
        , "Score : " + str(round(gagnant_jeu[1], 2))
        , ancrage = "center", taille = int(0.031 * LargeurFenetre), couleur = "white")
        
        texte(LargeurFenetre / 2, 0.6 * LongueurFenetre
        , "Score Joueur 1 : " + str(round(gagnant_jeu[0]
        , 2)), ancrage = "center" ,taille = int(0.021875 * LargeurFenetre), couleur = "white")

    # Cas ou le joueur 1 gagne
    if gagnant_jeu[2] == col_j1 :
        texte(LargeurFenetre / 2, LongueurFenetre / 2-0.1 * LongueurFenetre, col_j1
        , ancrage = "center", taille = int(0.031 * LargeurFenetre), couleur = "white")
        
        texte(LargeurFenetre / 2, LongueurFenetre / 2 
        , "Score : " + str(round(gagnant_jeu[0], 2))
        , ancrage = "center", taille = int(0.031 * LargeurFenetre), couleur = "white")
        
        texte(LargeurFenetre / 2, 0.6 * LongueurFenetre
        , "Score Joueur 2 : " + str(round(gagnant_jeu[1], 2))
        , ancrage = "center" ,taille = int(0.021875 * LargeurFenetre), couleur = "white")

    # Cas d'égalité
    if gagnant_jeu[2] == "grey" :
        texte(LargeurFenetre / 2, LongueurFenetre / 2 
                , "Personne\n  Égalité", ancrage = "center"
                , taille = int(0.031 * LargeurFenetre), couleur = "white")
############################################################# Fin de fonction fenetre_de_fin #############################################################

        
#----------------main----------------
if __name__ == "__main__":

    # Permet de prendre les paramètre du fichier paramètre.txt
    param_dict = dict()
    with open("parametre.txt") as parametre: # création du dictionnaire de parametre pour ne lire qu'une fois le fichier
        for line in parametre:
            line = line[:-1]
            (key, val) = line.split(":")
            if "." in val:
                param_dict[key] = float(val) # si il existe un "." dans la ligne il faut l'interpreter comme une valeur a virgule
            else:
                param_dict[key] = int(val) # sinon c'est une valeur entière 

    
    LargeurFenetre = param_dict["LargeurFenetre"]
    LongueurFenetre = param_dict["LongueurFenetre"]
    cree_fenetre(LargeurFenetre, LongueurFenetre)
    r = param_dict["r"]*LargeurFenetre # rayon de base du cercle
    r2=r
    nb_tour = param_dict["nb_tour"]
    
    com=0 # initialisation du compteur qui comptera le nombre de tour
    com2=False
    budget1 = param_dict["budget1"]
    budget2 = param_dict["budget2"]
    tarif=0
    lst_j2=[] # liste qui enregistre les coordonnées et le rayon de chaque cercle joueur2
    lst_j1=[] # liste qui enregistre les coordonnées et le rayon de chaque cercle joueur1
    lst_com_j2=[] # liste qui contient toutes les boules du joueur2
    lst_com_j1=[] # liste qui contient toutes les boules u joueur1
    lst_cerc=[]
    lst_fonction=[]
    
    #----------menu------------
    col_j1, col_j2 =Accueil(LongueurFenetre, LargeurFenetre)
    ax_rect = param_dict["ax_rect"]*LargeurFenetre
    ay_rect = param_dict["ay_rect"]*LongueurFenetre
    bx_rect = param_dict["bx_rect"]*LargeurFenetre
    by_rect = param_dict["by_rect"]*LongueurFenetre

    lst_score = []
    for i in range( int(ax_rect), int(bx_rect)):
        for j in range( int(ay_rect), int(by_rect)):
            lst_score.append((i,j,None))
    
    
    if os.path.isfile('save.txt'):
        if Reprendre()==False:
            lst_fonction = choix_fonction()
            rectangle( 0, 0, LargeurFenetre, LongueurFenetre, remplissage='dimgrey')
            rectangle(ax_rect, ay_rect, bx_rect, by_rect, remplissage="lightgrey")
            # rectangle qui represente l'aire du menu
            rectangle(bx_rect+2, 1, bx_rect+200, by_rect, remplissage="goldenrod")
            rectangle(ax_rect-202, 1, ax_rect-2, by_rect, remplissage="goldenrod")
            if 5 in lst_fonction:
                lst_cercle=obstacles()
            if 2 in lst_fonction:
                tarif=0
                budget1 = param_dict["budget1"]
                budget2 = param_dict["budget2"]

        else:
            save_dict = dict()
            with open("save.txt") as parametre:
                for line in parametre:
                    line = line
                    (key, val) = line.split(":")
                    save_dict[key] = eval(val)

                lst_j1=save_dict['lst_j1']
                lst_j2=save_dict['lst_j2']  
                lst_fonction=save_dict['lst_fonction']   
                com=save_dict['com']
                com2=save_dict['com2']
                nb_tour=save_dict['nb_tour']
                lst_score = save_dict["lst_score"]
                
            if 2 in lst_fonction:
                    budget1 = save_dict["budget1"]
                    budget2 = save_dict["budget2"]
                    
            if 5 in lst_fonction:
                    lst_cercle=save_dict['lst_cercle']
                    
            rectangle( 0, 0, LargeurFenetre, LongueurFenetre, remplissage='dimgrey')
            rectangle(ax_rect, ay_rect, bx_rect, by_rect, remplissage="lightgrey")
            # rectangle qui represente l'aire du menu
            rectangle(bx_rect+2, 1, bx_rect+200, by_rect, remplissage="goldenrod")
            rectangle(ax_rect-202, 1, ax_rect-2, by_rect, remplissage="goldenrod")
            
            if len(lst_j1)>0:
                for i in lst_j1:
                    boule=cercle(i[0], i[1], i[2], remplissage=col_j1)
                    lst_com_j1.append(boule)
                    
            if len(lst_j2)>0:
                for i in lst_j2:
                    boule=cercle(i[0], i[1], i[2], remplissage=col_j2)
                    lst_com_j2.append(boule)   
            
            if 5 in lst_fonction:
                if len(lst_fonction)>0:
                    for i in lst_cercle:
                        boule=cercle(i[0], i[1], i[2], remplissage='black')


    else :
        lst_fonction=choix_fonction()
        rectangle( 0, 0, LargeurFenetre, LongueurFenetre, remplissage='dimgrey')
        rectangle(ax_rect, ay_rect, bx_rect, by_rect, remplissage="lightgrey")
        # rectangle qui represente l'aire du menu
        rectangle(bx_rect+2, 1, bx_rect+200, by_rect, remplissage="goldenrod")
        rectangle(ax_rect-202, 1, ax_rect-2, by_rect, remplissage="goldenrod")
        if 5 in lst_fonction:
            lst_cercle=obstacles()

    texte(0.15*LargeurFenetre, 0.07*LongueurFenetre, "Tours restants", taille=int(0.01125*LargeurFenetre), ancrage="center")

    ax_pause=0.7625*LargeurFenetre
    ay_pause=0.67*LongueurFenetre
    bx_pause=0.825*LargeurFenetre
    by_pause=0.72*LongueurFenetre
    rectangle(ax_pause,ay_pause, bx_pause, by_pause, remplissage='cornflowerblue')
    texte(0.76875*LargeurFenetre, 0.68*LongueurFenetre, "Pause", "White",taille=int(0.0125*LargeurFenetre)) 
    
    # coordonnées du rectangle du bouton et texte de "quitter"
    ax_rect2=0.7625*LargeurFenetre
    ay_rect2=0.77*LongueurFenetre
    bx_rect2=0.825*LargeurFenetre
    by_rect2=0.82*LongueurFenetre
    rectangle(ax_rect2,ay_rect2, bx_rect2, by_rect2, remplissage="red")
    texte(0.76875*LargeurFenetre, 0.78*LongueurFenetre, "Quitter", "White",taille=int(0.0125*LargeurFenetre))
    mise_a_jour()
           
    # coordonnées du rectangle du bouton Taille boule
    if 2 in lst_fonction:
        ax_Tb=0.74375*LargeurFenetre
        ay_Tb=0.080*LongueurFenetre
        bx_Tb=0.84375*LargeurFenetre
        by_Tb=0.130*LongueurFenetre
        rectangle(ax_Tb, ay_Tb, bx_Tb, by_Tb, remplissage="skyblue")
        texte(0.79375*LargeurFenetre, 0.105*LongueurFenetre, "Taille Boule",taille=int(0.01125*LargeurFenetre), ancrage="center")


    

    if 4 in lst_fonction:
        # coordonnées du rectangle du bouton pour activer l'option terminaison
        ax_rect_terminaison = 0.74375*LargeurFenetre
        ay_rect_terminaison = 0.010*LongueurFenetre
        bx_rect_terminaison = 0.84375*LargeurFenetre
        by_rect_terminaison = 0.060*LongueurFenetre
        rectangle(ax_rect_terminaison, ay_rect_terminaison, bx_rect_terminaison,
                by_rect_terminaison, remplissage="skyblue", couleur="black")
        texte(0.79375*LargeurFenetre, 0.035*LongueurFenetre, "Terminaison", ancrage="center", taille=int(0.01125*LargeurFenetre)) 
        


    txt_tour_j2 = texte(0.75*LargeurFenetre, 0.02*LongueurFenetre, "Joueur "+col_j2, col_j2, taille=int(0.01375*LargeurFenetre)) # variable du texte du joueur 1          
    efface(txt_tour_j2) # efface le texte du joueur a qui est le tour pour laisser place au prochain
    txt_tour_j1 = texte(0.75*LargeurFenetre, 0.02*LongueurFenetre, "Joueur "+col_j1, col_j1, taille=int(0.01375*LargeurFenetre)) # variable du texte du joueur 2          
    efface(txt_tour_j1) # efface le texte du joueur a qui est le tour pour laisser place au prochain
        
    while com<2*nb_tour: # boucle principal du jeu

        tour_restant = texte(0.15*LargeurFenetre, 0.102*LongueurFenetre, int(2*nb_tour-com),  ancrage="center" , taille=int(0.01375*LargeurFenetre))
        if com%2==0:
            txt_tour_j1 = texte(0.15*LargeurFenetre, 0.030*LongueurFenetre, "Joueur 1", col_j1,  ancrage="center", taille=int(0.0125*LargeurFenetre))
        else:
            txt_tour_j2 = texte(0.15*LargeurFenetre, 0.03*LongueurFenetre, "Joueur 2", col_j2,  ancrage="center", taille=int(0.0125*LargeurFenetre))
        if 4 in lst_fonction and com2:
            rectangle(ax_rect_terminaison, ay_rect_terminaison
                    , bx_rect_terminaison, by_rect_terminaison
                    , remplissage="red", couleur="black")
            texte(0.79375*LargeurFenetre, 0.035*LongueurFenetre, "Enclenché", ancrage="center"
                , couleur="White", taille=int(0.01125*LargeurFenetre))
            
        if 1 in lst_fonction and 0 not in lst_fonction:
            x1, y1, type_clique = attente_clic_ou_touche() # prend les coordonnées du clique du joueur
            while type_clique == "Touche":
                scores(lst_j1, lst_j2, y1)
                
                x1, y1, type_clique = attente_clic_ou_touche()
                if type_clique == "ClicGauche":
                    break
        
        elif 0 in lst_fonction:
            chaine_time,sab=sablier(10, r,  ax_rect,  ay_rect,  bx_rect ,  by_rect,0)
            if chaine_time==0:
                if com%2==0:
                    efface(txt_tour_j1)
                else:
                    efface(txt_tour_j2)
                com+=1
                efface(tour_restant)
                continue
            else:
                x1,y1=coor_timer(chaine_time)
                if 4 in lst_fonction and com2==False:
                    # permet de voir si le bouton terminaison est déclanché
                    if inter_rect(0 ,x1, y1, ax_rect_terminaison, ay_rect_terminaison, bx_rect_terminaison, by_rect_terminaison) == True: 
                        rectangle(ax_rect_terminaison, ay_rect_terminaison
                                , bx_rect_terminaison, by_rect_terminaison
                                , remplissage="red", couleur="black")
                        texte(0.79375*LargeurFenetre, 0.035*LongueurFenetre, "Enclenché", ancrage="center"
                            , couleur="White", taille=int(0.01125*LargeurFenetre))
                        if com%2==0:
                            com=0
                            nb_tour=2.5
                        else:
                            com=1
                            nb_tour=3
                        chaine_time,sab=sablier(sab, r,  ax_rect,  ay_rect,  bx_rect ,  by_rect,1)
                        if chaine_time==0:
                            if com%2==0:
                                efface(txt_tour_j1)
                            else:
                                efface(txt_tour_j2)
                            com+=1
                            efface(tour_restant)
                            com2=True
                            continue
                        else:
                            x1,y1=coor_timer(chaine_time)
                        com2=True
                        
                if 2 in lst_fonction:
                        if inter_rect(0,x1,y1,ax_Tb,ay_Tb,bx_Tb,by_Tb)==True:
                            tarif=Affiche_TailleB(com, budget1, budget2, col_j1, col_j2,x1,y1)
                            r+=tarif
                            chaine_time,sab=sablier(sab, r,  ax_rect,  ay_rect,  bx_rect ,  by_rect,1)
                            if chaine_time==0:
                                if com%2==0:
                                    efface(txt_tour_j1)
                                else:
                                    efface(txt_tour_j2)
                                com+=1
                                efface(tour_restant)
                                continue
                            else:
                                x1,y1=coor_timer(chaine_time)
                                
        if 1 not in lst_fonction and 0 not in lst_fonction:
            x1, y1, type_clique = attente_clic()
        
        if inter_rect(0,x1,y1,ax_rect2,ay_rect2,bx_rect2,by_rect2)==True: # permet de voir si le bouton quitter est cliqué
            ferme_fenetre()
            
        if inter_rect(0,x1,y1,ax_pause,ay_pause,bx_pause,by_pause)==True:
            Sauvegarder()
        
        if 4 in lst_fonction and com2==False:
            # permet de voir si le bouton terminaison est déclanché
            if inter_rect(0 ,x1, y1, ax_rect_terminaison, ay_rect_terminaison, bx_rect_terminaison, by_rect_terminaison) == True: 
                rectangle(ax_rect_terminaison, ay_rect_terminaison
                        , bx_rect_terminaison, by_rect_terminaison
                        , remplissage="red", couleur="black")
                texte(0.79375*LargeurFenetre, 0.035*LongueurFenetre, "Enclenché", ancrage="center"
                    , couleur="White", taille=int(0.01125*LargeurFenetre))
                if com%2==0:
                    com=0
                    nb_tour=2.5
                else:
                    com=1
                    nb_tour=3
                com2=True
                
        if 2 in lst_fonction:
                if inter_rect(0,x1,y1,ax_Tb,ay_Tb,bx_Tb,by_Tb)==True:
                    tarif=Affiche_TailleB(com, budget1, budget2, col_j1, col_j2,x1,y1)
                    r+=tarif
                    x1, y1, type_clique = attente_clic()
     
        # si le joueur ne clique pas dans la zone de jeu il peut recliquer
        while inter_rect(r,x1,y1,ax_rect,ay_rect,bx_rect,by_rect)==False: 
            x1, y1, type_clique = attente_clic()
            
            if inter_rect(0,x1,y1,ax_rect2,ay_rect2,bx_rect2,by_rect2)==True: # permet de voir si le bouton quitter est cliqué
                ferme_fenetre()
                
            if 2 in lst_fonction: 
                if inter_rect(0,x1,y1,ax_Tb,bx_Tb,ay_Tb,by_Tb)==True:
                    tarif=Affiche_TailleB(com, budget1, budget2, col_j1, col_j2,x1,y1)
                    r+=tarif
                    x1, y1, type_clique = attente_clic()
                    
            if 4 in lst_fonction and com2==False:
                # permet de voir si le bouton terminaison est déclanché
                if inter_rect(0 ,x1, y1, ax_rect_terminaison, ay_rect_terminaison, bx_rect_terminaison, by_rect_terminaison) == True: 
                    rectangle(ax_rect_terminaison, ay_rect_terminaison
                            , bx_rect_terminaison, by_rect_terminaison
                            , remplissage="red", couleur="black")
                    texte(0.79375*LargeurFenetre, 0.035*LongueurFenetre, "Enclenché", ancrage="center"
                        , couleur="White", taille=int(0.01125*LargeurFenetre))
                    if com%2==0:
                        com=0
                        nb_tour=2.5
                    else:
                        com=1
                        nb_tour=3
                    com2=True
                    
        if com%2==0: # si compteur pair c'est au tour du joueur
            if 5 in lst_fonction: 
               if inter_obstacle(r,x1,y1,lst_cercle)==False:
                    com+=1
                    efface(txt_tour_j1)
                    efface(tour_restant)
                    continue
            # conditions qui vérifie si un cercle entre en intersection avec un autre cercle
            if inter_out(r,x1,y1,lst_j2)==True and inter_in(r,x1,y1,lst_j2)==False: 
                com+=1
                efface(txt_tour_j1)
                efface(tour_restant)
                continue

            # conditions qui vérifie si les coordonnées du clic sont contenus dans un cercle
            elif inter_in(r,x1,y1,lst_j2)==True: 
                remplace_boule(com,r,x1,y1,lst_j2,lst_com_j2, lst_score)
            else:
                boule=cercle(x1, y1, r, remplissage=col_j1)
                lst_j1.append([x1,y1,r])
                lst_com_j1.append(boule)
                lst_score=ajouter_score(lst_score, x1, y1, r, col_j1)
            budget1-=tarif
            
        else: # meme condition que ci-dessus mais pour le joueur deux 
            if 5 in lst_fonction:
                if inter_obstacle(r,x1,y1,lst_cercle)==False:
                     com+=1
                     efface(txt_tour_j2)
                     efface(tour_restant)
                     continue
            if inter_out(r,x1,y1,lst_j1)==True and inter_in(r,x1,y1,lst_j1)==False: 
                com+=1
                efface(txt_tour_j2)
                efface(tour_restant)
                continue 
            elif inter_in(r,x1,y1,lst_j1)==True:
                remplace_boule(com,r,x1,y1,lst_j1,lst_com_j1, lst_score)
            else:
                boule=cercle(x1, y1, r, remplissage=col_j2)
                lst_j2.append([x1,y1,r])
                lst_com_j2.append(boule)
                lst_score=ajouter_score(lst_score, x1, y1, r, col_j2)
            budget2-=tarif
        if 3 in lst_fonction:
                Version_dynamique(lst_j1,lst_com_j1,lst_j2,col_j1), Version_dynamique(lst_j2,lst_com_j2,lst_j1,col_j2)
        com+=1
        efface(tour_restant)
        efface(txt_tour_j1)
        efface(txt_tour_j2)
        tarif=0
        r=r2

    clic() # un clic pour passer au menu du gagnant
    liste_qui_gagne = func_somme_aire(lst_score, col_j1, col_j2, r, lst_j1, lst_j2) # permet de recolter les score des deux joueurs et la couleur du gagnant
    fenetre_de_fin(liste_qui_gagne, col_j1, col_j2) # affiche la fenetre de fin

attente_clic()
ferme_fenetre()
