def generate_series(n):
    result=[]
    diffs=[4,4,4,8]
    num=1
    i=0
    while num<=n:
        result.append(num)
        num+=diffs[i]
        i=(i+1)%len(diffs)
    return result


def main():
    n = int(input("Enter N: "))
    print(*generate_series(n))


def test_cases():
    assert generate_series(50) == [1, 5, 9, 13, 21, 25, 29, 37, 41, 45, 49]
    assert generate_series(45) == [1, 5, 9, 13, 21, 25, 29, 37, 41, 45]
    assert generate_series(20) == [1, 5, 9, 13]
    assert generate_series(1) == [1]
    assert generate_series(0) == []
    print("All test cases passed!")



if __name__ == "__main__":
    main()
    test_cases()
