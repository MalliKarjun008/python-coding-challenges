def reverse_array(arr):
    return arr[::-1]


def main():
    n = int(input("Enter n: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))

    print(reverse_array(arr))


def test_cases():
    assert reverse_array([1, 2, 3]) == [3, 2, 1]
    assert reverse_array([]) == []
    assert reverse_array([5]) == [5]
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
