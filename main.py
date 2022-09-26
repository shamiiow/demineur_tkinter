# made by ø
# this code is fuck dup
import tkinter
import random


def game(x, y):
    nb_bomb = 10
    root = tkinter.Tk()
    long = 11
    grille = [[0 for j in range(long+1)] for i in range(long+1)]

    for i in range(nb_bomb):
        while True:
            cx = random.randint(1, len(grille)-2)
            cy = random.randint(1, len(grille)-2)
            if grille[cx][cy] == 0:
                grille[cx][cy] = 10
                break
    for i in range(1, len(grille)-1):
        for j in range(1, len(grille)-1):
            if grille[i][j] != 10:
                if grille[i][j-1] == 10:
                    grille[i][j] += 1
                if grille[i][j+1] == 10:
                    grille[i][j] += 1

                for k in range(3):
                    if grille[i+1][j-(k-1)] == 10:
                        grille[i][j] += 1
                for k in range(3):
                    if grille[i-1][j-(k-1)] == 10:
                        grille[i][j] += 1

    root.geometry(f"{len(grille)*30}x{len(grille[0]*27)}")
    nb_bomb = 5

    def moredeleted(coord):
        if grille[int(coord[0])][int(coord[1])] != 10:
            if grille[int(coord[0])][int(coord[1])-1] != 10:
                b[f"{int(coord[0])}{int(coord[1])-1}"].grid_forget()
            if grille[int(coord[0])][int(coord[1]) + 1] != 10:
                b[f"{int(coord[0])}{int(coord[1])+1}"].grid_forget()
            for k in range(3):
                if grille[int(coord[0])+1][int(coord[1])-(k-1)] != 10 and (int(coord[0])+1) != 0 and (int(coord[1])-(k-1)) != 0 and (int(coord[0]+1)) != len(grille) and (int(coord[1]-(k-1))) != len(grille):
                    b[f"{int(coord[0])+1}{int(coord[1])-(k-1)}"].grid_forget()
            for k in range(3):
                if grille[int(coord[0])-1][int(coord[1])-(k-1)] != 10 and (int(coord[0])-1) != 0 and (int(coord[1])-(k-1)) != 0 and (int(coord[0]-1)) != len(grille) and (int(coord[1]-(k-1))) != len(grille):
                    b[f"{int(coord[0])-1}{int(coord[1])-(k-1)}"].grid_forget()

    def hidethecase(coord: str):
        b[coord].grid_forget()
        moredeleted(coord)


        if grille[int(coord[0])][int(coord[1])] == 10:
            print("boom")

    a = {}
    for i in range(1, len(grille)-1):
        for j in range(1, len(grille)-1):
            a[f"{i}{j}"] = tkinter.Label(root, text=grille[i][j])

    b = {}
    for i in range(1, len(grille)-1):
        for j in range(1, len(grille)-1):
            b[f"{i}{j}"] = tkinter.Button(root, command=lambda coord=f"{i}{j}": hidethecase(coord))
            b[f"{i}{j}"].bind("<Button-3>")

    for i in range(1, len(grille)-1):
        for j in range(1, len(grille)-1):
            a[f"{i}{j}"].grid(row=i, column=j, ipadx=10, ipady=3)

    for i in range(1, len(grille)-1):
        for j in range(1, len(grille)-1):
            b[f"{i}{j}"].grid(row=i, column=j, ipadx=10, ipady=3)


    root.mainloop()


game(1000, 100)
