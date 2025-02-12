def count_gem_elements(rocks):
    n = len(rocks)
    count = 0
    
    for char in range(97, 123):  # ASCII values for 'a' to 'z'
        present_in_all = True
        
        for rock in rocks:
            if chr(char) not in rock:
                present_in_all = False
                break
        
        if present_in_all:
            count += 1
    
    return count


if __name__ == "__main__":
    n = input().split()
    # print('n: ', n)
    count_gem_elements(n)
    print('count_gem_elements(n): ', count_gem_elements(n))