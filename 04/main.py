def isPalindrom(number):
    for x in range(int(round(len(str(number)))/2)):
        if int(str(number)[x]) != int(str(number)[len(str(number))-(1+x)]):
            return False
    return True

def findLargestPalindromProduct():
    palindromProducts = []
    for x in range(999):
        for y in range(999):
            result = (999-x) * (999-y)
            if isPalindrom(result):
                palindromProducts.append(result)
    return max(palindromProducts)

#some unit testing? wtf is dis
def unitTesting():
    print(isPalindrom(123321))
    print(isPalindrom(1234))
    print(isPalindrom(12321))

if __name__ == "__main__":
    #unitTesting()
    print(findLargestPalindromProduct())