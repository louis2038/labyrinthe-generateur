import pygame
import random
import time


pygame.init()

blue_color = (0,0,255)
boucle = True

red_color = (255,0,0)

size = (900,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("labyrinthe")




def menu():
    boucle_menu = True
    black_color = (0,0,0)
    blue_color = (0,0,255)
    taille = 0
    entre = False
    while boucle_menu:

        screen.fill(black_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle_menu = False
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if taille != 0:
                        return taille
                        boucle_menu = True
                elif event.key == pygame.K_UP:
                    taille = taille + 2
                elif event.key == pygame.K_DOWN:
                    if taille != 0:
                        taille = taille - 2


        arial = pygame.font.SysFont("arial", 20, True)

        text_presentation = arial.render("fléche du haut -> +2", True, blue_color)
        screen.blit(text_presentation, [400, 450])
        text_presentation = arial.render("fléche du bas  -> -2", True, blue_color)
        screen.blit(text_presentation, [400, 475])
        text_presentation = arial.render("SPACE pour commencer", True, blue_color)
        screen.blit(text_presentation, [400, 500])
        arial = pygame.font.SysFont("arial", 50, True)
        text_taille = arial.render("taille du labyrinthe {} * {}".format(taille, taille), True, blue_color)
        screen.blit(text_taille, [300,350])



        pygame.display.flip()




def generation():


    grille = []
    wall_vertical = []
    wall_horizontal = []

    dimension = menu()




    liste_temp = []


    for ii in range(0,int(dimension +1),1):
        liste_temp = []
        for tt in range(0,int(dimension),1):
            if ii == 0:
                liste_temp.append(3)
            elif ii == (dimension):
                liste_temp.append(3)
            else:
                liste_temp.append(1)
        wall_horizontal.append(liste_temp)


    liste_temp = []

    for ii in range(0,int(dimension +1),1):
        liste_temp = []
        for tt in range(0,int(dimension),1):
            if ii == 0:
                liste_temp.append(3)
            elif ii == (dimension):
                liste_temp.append(3)
            else:
                liste_temp.append(1)
        wall_vertical.append(liste_temp)



    liste_temp = []

    for ii in range(0,int(dimension),1):
        liste_temp = []
        for tt in range(0,int(dimension),1):
                liste_temp.append(0)
        grille.append(liste_temp)





    screen = pygame.display.set_mode((600,600), pygame.RESIZABLE)
    pygame.display.set_caption("labirinth")




    print(wall_horizontal)
    print(wall_vertical)
    print(grille)
    """
    (haut, bas, gauche , droite)
    """
    deplacement = [False,False,False,False]




    boucle_generation = True

    pos_D = (0,0)
    passe = True
    while boucle_generation:


        print(pos_D)
        grille[pos_D[0]][pos_D[1]] = 1

        nbs_random = 0


        if wall_horizontal[pos_D[0]][pos_D[1]] == 3:
            print("haut = 3")
            deplacement[0] = True
        else:
            if grille[pos_D[0] -1][pos_D[1]] == 1:
                deplacement[0] = True
                print("futur deplacement haut = 1")


        if wall_horizontal[pos_D[0]+1][pos_D[1]] == 3:
            print("bas = 3")
            deplacement[1] = True
        else:
            if grille[pos_D[0] +1][pos_D[1]] == 1:
                deplacement[1] = True
                print("futur deplacement bas = 1")

        if wall_vertical[pos_D[1]][pos_D[0]] == 3:
            print("gauche = 3")
            deplacement[2] = True
        else:
            if grille[pos_D[0]][pos_D[1] -1] == 1:
                deplacement[2] = True
                print("futur deplacement gauche = 1")

        if wall_vertical[pos_D[1]+1][pos_D[0]] == 3:
            print("droite = 3")
            deplacement[3] = True
        else:
            if grille[pos_D[0]][pos_D[1] +1] == 1:
                deplacement[3] = True
                print("futur deplacement droite = 1")


        if (deplacement[0] == True) and (deplacement[1] == True) and (deplacement[2] == True) and (deplacement[3] == True):
            print("deplacement impossible")
            fini = False
            for tt in range(0, dimension, 1):
                for ii in range(0, dimension, 1):
                    print("cherche")
                    if grille[tt][ii] == 0 and fini == False:
                        pos_D = (tt, ii)
                        print("curseur")
                        fini = True
                        grille[tt][ii] = 1
                        print(grille)
                        print(pos_D)
                        if pos_D[1] == 0:
                            wall_horizontal[pos_D[0]][pos_D[1]] = 0
                        else:
                            wall_vertical[pos_D[1]][pos_D[0]] = 0


            ok = False
            passe = False
        else:
            ok = True
            passe = True

        if passe == True:
            while ok:
                orientaion = [0,0,0,0]
                nbs_random = random.randint(1,4)
                if nbs_random == 1:
                    if deplacement[0] == False:
                        pos_A = (pos_D[0] -1,pos_D[1])
                        ok = False
                        orientaion[0] = 1

                if nbs_random == 2:
                    if deplacement[1] == False:
                        pos_A = (pos_D[0] +1,pos_D[1])
                        ok = False
                        orientaion[1] = 1
                        """
                        horizontal
                        """

                if nbs_random == 3:
                    if deplacement[2] == False:
                        pos_A = (pos_D[0],pos_D[1] -1)
                        ok = False
                        orientaion[2] = 1

                if nbs_random == 4:
                    if deplacement[3] == False:
                        pos_A = (pos_D[0],pos_D[1] +1)
                        ok = False
                        orientaion[3] = 1
                print("ok")

            if orientaion[0] == 1:
                wall_horizontal[pos_D[0]][pos_D[1]] = 0
                pos_D = pos_A

            if orientaion[1] == 1:
                wall_horizontal[pos_D[0] + 1][pos_D[1]] = 0
                pos_D = pos_A

            if orientaion[2] == 1:
                wall_vertical[pos_D[1]][pos_D[0]] = 0
                pos_D = pos_A

            if orientaion[3] == 1:
                wall_vertical[pos_D[1] + 1][pos_D[0]] = 0
                pos_D = pos_A


        orientaion = [0,0,0,0]
        print(grille)
        print(wall_horizontal)
        print(wall_vertical)
        deplacement = [False, False, False, False]
        prout = False
        for uu in range(0,dimension,1):
            for gg in range(0, dimension,1):
                if grille[uu][gg] == 0:
                    prout = True

        if prout == False:
            print("finit")
            boucle_generation = False




    print("dessin")
    print(dimension)
    print(wall_horizontal)
    print(wall_vertical)
    return dimension,grille,wall_horizontal,wall_vertical






