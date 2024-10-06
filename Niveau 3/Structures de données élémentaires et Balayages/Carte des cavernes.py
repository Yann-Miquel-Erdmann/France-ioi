# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=527&idTask=2772

# import random
import sys

# import time


def main():
    nb = int(sys.stdin.readline())
    cavernes = "".join(list(sys.stdin.readline()[:-1])).replace(" ", "")
    # cavernes = "".join(random.choice(["(", " ", ")"]) for i in range(10000)).replace(
    #     " ", ""
    # )

    big = "(" * 50 + ")" * 50

    # cavernes = "(" * 50000 + ")" * 50000
    # l = list(cavernes)
    # random.shuffle(l)
    # cavernes = "".join(l)
    # t = time.time()
    if len(cavernes) % 2 == 0 and cavernes.count("(") == len(cavernes) / 2:

        for i in range(int(len(cavernes) / 10)):
            cave = cavernes.replace(big, "")
            if cavernes == cave:
                break
            cavernes = cave
        for i in range(int(len(cavernes) / 2)):
            cavernes = cavernes.replace("()", "")

        print("1" if len(cavernes) == 0 else "0")
    else:
        print("0")
    # print(time.time() - t)


main()
