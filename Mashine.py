def find_pairs_password(n):
    result = ""

    for a in range(1, 21):
        for b in range(1, 21):
            if a != b:
                if n % (a + b) == 0:
                    result += f"{a}{b}"

    return result

for i in range(3, 21):
    print(f"{i}: {find_pairs_password(i)}")