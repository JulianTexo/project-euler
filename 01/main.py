NUMBER1 = 5
NUMBER2 = 3
BOUND = 1000

def solve():
    numbers = []
    for x in range(1000):
        if x%3 == 0 or x%5 == 0:
            numbers.append(x)
    print(sum(numbers))

if __name__ == "__main__":
    solve()