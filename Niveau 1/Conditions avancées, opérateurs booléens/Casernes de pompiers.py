# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=648&idTask=1979

n_z = 1
for i in range(n_z):
    a_X_min = 1
    a_X_max = 6
    a_Y_min = 1
    a_Y_max = 5

    b_X_min = 4
    b_X_max = 9
    b_Y_min = 3
    b_Y_max = 8

    if min(a_X_min, b_X_min) == a_X_min:
        c_X_min = a_X_min
        c_X_max = a_X_max
        c_Y_min = a_Y_min
        c_Y_max = a_Y_max

        d_X_min = b_X_min
        d_X_max = b_X_max
        d_Y_min = b_Y_min
        d_Y_max = b_Y_max
    else:
        d_X_min = a_X_min
        d_X_max = a_X_max
        d_Y_min = a_Y_min
        d_Y_max = a_Y_max

        c_X_min = b_X_min
        c_X_max = b_X_max
        c_Y_min = b_Y_min
        c_Y_max = b_Y_max

    if c_X_max <= d_X_min or (c_Y_max <= d_Y_min or c_Y_min >= d_Y_max):
        print("NON")
    else:
        print("OUI")
