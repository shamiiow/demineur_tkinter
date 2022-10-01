# made by ø
# this code is not fuck dup anymore

import tkinter
import fonction

while True:
    def game():
        # create the constant and the game grid

        LONG = 15
        NB_BOMB = 20
        grille = [[0 for i in range(LONG)] for i in range(LONG)]
        discovered = [[0 for j in range(LONG)] for i in range(LONG)]

        # create the windows

        root = tkinter.Tk()
        root.geometry(f"500x500")

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

        # this function is for cascading discovery of the boxes (not finish (because not working properly))

        def discovery(coord):
            if not (0 < coord[0] < len(grille) and 0 < coord[1] < len(grille)):
                return
            for i in range(-1,2):
                for j in range(-1,2,2):
                    if (0 <= grille[coord[0]+j][coord[1]+i] < 9) and (discovered[coord[0]+j][coord[1]+i] == 0):
                        button[(coord[0]+j, coord[1]+i)].grid_forget()
                        discovered[coord[0]+j][coord[1]+i] = 1
                        if grille[coord[0]+j][coord[1]+i] == 0:
                            discovery((coord[0]+j, coord[1]+i))
            for i in range(-1, 2, 2):
                if (0 <= grille[coord[0]][coord[1]+i] < 9) and (discovered[coord[0]][coord[1]+i] == 0):
                    button[(coord[0], coord[1]+i)].grid_forget()
                    discovered[coord[0]][coord[1]+i] = 1
                    if grille[coord[0]][coord[1]+i] == 0:
                        discovery((coord[0], coord[1]+i))

        # this function is executed every time the player click

        def user_click(coord):
            x = 0
            if grille[coord[0]][coord[1]] == 10:
                return
        #   if result.cget('text') != '':
        #       return
            button[coord].grid_forget()
            if grille[coord[0]][coord[1]] == 9:
                for i in range(LONG):
                    for j in range(LONG):
                        if grille[i][j] == 9:
                            button[(i, j)].grid_forget()
                print('Tu as perdu')
            if grille[coord[0]][coord[1]] == 0:
                discovery(coord)
            else:
                discovered[coord[0]][coord[1]] = 1
            for i in range(LONG):
                if 0 not in discovered[i]:
                    x += 1
            if x == LONG:
                print('Tu as win')

        # this function are going to be for the flap, but it needs to be implemented

        def put_flag(event, x):
            print(x)

        # loading the image for the game

        img = {}
        for i in range(11):
            img[i] = tkinter.PhotoImage(file=f"img/{i}.png")

        # create the 2 layers of widget for the game

        gamef = tkinter.Frame(root, bd=2, bg='red')
        gamef.grid(row=1, column=0)

        statf = tkinter.Frame(root, bd=2, bg='blue')
        statf.grid(row=0, column=0)

        answer = {}
        for i in range(1, LONG-1):
            for j in range(1, LONG-1):
                answer[(i, j)] = tkinter.Label(gamef, image=img[grille[i][j]])
                answer[(i, j)].grid(row=i+1, column=j, ipadx=3, ipady=3, sticky="N")

        button = {}
        for i in range(1, LONG-1):
            for j in range(1, LONG-1):
                button[(i, j)] = tkinter.Button(gamef, command=lambda x=(i, j): user_click(x))
                button[(i, j)].grid(row=i+1, column=j, ipadx=7)
                button[(i, j)].bind("<Button-3>", lambda e, x=(i, j): put_flag(e, x))

        bomb_r = tkinter.Label(statf, text=LONG, font=("Minecraft", 20, "bold"))
        bomb_r.grid(row=0, column=0)

        restart = tkinter.Button(statf, text='Restart', command=game)
        restart.grid(row=0, column=1)
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
