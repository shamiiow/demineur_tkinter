# made by Matéo et Florian
# this code work now
# Install Minecraft font for better experience ("https://fontmeme.com/polices/police-minecraft/")

import tkinter
import fonction
import os
from tkinter import ttk


def game(long: int, nb_bomb: int, fast_disco: bool, pack_texture, size_x=500, size_y=500) -> None:

    # set up the game // met en place les les grille pour le jeu

    grid = [[0 for j in range(long)] for i in range(long)]
    discovered = [[0 for j in range(long)] for i in range(long)]
    flag = [[0 for j in range(long)] for i in range(long)]
    first_click = True

    # create the windows // crée la fenetre de jeu

    root = tkinter.Tk()
    root.geometry(f"{size_x}x{size_y}+300+50")
    root.title("Minesweeper")
    root.iconbitmap('img/game_icon.ico')
    root.configure(bg='#bdbdbd')

    # create border of number around all the grid // crée une bordure de nombre autour des grilles

    for i in range(long):
        # autour de la grille de bombe
        grid[0][i], grid[long - 1][i], grid[i][0], grid[i][long - 1] = 100, 100, 100, 100
        # autour de la grille des case découverte
        discovered[0][i], discovered[long - 1][i], discovered[i][0], discovered[i][long - 1] = 100, 100, 100, 100
        # autour de la grille des drapeau
        flag[0][i], flag[long - 1][i], flag[i][0], flag[i][long - 1] = 100, 100, 100, 100

    # place the bomb and put the right number around them // met en place les bombe et met les bon nombre autour

    def set_up(coord: tuple) -> None:
        nonlocal grid
        grid = fonction.bomb(nb_bomb, grid, coord)
        grid = fonction.number_fill(long, grid)
        # met les bonnes images au chiffres et bombes associé
        for i in range(1, long - 1):
            for j in range(1, long - 1):
                answer[(i, j)].config(image=img[grid[i][j]])

    # This function is here only for debug // uniquement pour debogage

    def debug() -> None:
        print('-'*50)
        for i in range(1, long - 1):
            print(grid[i], '--', discovered[i], '--', flag[i])

    # permet de savoir les dimensions et la position de la fenetre dans l'écran (utile pour faire une belle fenetre)

    def dim(event) -> None:
        print("*********Size of the window*********")
        print("width :", root.winfo_width())
        print("height :", root.winfo_height())
        print("******Coordinate of the window******")
        print("x :", root.winfo_x())
        print("y :", root.winfo_y())
        print("------------------------------------")

    # this function is for cascading discovery of the boxes // fonction de découverte des cases ( en réccurtion )

    def discovery(coord: tuple) -> None:
        x, y = coord[0], coord[1]
        # evite les erreur d'index
        if not ((0 < x < len(grid)) and (0 < y < len(grid))):
            return
        # si la case est un drapeau ça ne la découvre pas au niveau du clique
        if flag[coord[0]][coord[1]] == 1:
            return
        # regarde les 8 cases autour
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                # si la case est vide ou est un nombre et qu'il n'y a pas de drapeau, ça la découvre
                if (0 <= grid[x+j][y+i] < 9) and (discovered[x+j][y+i] == 0) and (flag[x+j][y+i] == 0):
                    button[(x+j, y+i)].grid_forget()
                    discovered[x+j][y+i] = 1
                    # si la case est vide alors ça redécouvre les case autour de manière recursive
                    if grid[x+j][y+i] == 0:
                        discovery((x+j, y+i))

    # check if the player win // permet de savoir si le joueur a gagné

    def win() -> None:
        x = 0
        # compte le nombre de case ayant aucun nombre 0 (le nombre de cases non decouvertes)
        for i in range(long):
            if 0 not in discovered[i]:
                x += 1
        # si toutes les lignes sont découvertes alors le joueur a win
        if x == long:
            restart.config(image=img[13])
            # change le widget de win or loose en "win"
            wol.config(text='win')

    # check if the player loose // permet de savoir si le joueur a perdu

    def loose(coord: tuple) -> None:
        # si la case n'est pas une bombe le joueur n'a pas perdu
        if grid[coord[0]][coord[1]] != 9:
            return
        # met une image customisée pour la bombe qui a fait perdre le joueur
        answer[coord].config(image=img[14])
        # parcour toute la grille et découvre toutes les bombes
        for i in range(long):
            for j in range(long):
                if grid[i][j] == 9 and flag[i][j] != 1:
                    button[(i, j)].grid_forget()
                # si le joueur a mis un drapeau la où il y avait pas de bombe, une image customisée s'affiche
                if grid[i][j] != 9 and flag[i][j] == 1:
                    button[(i, j)].grid_forget()
                    answer[(i, j)].config(image=img[15])
        # met l'image de loose sur le smiley
        restart.config(image=img[12])
        # change le widget de win or loose en "loose"
        wol.config(text='loose')

    # this function is executed every time the player click // cette fonction s'exécute a chaque fois que le joueur clique

    def user_click(coord: tuple) -> None:
        #
        nonlocal first_click
        # si le joueur a perdu ou gagné il ne peut pas jouer
        if wol.cget("text") != '':
            return
        # si il clique sur un drapeau, rien ne se passe
        if flag[coord[0]][coord[1]] == 1:
            return
        # permet de ne pas découvrire en cascade les bordure créé dans la ligne 29
        if grid[coord[0]][coord[1]] > 10:
            return
        # si c'est le premier clique du joueur, ça exécute la fonction set_up
        if first_click:
            first_click = False
            set_up(coord)
        # découvre la case cliquée
        button[coord].grid_forget()
        if grid[coord[0]][coord[1]] == 0:
            # découvre les 8 case autour de celle cliquée
            discovered[coord[0]][coord[1]] = 1
            discovery(coord)
            # met a jour la découverte des cases

        else:
            # met a jour la découverte des cases
            discovered[coord[0]][coord[1]] = 1
        win()       # check win
        loose(coord)        # check loose

    # this function are going to be for the flag, but it needs to be implemented

    def put_flag(event, coord: tuple) -> None:
        # si le joueur a gagné il ne peut plus mettre de drapeau
        if wol.cget("text") != '':
            return
        # si il n'y avait pas de drapeau à la case cliquée
        if flag[coord[0]][coord[1]] == 0:
            flag[coord[0]][coord[1]] = 1        # changer la valeur dans la liste
            button[coord].grid_forget()
            button[coord].grid(row=coord[0]+1, column=coord[1])         # grid la nouvelle case sans le paramettre padx
            button[coord].config(image=img[10])         # change l'image
            bomb_r.config(text=bomb_r.cget('text')-1)       # retire 1 au compteur de bombe
        # si il y avait déjà un drapeau à la case cliquée
        # faire le procécusse inverse
        elif flag[coord[0]][coord[1]] == 1:
            flag[coord[0]][coord[1]] = 0        # changer la valeure dans le liste
            button[coord].grid_forget()
            button[coord].grid(row=coord[0]+1, column=coord[1], ipadx=7)    # grid la nouvelle case
            button[coord].config(image='')              # rechanger l'image
            bomb_r.config(text=bomb_r.cget('text')+1)       # ajoute 1 au compteur de bombes

    # fonction permettant de rejouer

    def replay() -> None:
        root.destroy()       # ferme la fenêtre de jeu
        game_settings()      # ouvre la fenêtre de paramètres

    # change l'image quand un bouton est entrain d'être pressé

    def press(event) -> None:
        if wol.cget("text") == "loose" or wol.cget("text") == "win":
            return
        restart.config(image=img[17])

    # change l'image quand un bouton est relaché

    def release(event) -> None:
        if wol.cget("text") == "loose" or wol.cget("text") == "win":
            return
        restart.config(image=img[11])

    def speed_finder(coord):
        x, y = coord[0], coord[1]
        # si il y a un drapeau ça ne le découvre pas
        if flag[coord[0]][coord[1]] == 1:
            return
        # pacoure les 6 case au dessus et en bas
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if flag[x+j][y+i] == 0:      # si il n'y a pas de drapeau
                    button[(x + j, y + i)].grid_forget()    # découvrir la case
                    discovered[x + j][y + i] = 1        # mise a jour de la grille
                    if grid[x + j][y + i] == 9:     # si la case étais un bombe
                        loose((x + j, y + i))       # faire perdre
                    if grid[x + j][y + i] == 0:     # si c'étais vide
                        discovery((x + j, y + i))      # faire la découverte de case normal
        # parcour les 2 cases à coté et fait la même chose qu'au dessus

    def speed_check(e, coord):
        nb_flag = 0     # compteur du nombre de drapeau
        x, y = coord[0], coord[1]
        if not ((0 < x < len(grid)) and (0 < y < len(grid))):       # empeche les erreur d'index
            return
        # parcour les 8 case et ajoute 1 a chaque drapeau trouver
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if flag[x + j][y + i] == 1:
                    nb_flag += 1
        # si le nombre de drapeau est correct alors il execute la fonction de speed finder
        if nb_flag == grid[x][y]:
            speed_finder(coord)

    # loading the image for the game // charge les images pour le jeu

    img = {}
    for i in range(18):
        img[i] = tkinter.PhotoImage(file=f"img/{pack_texture}/{i}.png")

    # create the 2 frame of widget for the game     // crée 2 cadre d'objet pour le jeu

    game_frame = tkinter.Frame(root, bd=2, bg='#606060')
    game_frame.grid(row=1, column=0, padx=30)

    counter_frame = tkinter.Frame(root, bg='#bdbdbd')
    counter_frame.grid(row=0, column=0, pady=5)

    # create the grid for the answer and grid it   // crée la grille pour les réponse et l'affiche


    answer = {}
    for i in range(1, long - 1):
        for j in range(1, long - 1):
            if grid[i][j] == 9:
                discovered[i][j] = 5
            answer[(i, j)] = tkinter.Button(game_frame, image=img[0], bg="#C0ADAC")
            answer[(i, j)].grid(row=i+1, column=j, ipadx=3, ipady=3)
            if fast_disco:
                answer[(i, j)].bind("<Button-1>", lambda e, x=(i, j): speed_check(e, x))

    # create the buttons to hide the grid answer and grid it // crée les bouton cliquable par les joueur pour

    button = {}
    for i in range(1, long - 1):
        for j in range(1, long - 1):
            button[(i, j)] = tkinter.Button(game_frame,image=img[0], bg="#606060", command=lambda x=(i, j): user_click(x))
            button[(i, j)].grid(row=i+1, column=j, ipadx=3, ipady=3)        #7
            button[(i, j)].bind("<Button-3>", lambda e, x=(i, j): put_flag(e, x))
            button[(i, j)].bind("<Button-2>", dim)
            button[(i, j)].bind("<ButtonPress-1>", press)
            button[(i, j)].bind("<ButtonRelease-1>", release)

    # show the number of bomb it last // montre le nombre de bombes qu'il reste

    bomb_r = tkinter.Label(counter_frame, text=nb_bomb, bg='#bdbdbd', font=("Minecraft", 20, "bold"))
    bomb_r.grid(row=0, column=0)

    # this is for restart the game // sert à redémarrer le jeu ( ce sont les smiley )

    restart = tkinter.Button(counter_frame, image=img[11], bg='#bdbdbd', command=replay)
    restart.grid(row=0, column=1, padx=50)

    wol = tkinter.Label(root, text='')

    # to exit the game (improve the img) // sert à fermer le jeu sans le relancer

    exit = tkinter.Button(counter_frame, image=img[16], bg='#bdbdbd', command=root.destroy)
    exit.grid(row=0, column=2)

    debug()
    # render the windows // fait l'affichage de la fenêtre

    root.mainloop()


def game_settings() -> None:

    # default settings for the size of the window // taille de la fenêtre

    settings = [904, 929, False]

    # create the windows and some settings // crée le fen^tre de paramêtre

    main = tkinter.Tk()
    main.geometry("504x504+300+50")
    main.title(" "*56+"Setting for the Game")
    main.iconbitmap('img/setting_icon.ico')
    bg = tkinter.PhotoImage(file="img/background.png")
    tkinter.Label(main, image=bg).place(x=0, y=0)

    # add the customs settings and launch the game // si ce n'est pas une difficulté préfaite cette fonction prend les paramêtre personnalisés

    def play():
        settings.append(int(len_grid.get()))
        if (int(number_bomb.get())) > (int(len_grid.get()**2)):

            settings.append(int(len_grid.get()**2)-9)
        else:
            settings.append(int(number_bomb.get()))

        main.destroy()

    # set default settings and launch the game // niveau préfait ( facile )

    def easy():
        settings[0] = 256
        settings[1] = 269
        settings.append(7)
        settings.append(10)

        main.destroy()

    # set default settings and launch the game // niveau préfait ( moyen )

    def normal():
        settings[0] = 513
        settings[1] = 531
        settings.append(16)
        settings.append(40)
        main.destroy()

    # set default settings and launch the game // niveau préfait ( difficile )

    def hard():
        settings[0] = 684
        settings[1] = 702
        settings.append(22)
        settings.append(99)
        main.destroy()

    def speed_onoff():
        settings[2] = not settings[2]    # active ou non le jeu rapide

    # create all the widget I need // crée tous les objects nécessaire à la fen^tre de paramtre

    easy = tkinter.Button(main, text='Easy', font=("Minecraft", 11), command=easy)
    normal = tkinter.Button(main, text='Normal', font=("Minecraft", 11), command=normal)
    hard = tkinter.Button(main, text='Hard', font=("Minecraft", 11), command=hard)

    l_texture = ["original", "floriant", "minecraft", "32x32"]
    s_texture = "original"

    def action(event):
        nonlocal s_texture
        s_texture = texture.get()

    texture = ttk.Combobox(main, values=l_texture)
    texture.bind("<<ComboboxSelected>>", action)
    texture.current(0)

    len_grid = tkinter.Scale(main, from_=30, to=0, orient=tkinter.VERTICAL)
    number_bomb = tkinter.Scale(main, from_=150, to=0, orient=tkinter.VERTICAL)

    launch = tkinter.Button(main, text='    Launch    \nthe game !', font=("Minecraft", 10), command=play)
    fast = tkinter.Checkbutton(main, font=("Minecraft", 11), variable=settings[2], command=speed_onoff, bg="black")

    bye = tkinter.Button(main, text="\n  Exit  \n", font=("Minecraft", 10), command=main.destroy)

    # place all the widget (I know place method is not the best) // place tous les objets ( même si c'est pas optimisé avec cette méthode )

    easy.place(x=50, y=90)
    normal.place(x=50, y=130)
    hard.place(x=50, y=170)

    texture.place(x=50, y=325)

    len_grid.place(x=310, y=75)
    number_bomb.place(x=420, y=75)

    launch.place(x=340, y=262)
    fast.place(x=420, y=445)

    bye.place(x=275, y=425)
    # render the windows // affiche la fenêtre

    main.mainloop()

    # after the windows is kill, the game launch // ferme le fenêtre et lance le jeu après ça ( il y a donc plusieurs moyen de fermer la fenêtre et le jeu s'ouvre seulement si les paramêtres sont fermés )

    try:
        game(settings[3]+2, settings[4], settings[2], s_texture, settings[0], settings[1])
    except IndexError:
        print("Bye")


game_settings()
