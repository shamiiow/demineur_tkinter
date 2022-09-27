import random


def number_fill(long, grille):
    for i in range(1, long - 1):
        for j in range(1, long - 1):
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
    for i in range(1, long - 1):
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
    for i in range(1, long - 1):
        if grille[long - 1][i] != 9:
            if grille[long - 1][i + 1] == 9:
                grille[long - 1][i] += 1
            if grille[long - 1][i - 1] == 9:
                grille[long - 1][i] += 1

            if grille[long - 2][i + 1] == 9:
                grille[long - 1][i] += 1
            if grille[long - 2][i - 1] == 9:
                grille[long - 1][i] += 1
            if grille[long - 2][i] == 9:
                grille[long - 1][i] += 1

    # grille left
    for i in range(1, long - 1):
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
    for i in range(1, long - 1):
        if grille[i][long - 1] != 9:
            if grille[i+1][long - 1] == 9:
                grille[i][long - 1] += 1
            if grille[i-1][long - 1] == 9:
                grille[i][long - 1] += 1

            if grille[i+1][long - 2] == 9:
                grille[i][long - 1] += 1
            if grille[i-1][long - 2] == 9:
                grille[i][long - 1] += 1
            if grille[i][long - 2] == 9:
                grille[i][long - 1] += 1

    for i in range(long):
        print(grille[i])

    return grille


def bomb(nb_bomb, grille):
    for i in range(nb_bomb):
        while True:
            cx = random.randint(0, len(grille)-1)
            cy = random.randint(0, len(grille)-1)
            if grille[cx][cy] == 0:
                grille[cx][cy] = 9
                break

    return grille

