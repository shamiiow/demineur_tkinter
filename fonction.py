import random


def bomb(nb_bomb: int, grille: list, coord: tuple) -> list:
    for i in range(nb_bomb):
        while True:
            cx = random.randint(0, len(grille)-1)
            cy = random.randint(0, len(grille)-1)
            if (grille[cx][cy] == 0) and ((cx, cy) != (coord[0], coord[1])) and ((cx , cy) != (coord[0]-1, coord[1])) and ((cx , cy) != (coord[0], coord[1]-1)) and ((cx , cy) != (coord[0]-1, coord[1]-1)) and ((cx , cy) != (coord[0]+1, coord[1])) and ((cx , cy) != (coord[0], coord[1]+1)) and ((cx , cy) != (coord[0]+1, coord[1]+1)) and ((cx , cy) != (coord[0]+1, coord[1]-1)) and ((cx , cy) != (coord[0]-1, coord[1]+1)):
                grille[cx][cy] = 9
                break
    return grille


def number_fill(long: int, grille: list) -> list:
    for i in range(1, long-1):
        for j in range(1, long-1):
            if grille[i][j] != 9:
                for k in range(-1, 2):
                    for p in range(-1, 2, 2):
                        if grille[i+p][j-k] == 9:
                            grille[i][j] += 1
                    if grille[i][j+k] == 9:
                        grille[i][j] += 1
    return grille



