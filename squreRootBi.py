def bsearch(s, e, first, last, calls):
    print first, last, calls
    if (last - first) < 2: return s[first] == e or s[last] == e
    mid = first + (last - first)/2
    if s[mid] == e: return True
    if s[mid] > e: return bsearch(s, e, first, mid - 1, calls+1)
    return bsearch(s, e, mid + 1, last, calls + 1)

def search(s, e):
    print bsearch(s, e, 0, len(s) - 1, 1)

def selSort(L):
    for i in range(len(L) - 1):
        print L
        minIndx = i
        minVal= L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal= L[j]
            j = j + 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
s = range(10)
selSort(s)