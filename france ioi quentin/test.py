# Densité du plastique

import sys

N = int(input())
Stock = sorted(list(map(int, input().split())))


def tri(Stock, Value, z1, z2):
    middle = (z1 + z2) // 2
    if abs(z1 - z2) > 1:
        if Value < Stock[middle]:
            return tri(Stock, Value, z1, middle)
        elif Value > Stock[middle]:
            return tri(Stock, Value, middle, z2)
        else:
            return 1
    else:
        if Value == Stock[middle]:
            return 1
        elif Value < Stock[middle]:
            return 1 if Value == Stock[z1] else 0
        else:
            return 1 if Value == Stock[z2] else 0


for i in range(int(input())):
    print(tri(Stock, int(sys.stdin.readline()), 0, len(Stock) - 1))

