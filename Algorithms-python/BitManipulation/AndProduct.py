import sys

def and_product(a, b):
    and_result = a
    if a % 4 == 0:
        for i in range(a + 4, b + 1, 4):
            and_result &= i
    elif a % 2 == 0:
        for i in range(a + 2, b + 1, 2):
            and_result &= i
    else:
        for i in range(a + 1, b + 1):
            and_result &= i
    return and_result

def main():
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        print(and_product(a, b))

if __name__ == "__main__":
    main()