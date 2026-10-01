while True:
    try:
        s = input()
    except EOFError:
        break

    isCapitalized = True
    s = s.strip()
    listString = s.lower().split()
    for i in range(len(listString)):
        if isCapitalized:
            listString[i] = listString[i].capitalize()
            isCapitalized = False
        if listString[i][-1] in "?!.":
            listString[i] = listString[i][:-1]
            print(listString[i])
            isCapitalized = True
        else:
            print(listString[i], end = " ")