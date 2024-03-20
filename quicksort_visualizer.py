COUNTER = []

def qprint(A, i, j, r):
    '''
    A: array
    i: swappable index
    j: loop index
    r: pivot index
    '''
    print("[", end='')
    for el in range(len(A)):
        element = A[el]
        if el == r:
            print(f"\033[91m{element}\033[0m", end=', ')
        elif el == i and i != -1:
            print(f"\033[96m{element}\033[0m", end=', ')
        elif el == j:
            print(f"\033[92m{element}\033[0m", end=', ')
        else:
            print(element, end =', ')
    print('\033[2D]')
    print(f'i = index\033[96m{i}\033[0m; j = index\033[92m{j}\033[0m\n')

def exchange(A, a1, a2):
    temp = A[a1]
    A[a1] = A[a2]
    A[a2] = temp

def partition(A, p, r):
    pivot = A[r]
    i = p-1
    for j in range(p,r):
        COUNTER.append(1)
        qprint(A, i, j, r)
        if A[j] <= pivot:
            i += 1
            print("swap, i+1 with j")
            qprint(A, i, j, r)
            exchange(A, i, j)
    exchange(A, i+1, r)
    qprint(A, i, j, i+1)
    return i+1

def Quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        # Partition returns q such that
        #   i. A[q] = pivot
        #  ii. All elements <= pivot appear in A[p, ..., q-1]
        # iii. All elements > pivot appear in A[q+1, ..., r]
        Quicksort(A, p, q-1)
        Quicksort(A, q+1, r)

array = [3,1,7,6,4,8,2,5]

# worst cases
array1 = [1,2,3,4,5,6,7,8,9,10,11]
array2 = [1,1,1,1,1,1,1,1,1,1,1]

array3 = [2,1,5,4,3,8,7,11,10,9,6] # best case example
Quicksort(array3, 0, 10)
print(len(COUNTER))
