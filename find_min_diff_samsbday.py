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

def find_min(sorted_arr, k, N):
    """ input: sorted array = [], k = number of friends passed as an arg to this file """
    k0 = k - 1 # this is the index(position of kth element) in the array A
    minval = sorted_arr[k0] - sorted_arr[0] # this is the difference between first element and kth element, this is calculated so that it can be used for comparing with other diffs in the below if condition.
    # this is the index of kth element for finding diff from second element of the array, this k keeps incrementing by 1 in the below loop until the loop reaches N-kth element.
    for i in range(1, N - k+1): # loop executes from i = 1 to N-k (N-k-1) => ex:N=10,k=4 loop from element at index=(1,7) => the last diff executed will be between the last element which is k=10
        new_min = sorted_arr[k] - sorted_arr[i]
        # the below condition compares the prev calculated diff with the current diff
        if new_min < minval:
            minval = new_min
        print i, sorted_arr[i], sorted_arr[k], new_min, minval
        k = k + 1
    return minval


def main():
    #A = [11,100,35,40,2,5,7,9,8,1,10,3,15,18,50,45,70]
    # N is the number of chocolate packets
    # k is the number of friends
    N, k= [int(x) for x in raw_input('Enter number of chocolate packets and number of friends separated by a space: ').split()]

    while N <= k:
        print 'The number of packets is less than the number of friends.'
        N, k= [int(x) for x in raw_input('Enter number of chocolate packets and number of friends separated by a space: ').split()]

    A = [int(x) for x in raw_input('Enter the number of chocolates in each packet separated by a space: ').split()]

    while len(A) != N:
        print 'You have entered content of %d packets while the expected number of packets are %d. Please re-enter the contents of %d packets' % (len(A), N, N)
        A = [int(x) for x in raw_input('Enter the number of chocolates in each packet separated by a space: ').split()]
    print 'Input Array of chocolate packets = ', A
    sortedarr = quicksort(A, N)
    print 'Sorted Array of chocolate packets = ', sortedarr
    res = find_min(sortedarr,k,N)
    print 'The best minimum between the least and maximum chocolates the friends get is ', res

if __name__ == '__main__':
    main()

