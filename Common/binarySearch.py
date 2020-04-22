def binarySearch(a):
    l = 0
    h = len(a)
    c = h // 2
    while c != l:
        n = a[c]
        if n > target:
            h = c
            c = (c + l) // 2
        else:
            l = c
            c = (c + h) // 2
    return c
