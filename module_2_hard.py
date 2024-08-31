import random
list_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 , 18, 19, 20]
stone = random.choice(list_1)
print(stone)

pwd = []
for i in range(1, stone):
    for j in range(1, stone):
        if stone % (i + j) == 0:
            if i < j:
                pwd.extend([i, j])

print(*pwd)







