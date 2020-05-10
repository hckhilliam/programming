def binarySearch(a, target):
    # Returns lower of value if cannot be found.
    l = 0
    h = len(a)
    c = h // 2
    while c != l:
        n = a[c]
        # Go lower case.
        if n > target:
            h = c
            c = (c + l) // 2
        # Go higher case.
        else:
            l = c
            c = (c + h) // 2
    return c