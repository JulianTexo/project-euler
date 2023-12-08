#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with $1$ and $2$, the first $10$ terms will be:
#$$1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots$$</p>
#<p>By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

UPPERBOUND = 4000000

def fibonacci() -> list:
    fib = []
    x = 1
    fib.append(x)
    prev_x = 1
    while x < UPPERBOUND:
        temp = x
        x += prev_x
        if x < UPPERBOUND:
            fib.append(x)
        prev_x = temp
    print(fib)
    return fib

def solve():
    fib = fibonacci()
    evens = []
    for line in fib:
        if line % 2 == 0:
            evens.append(line)
    print(sum(evens))

if __name__ == "__main__":
    solve()
