#

def primeNumberChecker(numToCheck):
    isPrimeNumber = True
        for i in range(2, numToCheck):
            if numToCheck % i == 0:
                isPrimeNumber = False

    if isPrimeNumber == True:
        return True
    else:
        return False
    
        
