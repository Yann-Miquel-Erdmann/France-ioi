# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=509&idTask=455

l = int(input())
h, w = int(input()), int(input())
t = int(input())

print("".join(["X"] * l))
print()
for i in range(h):
    if i in [0, h - 1]:
        print("".join(["#"] * w))
    else:
        print("".join(["#"] + [" "] * (w - 2) + ["#"] * (0 if w == 1 else 1)))

print()

for i in range(t):
    if i == 0:
        print("@")
    elif i < t - 1:
        print("".join(["@"] + [" "] * (i - 1) + ["@"]))
    else:
        print("".join(["@"] * t))
