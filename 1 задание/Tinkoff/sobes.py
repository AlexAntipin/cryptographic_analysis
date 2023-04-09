for a in range(100):
    for b in range(100):
        for c in range(100):
            if (2 * a * b + b * c + c == 273) and (a * b + b * c - a * c - b == -70):
                print(f'A = {a}')
                print(f'B = {b}')
                print(f'C = {c}')