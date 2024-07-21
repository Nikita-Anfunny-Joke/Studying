

def reversed_(array):
    rv = []
    for i in range(len(array)):
        rv.append(array[i])
    return rv

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arr, reversed_(reversed_(arr)) == arr)
