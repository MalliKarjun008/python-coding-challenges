def sum_and_avg(a, b):
    total = a + b
    average = total / 2
    return total, average


def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    total, average = sum_and_avg(a, b)
    print(f"Sum is: {total}")
    print(f"Average is: {average}")


def test_cases():
    assert sum_and_avg(10, 10) == (20, 10.0)
    assert sum_and_avg(-5, -15) == (-20, -10.0)
    assert sum_and_avg(0, 0) == (0, 0.0)
    assert sum_and_avg(-10, 20) == (10, 5.0)
    assert sum_and_avg(10**9, 10**9) == (2 * 10**9, 10**9)

    print("All test cases passed successfully.")


if __name__ == "__main__":
    test_cases()
    main()
