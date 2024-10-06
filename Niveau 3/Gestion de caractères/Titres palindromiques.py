# Lien vers l'éxercice: https://www.france-ioi.org/algo/task.php?idChapter=566&idTask=2417

def ispalindrome(phrase):
    phrase = str(phrase)
    livretrans = [char for char in phrase.lower() if char != " "]
    for a in range(
        int(len(livretrans) / 2)
        if len(livretrans) % 2 == 0
        else int((len(livretrans) - 1) / 2)
    ):
        if livretrans[a] != livretrans[-a - 1]:
            return
    print(phrase)


for i in range(int(input())):
    ispalindrome(input())
