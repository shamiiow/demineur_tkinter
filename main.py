# made by ø
# this code is not fuck dup anymore

import tkinter
import fonction


def game(LONG: int, NB_BOMB: int):

    # set up the game

    grille = [[0 for i in range(LONG)] for i in range(LONG)]
    discovered = [[0 for j in range(LONG)] for i in range(LONG)]

    # create the windows

    root = tkinter.Tk()
    root.geometry(f"500x500")

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

    # this function is for cascading discovery of the boxes (not finish (because not working properly))

    def discovery(coord: tuple):
        x = coord[0]
        y = coord[1]
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

    def put_flag(event, x: int):
        print(x)

    # loading the image for the game

    img = {}
    for i in range(11):
        img[i] = tkinter.PhotoImage(file=f"img/{i}.png")

    # create the 2 layers of widget for the game

    game_frame = tkinter.Frame(root, bd=2, bg='red')
    game_frame.grid(row=1, column=0)

    counter_frame = tkinter.Frame(root, bd=2, bg='blue')
    counter_frame.grid(row=0, column=0)

    answer = {}
    for i in range(1, LONG-1):
        for j in range(1, LONG-1):
            if grille[i][j] == 9:
                discovered[i][j] = 5
            answer[(i, j)] = tkinter.Label(game_frame, image=img[grille[i][j]])
            answer[(i, j)].grid(row=i+1, column=j, ipadx=3, ipady=3, sticky="w")

    button = {}
    for i in range(1, LONG-1):
        for j in range(1, LONG-1):
            button[(i, j)] = tkinter.Button(game_frame, command=lambda x=(i, j): user_click(x))
            button[(i, j)].grid(row=i+1, column=j, ipadx=7)
            button[(i, j)].bind("<Button-3>", lambda e, x=(i, j): put_flag(e, x))

    bomb_r = tkinter.Label(counter_frame, text=LONG, font=("Minecraft", 20, "bold"))
    bomb_r.grid(row=0, column=0)

    # this button doesn't work

    restart = tkinter.Button(counter_frame, text='Restart', command=game)
    restart.grid(row=0, column=1)

    # render the windows

    root.mainloop()


settings = []

main = tkinter.Tk()
main.geometry("500x200")


def play():
    settings.append(int(len_grid.get()))
    if (int(number_bomb.get())) > (int(len_grid.get()**2)):
        print(int(len_grid.get()**2))
        settings.append(len_grid.get() ** 2)
    else:
        settings.append(int(number_bomb.get()))
    main.destroy()


len_grid = tkinter.Scale(main, from_=30, to=0, orient=tkinter.VERTICAL)
number_bomb = tkinter.Scale(main, from_=69, to=0, orient=tkinter.VERTICAL)
text_grid = tkinter.Label(main, text="  Longer of the  \ngrid")
text_bomb = tkinter.Label(main, text="Number of\nbomb")
launch = tkinter.Button(main, text='Launch\nthe game !', command=play)

len_grid.place(x=175)
text_grid.place(x=175-15, y=105)
number_bomb.place(x=175+100)
text_bomb.place(x=175+100-5, y=105)
launch.place(x=220, y=150)

main.mainloop()

game(settings[0]+2, settings[1])
