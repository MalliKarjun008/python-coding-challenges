def calculate_simple_interest(p, t, r):
    if p < 0 or t < 0 or r < 0:
        raise ValueError("Values cannot be negative")
    return (p * t * r) / 100


def main():
    try:
        p = float(input("Enter principal amount: "))
        t = float(input("Enter time (years): "))
        r = float(input("Enter rate of interest: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    try:
        si = calculate_simple_interest(p, t, r)
    except ValueError as e:
        print(e)
        return

    print("Simple Interest:", si)


def test_cases():
    assert calculate_simple_interest(1000, 2, 10) == 200.0
    assert calculate_simple_interest(0, 5, 10) == 0.0
    assert calculate_simple_interest(1500.5, 1.5, 7.5) == (1500.5 * 1.5 * 7.5) / 100

    try:
        calculate_simple_interest(-100, 2, 5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
