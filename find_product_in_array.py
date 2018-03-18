import sys
import pdb
import string

def get_pivot_index(A, low, high):
    #pdb.set_trace()
    # Find median to set as pivot
    mid = (low + high)/2
    pivot = high
    if A[low] < A[mid]:
        if A[mid] < A[high]:
            pivot = mid
        elif A[low] > A[high]:
            pivot = low
    elif A[mid] > A[high]:
        pivot = mid
    elif A[low] < A[high]:
            pivot = low
    #print 'pivot = ', A[pivot]
    return pivot

def partition(A, low, high):
    #pdb.set_trace()
    pivotindex = get_pivot_index(A, low, high)
    pivotvalue = A[pivotindex]
    A[pivotindex], A[low] = A[low], A[pivotindex]
    #print 'A pivot = ', A
    ref = low
    for i in range(low, high+1):
        #print 'debug'
        if A[i] < pivotvalue:
            ref += 1
            A[ref], A[i] = A[i], A[ref]
    A[ref], A[low] = A[low], A[ref]
    #print 'A = ', A
    #print 'ref = ', ref
    return ref

def qspartitioned(A, low, high):
    #pdb.set_trace()
    if low<high:  # More than one item in th list
        ref = partition(A, low, high)
        qspartitioned(A, low, ref-1)
        qspartitioned(A, ref+1, high)

def quicksort(A, N):
    #pdb.set_trace()
    qspartitioned(A, 0, N-1)
    return A

def binary_search(arr, search_elem):
    index = None
    start = 0
    end = len(arr) - 1
    flag = False
    while start <= end and not flag:
        mid = (start + end)/2
        if arr[mid] == search_elem:
            index = mid
            flag = True
        else:
            if search_elem < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return [flag, index]

def find_product(arr, prod_elem):
    for i in arr:
        search_res = [False]
        search_elem = None
        if prod_elem % i == 0: search_elem = prod_elem/i
        if search_elem != None: search_res = binary_search(arr, search_elem)
        if search_res[0] == True and (search_res[1] != arr.index(i)):
            return [True, search_elem, i]

    print 'No element product pair found'
    return [False]

def main():
    """ Get the input from the user and sort the elements
        and then find if multiples are present."""
    i = 0
    A = []
    while True:
       try:
           N = int(raw_input('Enter the number of elements in the array: '))
           break
       except ValueError:
           i = i + 1
           if i == 3:
                print 'Terminating.. !'
                return
           print 'Entered value is not integer, enter again'

    for i in range(1,N+1):
        num = int(raw_input('Enter number %s = ' % i))
        A.append(num)

    search_elem = int(raw_input('Enter the element = '))
    sorted_array = quicksort(A, N)
    print 'sorted_array = ', sorted_array
    result = find_product(sorted_array, search_elem)
    if result[0]:
        print 'Elements found = %i, %i' % (result[1], result[2])


if __name__ == '__main__':
     main()
