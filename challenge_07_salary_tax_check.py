def must_pay_tax(salary):
    if not isinstance(salary, (int, float)) or salary < 0:
        raise ValueError("Invalid salary")
    return salary > 300000


def main():
    name = input("Enter name: ")
    try:
        salary = float(input("Enter annual salary: "))
    except ValueError:
        print("Invalid input. Please enter numeric salary.")
        return

    try:
        if must_pay_tax(salary):
            print(name, "must pay tax")
        else:
            print(name, "does not need to pay tax")
    except ValueError as e:
        print(e)


def test_cases():
    assert must_pay_tax(300001) is True
    assert must_pay_tax(300000) is False
    assert must_pay_tax(0) is False
    assert must_pay_tax(10**7) is True

    try:
        must_pay_tax(-5000)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
