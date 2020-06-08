def checkMagazine(magazine, note):
    magz = Counter(magazine)
    notz = Counter(note)

    result = notz - magz

    if result == {}:
        print("Yes")
    else:
        print("No")
