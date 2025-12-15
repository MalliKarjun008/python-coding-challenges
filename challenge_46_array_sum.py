def array_sum(arr):
    if not isinstance(arr,list):
        raise ValueError("Input must be a list")
    total=0
    for x in arr:
        total+=x
    return total
def main():
    while True:
        try:
            n = int(input("Enter number of elements N: "))
            arr = []
            for i in range(n):
                arr.append(int(input(f"Enter element {i + 1}: ")))
            result = array_sum(arr)
            break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    print("Sum of array elements:")
    print(result)

def test_cases():
    assert array_sum([1, 2, 3, 4, 5]) == 15
    assert array_sum([-1, -2, -3, -4, -5]) == -15
    assert array_sum([0, 0, 0]) == 0
    assert array_sum([10]) == 10
    assert array_sum([]) == 0

    try:
        array_sum("not a list")
        assert False
    except ValueError:
        pass

    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()
    main()