import pygame
from principale import generation
import time



def jeu():
    pygame.init()

    liste = generation()
    print("passage autre fichier")
    dimension = liste[0]
    grille = liste[1]
    wall_horizontal = liste[2]
    wall_vertical = liste[3]
    print(wall_vertical)
    print(wall_horizontal)
    print(grille)

    red_color = (255,0,0)

    size = (900, 700)
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("labirinth")

    clock = pygame.time.Clock()



    persso_0 = pygame.image.load("persso_0.png")
    persso_1 = pygame.image.load("persso_1.png")
    persso_2 = pygame.image.load("persso_2.png")
    persso_0 = pygame.transform.scale(persso_0, size)
    persso_1 = pygame.transform.scale(persso_1, size)
    persso_2 = pygame.transform.scale(persso_2, size)

    persso_0_90 = pygame.transform.rotate(persso_0, 90)

    pos_rot = 70

    red_color = [255,0,0]
    black_color = [0,0,0]
    brown_color = [161,110,28]



    time_animation = 200

    boucle = True
    temps_1 = pygame.time.get_ticks()
    temps_2 = pygame.time.get_ticks()
    temps_3 = pygame.time.get_ticks()
    persso_disp = persso_0

    persso_x = 0
    persso_y = 0
    rotation = 1
    animation_plateau = False
    dem_x_ch = 0
    dem_y_ch = 0
    nbs_pas = 0
    pas_anim = 0
    dem_x = 0
    dem_y = 0
    pos_D = [0,0]
    go_animation = False
    while boucle:
        screen.fill(black_color)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle = False
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if animation_plateau == False:
                        if (wall_vertical[pos_D[1]][pos_D[0]] == 3) or (wall_vertical[pos_D[1]][pos_D[0]] == 1):
                            print("mur !")
                        else:
                            animation_dir = 1
                            animation_plateau = True
                            go_animation = True
                            temps_1 = pygame.time.get_ticks()
                            temps_2 = pygame.time.get_ticks() + (time_animation / 4)
                            temps_3 = pygame.time.get_ticks() + (time_animation / 2)
                            temps_4 = pygame.time.get_ticks() + ((time_animation / 4) * 3)
                            pos_D[1] = pos_D[1] - 1
                            print(pos_D)
                            rotation = 90
                            persso_x = 80
                            persso_y = -80

                elif event.key == pygame.K_UP:
                    if animation_plateau == False:
                        if (wall_horizontal[pos_D[0]][pos_D[1]] == 3) or (wall_horizontal[pos_D[0]][pos_D[1]] == 1):
                            print("mur !")
                        else:
                            animation_dir = 2
                            animation_plateau = True
                            go_animation = True
                            temps_1 = pygame.time.get_ticks()
                            temps_2 = pygame.time.get_ticks() + (time_animation / 4)
                            temps_3 = pygame.time.get_ticks() + (time_animation / 2)
                            temps_4 = pygame.time.get_ticks() + ((time_animation / 4) * 3)
                            pos_D[0] = pos_D[0] - 1
                            print(pos_D)
                            rotation = 0
                            persso_x = 0
                            persso_y = 0

                elif event.key == pygame.K_DOWN:
                    if animation_plateau == False:
                        if (wall_horizontal[pos_D[0]+1][pos_D[1]] == 3) or (wall_horizontal[pos_D[0]+1][pos_D[1]] == 1):
                            print("mur !")
                        else:
                            animation_dir = 3
                            animation_plateau = True
                            go_animation = True
                            temps_1 = pygame.time.get_ticks()
                            temps_2 = pygame.time.get_ticks() + (time_animation / 4)
                            temps_3 = pygame.time.get_ticks() + (time_animation / 2)
                            temps_4 = pygame.time.get_ticks() + ((time_animation / 4) * 3)
                            pos_D[0] = pos_D[0] +1
                            print(pos_D)
                            rotation = 180
                            persso_x = 0
                            persso_y = 0

                elif event.key == pygame.K_RIGHT:
                    if animation_plateau == False:
                        if (wall_vertical[pos_D[1] + 1][pos_D[0]] == 3) or (wall_vertical[pos_D[1] + 1][pos_D[0]] == 1):
                            print("mur !")
                        else:
                            animation_dir = 4
                            animation_plateau = True
                            go_animation = True
                            temps_1 = pygame.time.get_ticks()
                            temps_2 = pygame.time.get_ticks() + (time_animation /4)
                            temps_3 = pygame.time.get_ticks() + (time_animation /2)
                            temps_4 = pygame.time.get_ticks() + ((time_animation /4) *3)
                            pos_D[1] = pos_D[1] + 1
                            print(pos_D)
                            rotation = 270
                            persso_x = 80
                            persso_y = -80





        if go_animation == True:
            if temps_1 <= pygame.time.get_ticks():
                persso_disp = pygame.transform.rotate(persso_1, rotation)
                temps_1 = pygame.time.get_ticks() + time_animation

            if temps_2 <= pygame.time.get_ticks():
                persso_disp = pygame.transform.rotate(persso_0, rotation)
                temps_2 = pygame.time.get_ticks() + time_animation

            if temps_3 <= pygame.time.get_ticks():
                persso_disp = pygame.transform.rotate(persso_2, rotation)
                temps_3 = pygame.time.get_ticks() + time_animation

            if temps_4 <= pygame.time.get_ticks():
                persso_disp = pygame.transform.rotate(persso_0, rotation)
                nbs_pas = nbs_pas +1
                temps_4 = pygame.time.get_ticks() + time_animation

            if nbs_pas == 2:
                go_animation = False
                nbs_pas = 0


        zoom = 300
        if animation_plateau == True:
            if animation_dir == 1:
                anim_D = -(zoom * dem_x_ch)
                dem_x = dem_x - (anim_D - 12.5)
                pas_anim = pas_anim + 1

            if animation_dir == 2:
                anim_D = -(zoom * dem_y_ch)
                dem_y = dem_y - (anim_D - 12.5)
                pas_anim = pas_anim + 1

            if animation_dir == 3:
                anim_D = -(zoom * dem_y_ch)
                dem_y = dem_y + (anim_D - 12.5)
                pas_anim = pas_anim + 1

            if animation_dir == 4:
                anim_D = -(zoom * dem_x_ch)
                dem_x = dem_x + (anim_D - 12.5)
                pas_anim = pas_anim + 1

            if pas_anim >= 24:
                animation_plateau = False
                pas_anim = 0

        for tt in range(0,dimension +1,1):
            for ii in range(0,dimension,1):
                if (wall_vertical[tt][ii] == 3) or (wall_vertical[tt][ii] == 1):
                    pygame.draw.line(screen, red_color,((tt+1)*zoom +dem_x, zoom *(ii + 1)-100 +dem_y) ,( (zoom*(tt+1)) +dem_x, zoom*(ii+1) + zoom -100 +dem_y), 10)

        for tt in range(0,dimension +1 ,1):
            for ii in range(0,dimension,1):
                if (wall_horizontal[tt][ii] == 3) or (wall_horizontal[tt][ii] == 1):
                    pygame.draw.line(screen, red_color,( (ii+1)*zoom +dem_x , zoom *(tt + 1)-100 +dem_y) ,( (zoom*(ii+1))+zoom +dem_x, zoom*(tt+1)-100 +dem_y), 10)




        if (pos_D[0] == dimension - 1) and (pos_D[1] == dimension -1):
            screen.fill(black_color)
            pygame.display.flip()
            boucle = False
            return  True

        recta = pygame.Rect(zoom+dem_x+(dimension*zoom) -290,zoom+dem_y+(dimension*zoom) -390,zoom-20,zoom-20)
        pygame.draw.rect(screen, brown_color, recta, 0)
        screen.blit(persso_disp, [persso_x,persso_y])

        clock.tick(60)
        pygame.display.flip()










tout = True
while tout:
    tout = jeu()