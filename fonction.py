import random

# fonction qui place les bombes


def bomb(nb_bomb: int, grille: list, coord: tuple) -> list:
    # place le bon nombre de bombe de façon random
    for i in range(nb_bomb):
        while True:
            cx = random.randint(0, len(grille)-1)
            cy = random.randint(0, len(grille)-1)
            # cet énorme condition permet de faire en sorte que le premier clique ne sois jamais un nombre ou une bombe
            if (grille[cx][cy] == 0) and ((cx, cy) != (coord[0], coord[1])) and ((cx, cy) != (coord[0]-1, coord[1])) and ((cx, cy) != (coord[0], coord[1]-1)) and ((cx, cy) != (coord[0]-1, coord[1]-1)) and ((cx, cy) != (coord[0]+1, coord[1])) and ((cx, cy) != (coord[0], coord[1]+1)) and ((cx, cy) != (coord[0]+1, coord[1]+1)) and ((cx, cy) != (coord[0]+1, coord[1]-1)) and ((cx, cy) != (coord[0]-1, coord[1]+1)):
                grille[cx][cy] = 9
                break
    return grille

# fonction qui met les nombre autour des bombes


def number_fill(long: int, grille: list) -> list:
    for i in range(1, long-1):
        for j in range(1, long-1):
            # si la case n'est pas une bombe, on verifie combien il y en a autour et rajoute 1 si il en trouve une
            if grille[i][j] != 9:
                for k in [-1, 0, 1]:
                    for p in [-1, 1]:
                        if grille[i+p][j-k] == 9:
                            grille[i][j] += 1
                    if grille[i][j+k] == 9:
                        grille[i][j] += 1
    return grille
