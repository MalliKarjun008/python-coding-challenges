def search_2d_array(matrix, target):
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []

    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(int(input("Enter element: ")))
        matrix.append(row)

    target = int(input("Enter element to search: "))
    if search_2d_array(matrix, target):
        print("Element exists in the 2D array")
    else:
        print("Element does not exist in the 2D array")


def test_cases():
    assert search_2d_array([[1, 2], [3, 4]], 3) is True
    assert search_2d_array([[1, 2], [3, 4]], 5) is False
    assert search_2d_array([], 1) is False
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
