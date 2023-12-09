#<p>The sum of the squares of the first ten natural numbers is,</p>
#$$1^2 + 2^2 + ... + 10^2 = 385.$$
#<p>The square of the sum of the first ten natural numbers is,</p>
#$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
#<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
#<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>

def sum_of_squares(upper):
    sum = 0
    for x in range(upper):
        sum += pow(x+1,2)
    return sum

def square_of_sums(upper):
    sum = 0
    for x in range(upper):
        sum += x+1
    return pow(sum,2)

def difference(bigger, smaller):
    return bigger - smaller

if __name__ == '__main__':
    print(difference(square_of_sums(100), sum_of_squares(100)))