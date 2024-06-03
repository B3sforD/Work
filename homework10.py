first = 123
second = 456
third = 789

if first == second == third:
    print(3)

first_1 = 42
second_1 = 69
third_2 = 42

if first_1 == second_1 or first_1 == third_2:
    print(2)
elif second_1 == third_2 or second_1 == first_1:
    print(2)
else:
    print(0)