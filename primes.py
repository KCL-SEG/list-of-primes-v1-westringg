"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]

    curNum=3

    while len(list)<number_of_primes:
        isPrime=True
        print('curNum', curNum)
        divider=2
        while(divider<curNum):
            print('divider', divider)
            if curNum%divider==0:
                isPrime=False
            divider=divider+1
        
        if isPrime:
            list.append(curNum)

        curNum=curNum+1

    return list

#print(primes(10))
