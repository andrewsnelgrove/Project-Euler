def primeNumberChecker(numToCheck):
    isPrimeNumber = True
    for i in range(2, numToCheck):
        if numToCheck % i == 0:
            isPrimeNumber = False

    if isPrimeNumber == True:
        return True
    else:
        return False


def main():
    limit = int(input("Enter the number of prime number you want to get: "))
    primeNumberCounter = 0
    numbers = 2

    while primeNumberCounter != limit:
        if primeNumberChecker(numbers) == True:
            primeNumberCounter += 1
            numbers += 1
        else:
            numbers += 1

    reqPrimeNum = numbers - 1

    print("That prime number is:", reqPrimeNum)
    
main()
    
    
