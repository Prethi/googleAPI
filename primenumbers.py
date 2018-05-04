import math

def findprime(n1, n2):
    """ For the range provided find out the list of prime numbers """
    prime_num = []
    for num in range(n1, n2 + 1):
        #Creating a flag to check if prime or not
        prime = True

        #Checking if the provided number is an even number; if even set prim flag to False.
        if num % 2 == 0 and num > 2:
            #flag is set to False because num is not prime
            prime = False

        #If number is not even, take sqrt of it is obtained
        #and looped through the range of divisors from 3 to sqrt + 1
        #(as 1 can be ignored and 2 is tested in the above if loop)
        #skipping every 2nd element in the range as they are even numbers.
        else:
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    #flag is set to False because num is not prime
                    prime = False
                    continue
        if prime:
            prime_num.append(num)
    return prime_num

def main():
    """ user input for range of numbers to find primes present in the range """
    n1 = int(raw_input('Enter a start number ? '))
    n2 = int(raw_input('Enter a end number   ? '))
    prime_num = findprime(n1, n2)

if __name__ == '__main__':
    main()
