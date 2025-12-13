def calculate_net_salary(annual_gross, total_tax):
    return annual_gross - total_tax


def main():
    annual_gross = float(input("Enter annual gross salary: "))
    total_tax = float(input("Enter total tax payable: "))

    net_salary = calculate_net_salary(annual_gross, total_tax)

    print("Annual Gross Salary:", annual_gross)
    print("Total Tax Payable:", total_tax)
    print("Annual Net Salary:", net_salary)


def test_cases():
    assert calculate_net_salary(1000000, 100000) == 900000
    assert calculate_net_salary(500000, 0) == 500000
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
