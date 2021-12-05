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
