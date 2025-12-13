def count_odd_even(arr):
    odd = 0
    even = 0
    for x in arr:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even


def main():
    n = int(input("Enter n: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))

    odd, even = count_odd_even(arr)
    print("Odd count:", odd)
    print("Even count:", even)


def test_cases():
    assert count_odd_even([1, 2, 3, 4]) == (2, 2)
    assert count_odd_even([2, 4, 6]) == (0, 3)
    assert count_odd_even([]) == (0, 0)
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
