

def calculate_simple_interest(p, t, r):
    return (p * t * r) / 100


def main():
    p = float(input("Enter principal amount: "))
    t = float(input("Enter time (years): "))
    r = float(input("Enter rate of interest: "))

    si = calculate_simple_interest(p, t, r)
    print("Simple Interest:", si)


def test_cases():
    # Positive
    assert calculate_simple_interest(1000, 2, 10) == 200

    # Edge
    assert calculate_simple_interest(0, 5, 10) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
