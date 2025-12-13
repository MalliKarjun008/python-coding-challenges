def sort_array(arr, order):
    if order == "asc":
        return sorted(arr)
    if order == "desc":
        return sorted(arr, reverse=True)
    return arr


def main():
    n = int(input("Enter n: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter element: ")))

    order = input("Enter order (asc/desc): ").lower()
    print(sort_array(arr, order))


def test_cases():
    assert sort_array([3, 1, 2], "asc") == [1, 2, 3]
    assert sort_array([3, 1, 2], "desc") == [3, 2, 1]
    assert sort_array([], "asc") == []
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
