
# return a list of prime numbers [2-n], sorted in increasing order
# Param: integer
def primes_list(N):

    factorables = []
    primes_list = []

    # Iterate all ints between 2 and n
    i = 2
    while i <= N:
        # Determine if i is divisible by any number between 2 and i-1
        j = i-1
        while j > 1:
            # if J is a factor of I, I is not prime
            if (i%j==0) :

                factorables.append(i)
                break
            j -= 1

        # Add non-factorable int to primes_list
        if not(i in factorables):
            primes_list.append(i)

        i += 1

    return primes_list

def demo():
    while True:
        number = input("Enter a number and see a list of all the prime numbers less than it.\n")
        if number.isdigit():
            print(primes_list(number))
            continue
        return

demo()
