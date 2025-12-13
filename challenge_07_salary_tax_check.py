def must_pay_tax(salary):
    return salary > 300000


def main():
    name = input("Enter name: ")
    salary = float(input("Enter annual salary: "))

    if must_pay_tax(salary):
        print(name, "must pay tax")
    else:
        print(name, "does not need to pay tax")


def test_cases():
    assert must_pay_tax(300001) is True
    assert must_pay_tax(300000) is False
    assert must_pay_tax(0) is False
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
