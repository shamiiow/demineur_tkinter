# made by ø
# this code is not fuck dup anymore

import tkinter
import fonction

root = tkinter.Tk()
root.geometry("500x500")
LONG = 10
NB_BOMB = 1
grille = [[0 for j in range(LONG)] for i in range(LONG)]

grille = fonction.bomb(NB_BOMB, grille)
grille = fonction.number_fill(LONG, grille)

def discovery(coord) :
    if 0 < coord[0] < (LONG-1) and 0 < coord[1] < (LONG-1):
        if grille[coord[0]][coord[1]] == 0:
            for i in range(0, 3, 2):
                if grille[coord[0]-(i-1)][coord[1]] != 9:
                    button[(coord[0]-(i-1), coord[1])].grid_forget()
                if grille[coord[0]][coord[1]-(i-1)] != 9:
                    button[(coord[0], coord[1]-(i-1))].grid_forget()


def user_click(coord, nb_bomb):
    if (len(button)) == nb_bomb:
        result.config(text="baka..")
    button[coord].grid_forget()
    if grille[coord[0]][coord[1]] == 9:
        for i in range(LONG):
            for j in range(LONG):
                button[(i, j)].grid_forget()
        result.config(text="L.O.O.S.E.R")
    discovery(coord)

    print((len(button)))
    print(nb_bomb)
    print("-------------")


def put_flag(event):
    print(event)


img = {}
for i in range(10):
    img[i] = tkinter.PhotoImage(file=f"img/{i}.png")

answer = {}
for i in range(LONG):
    for j in range(LONG):
        answer[(i, j)] = tkinter.Label(root, image=img[grille[i][j]])
        answer[(i, j)].grid(row=i+1, column=j, ipadx=2, ipady=3, sticky="N")

button = {}
for i in range(LONG):
    for j in range(LONG):
        button[(i, j)] = tkinter.Button(root, command=lambda x=(i, j), y=NB_BOMB: user_click(x,y))
        button[(i, j)].grid(row=i+1, column=j, ipadx=6)
        button[(i, j)].bind("<Button-3>", lambda x="test": put_flag(x))

result = tkinter.Label(root, font=("Minercaft", 20, "bold"))
result.grid(row=0, columnspan=LONG)

root.mainloop()
