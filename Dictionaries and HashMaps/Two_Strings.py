def twoStrings(s1, s2):
    s1 = list(s1)
    flag = 'NO'
    prev = []
    for char in s1:
        if(char in prev):
            continue
        if(re.search(char, s2)):
            flag = 'YES'
            break
        prev.append(char)
        #print prev
    return(flag)
