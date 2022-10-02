# made by ø
# this code work now

import tkinter
import fonction


def game(LONG: int, NB_BOMB: int,L=500,l=500):

    # set up the game

    grille = [[0 for i in range(LONG)] for i in range(LONG)]
    discovered = [[0 for j in range(LONG)] for i in range(LONG)]

    # create the windows

    root = tkinter.Tk()
    root.geometry(f"{L}x{l}+300+250")
    root.title("Démineur")
    root.iconbitmap('img/game_icon.ico')
    root.configure(bg='#bdbdbd')

    for i in range(LONG):
        grille[0][i] = 100
        grille[LONG-1][i] = 100
        grille[i][0] = 100
        grille[i][LONG-1] = 100
        discovered[0][i] = 100
        discovered[LONG-1][i] = 100
        discovered[i][0] = 100
        discovered[i][LONG-1] = 100

    # place the bomb and put the right number around them

    grille = fonction.bomb(NB_BOMB, grille)
    grille = fonction.number_fill(LONG, grille)

    # This function is here only for debug

    def dim(event):
        print("*********Size of the window*********")
        print("width :", root.winfo_width())
        print("height :", root.winfo_height())
        print("******Coordinate of the window******")
        print("x :", root.winfo_x())
        print("y :", root.winfo_y())
        print("------------------------------------")

    # this function is for cascading discovery of the boxes (not finish (because not working properly))

    def discovery(coord: tuple):
        x,y = coord[0], coord[1]
        if not ((0 < x < len(grille)) and (0 < y < len(grille))):
            return
        for i in [-1, 0, 1]:
            for j in [-1, 1]:
                if (0 <= grille[x+j][y+i] < 9) and (discovered[x+j][y+i] == 0):
                    button[(x+j, y+i)].grid_forget()
                    discovered[x+j][y+i] = 1
                    if grille[x+j][y+i] == 0:
                        discovery((x+j, y+i))
        for i in [-1, 1]:
            if (0 <= grille[x][y+i] < 9) and (discovered[x][y+i] == 0):
                button[(x, y+i)].grid_forget()
                discovered[x][y+i] = 1
                if grille[x][y+i] == 0:
                    discovery((x, y+i))

    # check if the player win

    def win():
        x = 0
        for i in range(LONG):
            if 0 not in discovered[i]:
                x += 1
        if x == LONG:
            print('Tu as win')

    # check if the player loose

    def loose(coord: tuple):
        if grille[coord[0]][coord[1]] == 9:
            for i in range(LONG):
                for j in range(LONG):
                    if grille[i][j] == 9:
                        button[(i, j)].grid_forget()
            print('Tu as perdu')

    # this function is executed every time the player click

    def user_click(coord: tuple):
        if grille[coord[0]][coord[1]] > 10:
            return
        button[coord].grid_forget()

        if grille[coord[0]][coord[1]] == 0:
            discovery(coord)
        else:
            discovered[coord[0]][coord[1]] = 1

        loose(coord)
        win()

    # this function are going to be for the flap, but it needs to be implemented

    def put_flag(event, coord: tuple):
        button[coord].grid_forget()
        button[coord].grid(row=coord[0]+1, column=coord[1])
        button[coord].config(image=img[10])

    def replay():
        root.destroy()
        game_settings()

    # loading the image for the game

    img = {}
    for i in range(13):
        img[i] = tkinter.PhotoImage(file=f"img/{i}.png")

    # create the 2 layers of widget for the game

    game_frame = tkinter.Frame(root, bd=2, bg='#606060')
    game_frame.grid(row=1, column=0, padx=30)

    counter_frame = tkinter.Frame(root, bg='#bdbdbd')
    counter_frame.grid(row=0, column=0, pady=5)

    answer = {}
    for i in range(1, LONG-1):
        for j in range(1, LONG-1):
            if grille[i][j] == 9:
                discovered[i][j] = 5
            answer[(i, j)] = tkinter.Label(game_frame, image=img[grille[i][j]], bg="#C0ADAC")
            answer[(i, j)].grid(row=i+1, column=j, ipadx=3, ipady=3, sticky="w")

    button = {}
    for i in range(1, LONG-1):
        for j in range(1, LONG-1):
            button[(i, j)] = tkinter.Button(game_frame, bg="#606060", command=lambda x=(i, j): user_click(x))
            button[(i, j)].grid(row=i+1, column=j, ipadx=7)
            button[(i, j)].bind("<Button-3>", lambda e, x=(i, j): put_flag(e, x))
            button[(i, j)].bind("<Button-2>", dim)

    bomb_r = tkinter.Label(counter_frame, text=LONG, bg='#bdbdbd', font=("Minecraft", 20, "bold"))
    bomb_r.grid(row=0, column=0, padx=25, ipadx=25)

    # this button doesn't work

    restart = tkinter.Button(counter_frame, image=img[12], bg='#bdbdbd', command=replay)
    restart.grid(row=0, column=1, padx=25)

    # render the windows

    root.mainloop()


def game_settings():
    settings = [841,500]

    main = tkinter.Tk()
    main.geometry("500x200+300+50")
    main.title(" "*56+"Setting for the Game")
    main.iconbitmap('img/setting_icon.ico')


    def play():
        settings.append(int(len_grid.get()))
        if (int(number_bomb.get())) > (int(len_grid.get()**2)):
            print(int(len_grid.get()**2))
            settings.append(int(len_grid.get()**2))
        else:
            settings.append(int(number_bomb.get()))
        main.destroy()

    def debutant_play():
        settings[0] = 247
        settings[1] = 257
        settings.append(7)
        settings.append(10)
        main.destroy()

    def intermediaire_play():
        settings[0] = 479
        settings[1] = 489
        settings.append(16)
        settings.append(40)
        main.destroy()

    def expert_play():
        settings[0] = 634
        settings[1] = 644
        settings.append(22)
        settings.append(99)
        main.destroy()

    default = tkinter.Label(main, text='The default settings :', font=("Minecraft", 11))
    debutant = tkinter.Button(main, text='Debutant', font=("Minecraft", 11), command=debutant_play)
    intermediaire = tkinter.Button(main, text='Intermediaire', font=("Minecraft", 11), command=intermediaire_play)
    expert = tkinter.Button(main, text='Expert', font=("Minecraft", 11), command=expert_play)

    dorc = tkinter.Label(main, text='Or\nCustome\nThe\nSettings', font=("Minecraft"))

    len_grid = tkinter.Scale(main, from_=30, to=0, orient=tkinter.VERTICAL)
    number_bomb = tkinter.Scale(main, from_=69, to=0, orient=tkinter.VERTICAL)
    text_grid = tkinter.Label(main, text="  Longer of the  \ngrid", font=("Minecraft", 10))
    text_bomb = tkinter.Label(main, text="Number of\nbomb", font=("Minecraft", 10))
    launch = tkinter.Button(main, text='Launch\nthe game !', font=("Minecraft", 10), command=play)

    default.place(x=25, y=20)
    debutant.place(x=25, y=50)
    intermediaire.place(x=25, y=80)
    expert.place(x=25, y=110)

    dorc.place(x=200, y=50)

    len_grid.place(x=325)
    text_grid.place(x=325-15, y=105)
    number_bomb.place(x=325+100)
    text_bomb.place(x=325+100-5, y=105)
    launch.place(x=370, y=150)

    main.mainloop()

    game(settings[2]+2, settings[3], settings[0], settings[1])


game_settings()
