def sansa_and_xor(arr):
    n = len(arr)
    if n % 2 == 0:
        return 0
    xor = arr[-1]
    for i in range(n - 1):
        if i % 2 == 0:
            xor ^= arr[i]
    return xor


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(sansa_and_xor(arr))


if __name__ == "__main__":
    main()