#$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
#What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from $1$ to $20$?</p>

def findSmallestEvenlyDivisible(upper):
    numberToTest = 2520
    running = True
    while running:
        for x in range(upper):
            if not numberToTest%(x+1)==0:
                break
        else:
            running = False
            break
        numberToTest += 1
    return numberToTest

if __name__ == "__main__":
    print(findSmallestEvenlyDivisible(20))