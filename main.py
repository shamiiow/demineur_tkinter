# made by ø
# this code is not fuck dup anymore

import tkinter
import fonction


def Game() :
    # create the windows

    root = tkinter.Tk()
    root.geometry("500x500")

    # create the constant and the game grid


    LONG = 20
    NB_BOMB = 20
    grille = [[0 for i in range(LONG)] for i in range(LONG)]
    discovered = [[0 for j in range(LONG)] for i in range(LONG)]

    for i in range(LONG) :
        grille[0][i] = 100
        grille[LONG-1][i] = 100
        grille[i][0] = 100
        grille[i][LONG-1] = 100




    # place the bomb and put the right number around them

    grille = fonction.bomb(NB_BOMB, grille)
    grille = fonction.number_fill(LONG, grille)

    # this fonction is for cascading discovery of the boxes (not finish (because not working proprely))

    def discovery(coord):
        if 0<coord[0]<len(grille) and 0<coord[1]<len(grille):

            for i in range(3):
               if (0 <= grille[coord[0]-1][coord[1]-(1-i)] < 9) and (discovered[coord[0]-1][coord[1]-(1-i)] == 0):
                button[(coord[0]-1,coord[1]-(1-i))].grid_forget()
                discovered[coord[0]-1][coord[1]-(1-i)] = 1
                if grille[coord[0]-1][coord[1]-(1-i)] == 0:
                    discovery((coord[0]-1,coord[1]-(1-i)))
            for i in range(3):
               if (0 <= grille[coord[0]+1][coord[1]-(1-i)] < 9) and (discovered[coord[0]+1][coord[1]-(1-i)] == 0):
                button[(coord[0]+1,coord[1]-(1-i))].grid_forget()
                discovered[coord[0]+1][coord[1]-(1-i)] = 1
                if grille[coord[0]+1][coord[1]-(1-i)] == 0:
                    discovery((coord[0]+1,coord[1]-(1-i)))
            if (0 <= grille[coord[0]][coord[1]-1] < 9) and (discovered[coord[0]][coord[1]-1] == 0):
                button[(coord[0],coord[1]-1)].grid_forget()
                discovered[coord[0]][coord[1]-1] = 1
                if grille[coord[0]][coord[1]-1] == 0:
                    discovery((coord[0],coord[1]-1))
            if (0 <= grille[coord[0]][coord[1]+1] < 9) and (discovered[coord[0]][coord[1]+1] == 0):
                button[(coord[0],coord[1]+1)].grid_forget()
                discovered[coord[0]][coord[1]+1] = 1
                if grille[coord[0]][coord[1]+1] == 0:
                    discovery((coord[0],coord[1]+1))




    # this function is excecuted every time the player click


    def user_click(coord, nb_bomb):
        if result.cget('text')== '':
            if (len(button)) == nb_bomb:
                result.config(text="GIGA CHAD")
            button[coord].grid_forget()
            if grille[coord[0]][coord[1]] == 9:
                for i in range(LONG):
                    for j in range(LONG):
                        if grille[i][j] == 9:
                            button[(i, j)].grid_forget()
                result.config(text="L.O.O.S.E.R")
            if grille[coord[0]][coord[1]] == 0:
                discovery(coord)

    # this function are going to be for the flap, but it need to be implemented


    def put_flag(xa):
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
            button[(i, j)] = tkinter.Button(root, command=lambda x=(i, j), y=NB_BOMB: user_click(x, y))
            button[(i, j)].grid(row=i+1, column=j, ipadx=7)
            button[(i, j)].bind("<Button-3>", lambda x="test": put_flag(x))

    # widget for telling the player if he loose or win

    result = tkinter.Label(root, font=("Minercaft", 20, "bold"))
    result.grid(row=0, columnspan=LONG)

    # render the windows

    root.mainloop()
Game()

"""

main = tkinter.Tk()
main.geometry("500x100")


def js():
    Game(len_grid.get(), number_bomb.get())

len_grid = tkinter.Entry(main)
number_bomb = tkinter.Entry(main)
abc = tkinter.Button(main)
bcd = tkinter.Button(main)

fg = tkinter.Button(main,text = 'je suis large', command = js)
len_grid.place(x = 200)
number_bomb.place(x = 200, y= 50)
abc.place(x= 0)
fg.place(x=50)

main.mainloop()"""








