# made by ø
# this code is not fuck dup anymore

import tkinter
import fonction

root = tkinter.Tk()
root.geometry("500x500")
LONG = 10
NB_BOMB = 5
grille = [[0 for j in range(LONG)] for i in range(LONG)]

grille = fonction.bomb(NB_BOMB, grille)
grille = fonction.number_fill(LONG, grille)


def user_click(coord):
    button[coord].grid_forget()
    if 0 < coord[0] < (LONG-1) and 0 < coord[1] < (LONG-1):
        if grille[coord[0]][coord[1]] == 0:
            for i in range(0, 3, 2):
                if grille[coord[0]-(i-1)][coord[1]] != 9:
                    button[(coord[0]-(i-1), coord[1])].grid_forget()
                if grille[coord[0]][coord[1]-(i-1)] != 9:
                    button[(coord[0], coord[1]-(i-1))].grid_forget()


def thatwork(a):
    print(a)


img = {}
for i in range(10):
    img[i] = tkinter.PhotoImage(file=f"img/{i}.png")

answer = {}
for i in range(LONG):
    for j in range(LONG):
        answer[(i, j)] = tkinter.Label(root, image=img[grille[i][j]])
        answer[(i, j)].grid(row=i, column=j, ipadx=1, ipady=3)

button = {}
for i in range(LONG):
    for j in range(LONG):
        button[(i, j)] = tkinter.Button(root, command=lambda x=(i, j): user_click(x))
        button[(i, j)].grid(row=i, column=j, ipadx=6)
        button[(i, j)].bind("<Button-3>", lambda x="test": thatwork(x))

root.mainloop()
