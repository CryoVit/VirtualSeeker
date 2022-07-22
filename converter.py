with open ('full.txt', mode = 'r', encoding = 'utf-8') as loaf:
    tot = 0
    for line in loaf:
        tot = tot + 1
        if tot < 2:
            continue
        if tot > 3:
            break
        conut = line.split()
        for i in range (0, 5):
            print(conut[i], end = ',')
        print('')