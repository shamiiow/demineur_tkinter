# made by ø
# this code is not fuck dup anymore
import tkinter
import random

root = tkinter.Tk()
root.geometry("500x500")
LONG = 10
NB_BOMB = 10
grille = [[0 for j in range(LONG)] for i in range(LONG)]

for i in range(NB_BOMB):
    while True:
        cx = random.randint(0, len(grille)-1)
        cy = random.randint(0, len(grille)-1)
        if grille[cx][cy] == 0:
            grille[cx][cy] = 9
            break


for i in range(LONG) :
    print(grille[i])

img = {}
for i in range(10): #temporaire
    img[i] = tkinter.PhotoImage(file=f"img/{i}.png")


def userplay(coord):
    button[coord].grid_forget()


answer = {}
for i in range(LONG):
    for j in range(LONG):
        answer[(i, j)] = tkinter.Label(root, image=img[grille[i][j]]) #add that when all img are create : ""
        answer[(i, j)].grid(row=i, column=j, ipadx=1, ipady=3)

button = {}
for i in range(LONG):
    for j in range(LONG):
        button[(i, j)] = tkinter.Button(root, command=lambda x=(i, j): userplay(x))
        button[(i, j)].grid(row=i, column=j, ipadx=6)

root.mainloop()
