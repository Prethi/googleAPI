import random
import numpy

def find_2Dpeak(_2darray, num_rows, num_col, mid):

          col = [row[mid] for row in _2darray]
          print '\nChosen columns = ', col
          #max_index = find_max(col)
          max_index = col.index(max(col))
          #print (max_index)

          if mid == 0 or mid == len(_2darray)-1:
              #print ('_2darray[max_index][mid] = ', _2darray[max_index][mid])
              return _2darray[max_index][mid]

          if _2darray[max_index][mid-1] < _2darray[max_index][mid] > _2darray[max_index][mid+1]:
              #print ('_2darray[max_index][mid] = ', _2darray[max_index][mid])
              return _2darray[max_index][mid]

          if _2darray[max_index][mid] < _2darray[max_index][mid-1]:
              #print ('left = ', _2darray, num_rows, num_col, mid - mid/2)
              return find_2Dpeak(_2darray, num_rows, num_col, mid - mid/2)

          elif _2darray[max_index][mid] < _2darray[max_index][mid+1]:
              #print ('right = ', _2darray, num_rows, num_col, mid + mid/2)
              return find_2Dpeak(_2darray, num_rows, num_col, mid + mid/2)

def main():
    i = 0
    while True:
        try:
            num_rows = int(raw_input('Enter number of rows = '))
            num_cols = int(raw_input('Enter number of columns = '))
            break
        except ValueError:
            i = i + 1
            if i == 5:
                print('Terminating...!')
                return
            print 'Entered input is not an integer, Re-enter all values '

    matrix =numpy.random.random_integers(0, 200, (num_rows, num_cols))
    print matrix
    res = find_2Dpeak(matrix, num_rows, num_cols, num_cols/2)
    print '\nThe peak is = ', res

    # Few examples for different scenarios
    #matrix  = [[16,  3,  5, 18], [2, 18,  7, 16],[17, 15,  4,  7],[ 6, 20, 14,  9]]
    #matrix = [[14, 18,  3, 15], [2,  1,  8,  3], [10, 20, 15,  2], [6, 14, 3, 10]]
    #res = find_2Dpeak([[180, 159, 107, 21], [200, 8, 110, 114], [138, 174, 96,  15],[161, 0, 19, 135]], 4, 4, 4/2)
    #res = find_2Dpeak([[1,2,3,4], [5,7,8,9], [2,13,5,10], [8,6,15,1]], 4, 4, 4/2)
    #print '\nThe peak is = ', res

if __name__ == '__main__':
     main()
