def heapify(array, n, i):
    largest = i
    l = i*2 + 1
    r = i*2 + 2

    if (l<n and array[l] > array[largest]):
        largest = l
    if (r<n and array[r] > array[largest]):
        largest = r

    if largest != i:
        array[largest], array[i] = array[i], array[largest]

        heapify(array, n, largest)

def heap_sort(array, n):

    for i in range(n//2 -1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)




A = [10,7,8,11,1,2,3,4]

heap_sort(A, 8)

print(A)
