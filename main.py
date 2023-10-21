a = [2, 1, 2, 1, 2, 1]
b = []


def rec(a, level, hod):
    b = []
    if level == 0:
        return a
    for i in range(len(a) - 1):
        x = a.copy()
        if hod == 1:
            if x[i] == 1 and x[i + 1] == 2:
                x[i] = 0
                x[i + 1] = 1
                x = rec(x, level - 1, 2)
                b.append(x)
            elif x[i] == 2 and x[i + 1] == 1:
                x[i] = 1
                x[i + 1] = 0
                x = rec(x, level - 1, 2)
                b.append(x)
        elif hod == 2:
            if x[i] == 1 and x[i + 1] == 2:
                x[i] = 2
                x[i + 1] = 0
                x = rec(x, level - 1, 1)
                b.append(x)
            elif x[i] == 2 and x[i + 1] == 1:
                x[i] = 0
                x[i + 1] = 2
                x = rec(x, level - 1, 1)
                b.append(x)

    return b


print(rec(a, 3, 1))
