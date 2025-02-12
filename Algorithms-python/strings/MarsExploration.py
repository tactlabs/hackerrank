def mars_exploration(s):
    count = 0
    for i, char in enumerate(s):
        expected_char = 'O' if i % 3 == 1 else 'S'
        if char != expected_char:
            count += 1
    return count

if __name__ == "__main__":
    s = input().strip()
    print(mars_exploration(s))
