# made by ø
# this code is not fuck dup anymore

import tkinter
import fonction


def game():
    # create the windows

    root = tkinter.Tk()
    root.geometry("500x500")

    # create the constant and the game grid

    LONG = 10
    NB_BOMB = 2
    grille = [[0 for i in range(LONG)] for i in range(LONG)]
    discovered = [[0 for j in range(LONG)] for i in range(LONG)]

    for i in range(LONG):
        grille[0][i] = 100
        grille[LONG - 1][i] = 100
        grille[i][0] = 100
        grille[i][LONG - 1] = 100
        discovered[0][i] = 100
        discovered[LONG - 1][i] = 100
        discovered[i][0] = 100
        discovered[i][LONG - 1] = 100

    # place the bomb and put the right number around them

    grille = fonction.bomb(NB_BOMB, grille)
    grille = fonction.number_fill(LONG, grille)

    for i in range(LONG):
        for j in range(LONG):
            if grille[i][j] == 9:
                discovered[i][j] = 5
    for i in range(LONG):
        print(discovered[i])
    # this function is for cascading discovery of the boxes (not finish (because not working properly))

    def discovery(coord):
        if not (0 < coord[0] < len(grille) and 0 < coord[1] < len(grille)):
            return
        for i in range(3):
            if (0 <= grille[coord[0]-1][coord[1]-(1-i)] < 9) and (discovered[coord[0]-1][coord[1]-(1-i)] == 0):
                button[(coord[0]-1, coord[1]-(1-i))].grid_forget()
                discovered[coord[0]-1][coord[1]-(1-i)] = 1
                if grille[coord[0]-1][coord[1]-(1-i)] == 0:
                    discovery((coord[0]-1, coord[1]-(1-i)))
        for i in range(3):
            if (0 <= grille[coord[0]+1][coord[1]-(1-i)] < 9) and (discovered[coord[0]+1][coord[1]-(1-i)] == 0):
                button[(coord[0]+1, coord[1]-(1-i))].grid_forget()
                discovered[coord[0]+1][coord[1]-(1-i)] = 1
                if grille[coord[0]+1][coord[1]-(1-i)] == 0:
                    discovery((coord[0]+1, coord[1]-(1-i)))
        if (0 <= grille[coord[0]][coord[1]-1] < 9) and (discovered[coord[0]][coord[1]-1] == 0):
            button[(coord[0], coord[1]-1)].grid_forget()
            discovered[coord[0]][coord[1]-1] = 1
            if grille[coord[0]][coord[1]-1] == 0:
                discovery((coord[0], coord[1]-1))
        if (0 <= grille[coord[0]][coord[1]+1] < 9) and (discovered[coord[0]][coord[1]+1] == 0):
            button[(coord[0], coord[1]+1)].grid_forget()
            discovered[coord[0]][coord[1]+1] = 1
            if grille[coord[0]][coord[1]+1] == 0:
                discovery((coord[0], coord[1]+1))

    # this function is executed every time the player click

    def user_click(coord):
        x = 0
        if result.cget('text') != '':
            return
        button[coord].grid_forget()
        if grille[coord[0]][coord[1]] == 9:
            for i in range(LONG):
                for j in range(LONG):
                    if grille[i][j] == 9:
                        button[(i, j)].grid_forget()
            result.config(text="L.O.O.S.E.R")
        if grille[coord[0]][coord[1]] == 0:
            discovery(coord)
        else:
            discovered[coord[0]][coord[1]] = 1
        for i in range(LONG):
            if 0 not in discovered[i]:
                x += 1
        if x == LONG:
            result.config(text="GIGA CHAD")
        print(x)
        print(LONG)
        for i in range(LONG):
            print(discovered[i])

    # this function are going to be for the flap, but it needs to be implemented

    def put_flag():
        abs_coord_x = root.winfo_pointerx() - root.winfo_rootx()
        abs_coord_y = root.winfo_pointery() - root.winfo_rooty()
        print(abs_coord_x)
        print(abs_coord_y)

    # loading the image for the game

    img = {}
    for i in range(10):
        img[i] = tkinter.PhotoImage(file=f"img/{i}.png")

    # create the 2 layers of widget for the game

    answer = {}
    for i in range(1, LONG-1):
        for j in range(1, LONG-1):
            answer[(i, j)] = tkinter.Label(root, image=img[grille[i][j]])
            answer[(i, j)].grid(row=i+1, column=j, ipadx=3, ipady=3, sticky="N")

    button = {}
    for i in range(1, LONG-1):
        for j in range(1, LONG-1):
            button[(i, j)] = tkinter.Button(root, command=lambda x=(i, j): user_click(x))
            button[(i, j)].grid(row=i+1, column=j, ipadx=7)
            button[(i, j)].bind("<Button-3>", put_flag)

    # widget for telling the player if he loose or win

    result = tkinter.Label(root, font=("Minecraft", 20, "bold"))
    result.grid(row=0, columnspan=LONG)

    # render the windows

    root.mainloop()


game()

"""main = tkinter.Tk()
main.geometry("500x100")

len_grid = tkinter.Scale(main, from_=30, to=0, orient=tkinter.VERTICAL)
number_bomb = tkinter.Scale(main, from_=69, to=0, orient=tkinter.VERTICAL)
abc = tkinter.Button(main)
bcd = tkinter.Button(main)

fg = tkinter.Button(main,text = 'je be large', command = Game )
len_grid.place(x = 200)
number_bomb.place(x = 200+50)
abc.place(x= 0)
fg.place(x=50)

main.mainloop()
"""
