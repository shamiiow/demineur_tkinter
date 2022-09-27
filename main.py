# made by ø
# this code is not fuck dup anymore
import tkinter
import random

root = tkinter.Tk()
root.geometry("500x500")
LONG = 25
NB_BOMB = 20
grille = [[0 for j in range(LONG)] for i in range(LONG)]

for i in range(NB_BOMB):
    while True:
        cx = random.randint(0, len(grille)-1)
        cy = random.randint(0, len(grille)-1)
        if grille[cx][cy] == 0:
            grille[cx][cy] = 9
            break

for i in range(1, LONG-1):
    for j in range(1, LONG-1):
        if grille[i][j] != 9:
            if grille[i][j-1] == 9:
                grille[i][j] += 1
            if grille[i][j+1] == 9:
                grille[i][j] += 1

            for k in range(3):
                if grille[i+1][j-(k-1)] == 9:
                    grille[i][j] += 1
            for k in range(3):
                if grille[i-1][j-(k-1)] == 9:
                    grille[i][j] += 1

# border
# grille[0]
for i in range(1, LONG-1):
    if grille[0][i] != 9:
        if grille[0][i+1] == 9:
            grille[0][i] += 1
        if grille[0][i-1] == 9:
            grille[0][i] += 1

        if grille[1][i+1] == 9:
            grille[0][i] += 1
        if grille[1][i-1] == 9:
            grille[0][i] += 1
        if grille[1][i] == 9:
            grille[0][i] += 1

# grille[LONG]
for i in range(1, LONG-1):
    if grille[LONG-1][i] != 9:
        if grille[LONG-1][i+1] == 9:
            grille[LONG-1][i] += 1
        if grille[LONG-1][i-1] == 9:
            grille[LONG-1][i] += 1

        if grille[LONG-2][i+1] == 9:
            grille[LONG-1][i] += 1
        if grille[LONG-2][i-1] == 9:
            grille[LONG-1][i] += 1
        if grille[LONG-2][i] == 9:
            grille[LONG-1][i] += 1

# grille left
for i in range(1, LONG-1):
    if grille[i][0] != 9:
        if grille[i+1][0] == 9:
            grille[i][0] += 1
        if grille[i-1][0] == 9:
            grille[i][0] += 1

        if grille[i+1][1] == 9:
            grille[i][0] += 1
        if grille[i-1][1] == 9:
            grille[i][0] += 1
        if grille[i][1] == 9:
            grille[i][0] += 1

# grille right
for i in range(1, LONG-1):
    if grille[i][LONG-1] != 9:
        if grille[i+1][LONG-1] == 9:
            grille[i][LONG-1] += 1
        if grille[i-1][LONG-1] == 9:
            grille[i][LONG-1] += 1

        if grille[i+1][LONG-2] == 9:
            grille[i][LONG-1] += 1
        if grille[i-1][LONG-2] == 9:
            grille[i][LONG-1] += 1
        if grille[i][LONG-2] == 9:
            grille[i][LONG-1] += 1

for i in range(LONG):
    print(grille[i])

img = {}
for i in range(10):
    img[i] = tkinter.PhotoImage(file=f"img/{i}.png")


def userplay(coord):
    button[coord].grid_forget()


answer = {}
for i in range(LONG):
    for j in range(LONG):
        answer[(i, j)] = tkinter.Label(root, image=img[grille[i][j]])
        answer[(i, j)].grid(row=i, column=j, ipadx=1, ipady=3)

button = {}
for i in range(LONG):
    for j in range(LONG):
        button[(i, j)] = tkinter.Button(root, command=lambda x=(i, j): userplay(x))
        #button[(i, j)].grid(row=i, column=j, ipadx=6)

root.mainloop()
