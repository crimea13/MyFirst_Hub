first = int(input("Введите первое число: "))
second = int(input("Введите второе чисоо: "))
third = int(input("Введите третье чисоо: "))

if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)