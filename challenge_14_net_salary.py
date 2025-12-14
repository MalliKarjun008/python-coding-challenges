def calculate_net_salary(annual_gross, total_tax):
    if not isinstance(annual_gross, (int, float)) or not isinstance(total_tax, (int, float)):
        raise ValueError("Invalid input")
    if annual_gross < 0 or total_tax < 0 or total_tax > annual_gross:
        raise ValueError("Invalid salary or tax values")

    return annual_gross - total_tax


def main():
    try:
        annual_gross = float(input("Enter annual gross salary: "))
        total_tax = float(input("Enter total tax payable: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    try:
        net_salary = calculate_net_salary(annual_gross, total_tax)
    except ValueError as e:
        print(e)
        return

    print("Annual Gross Salary:", annual_gross)
    print("Total Tax Payable:", total_tax)
    print("Annual Net Salary:", net_salary)


def test_cases():
    assert calculate_net_salary(1000000, 100000) == 900000
    assert calculate_net_salary(500000, 0) == 500000
    assert calculate_net_salary(10**7, 10**6) == 9 * 10**6

    try:
        calculate_net_salary(-500000, 10000)
        assert False
    except ValueError:
        pass

    try:
        calculate_net_salary(500000, 600000)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
