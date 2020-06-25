def sherlockAndAnagrams(s):
    n = len(s)
    d = {}
    res = 0

    for i in range(1,n):
        for j in range(n-i+1):
            sub = ''.join(sorted(s[j:j+i]))

            if sub not in d:
                d[sub] = 1
            else:
                d[sub] += 1

            res +=d[sub]-1

    return res
