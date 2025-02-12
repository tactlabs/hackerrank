def hackerrank_in_string(queries):
    target = "hackerrank"
    target_len = len(target)
    
    results = []
    
    for s in queries:
        i, j = 0, 0
        l = len(s)
        print('l: ', l)
        
        while i < l and j < target_len:
            if s[i] == target[j]:
                j += 1
            i += 1
        
        results.append("YES" if j == target_len else "NO")
    
    return results

# Test cases
def test_hackerrank_in_string():
    assert hackerrank_in_string(["hereiamstackerrank"]) == ["YES"]
    assert hackerrank_in_string(["hackerworld"]) == ["NO"]
    assert hackerrank_in_string(["hhaacckkekraraannk"]) == ["YES"]
    assert hackerrank_in_string(["abcdefghijklmnopqrstuvwxyz"]) == ["NO"]
    assert hackerrank_in_string(["hackerrank"]) == ["YES"]
    print("All test cases passed!")

test_hackerrank_in_string()
