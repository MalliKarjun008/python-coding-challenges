def calculate_tax(income):
    if not isinstance(income, (int, float)) or income < 0:
        raise ValueError("Invalid income")

    tax = 0

    if income > 1500000:
        tax += (income - 1500000) * 0.30
        income = 1500000
    if income > 1200000:
        tax += (income - 1200000) * 0.20
        income = 1200000
    if income > 900000:
        tax += (income - 900000) * 0.15
        income = 900000
    if income > 600000:
        tax += (income - 600000) * 0.10
        income = 600000
    if income > 300000:
        tax += (income - 300000) * 0.05

    rebate = tax if income <= 700000 else 0
    tax_after_rebate = tax - rebate
    cess = tax_after_rebate * 0.04
    total_tax = tax_after_rebate + cess

    return tax, rebate, cess, total_tax


def main():
    try:
        income = float(input("Enter annual income: "))
    except ValueError:
        print("Invalid input. Please enter numeric income.")
        return

    try:
        tax, rebate, cess, total_tax = calculate_tax(income)
    except ValueError as e:
        print(e)
        return

    print("Annual Income:", income)
    print("Calculated Tax:", tax)
    print("Rebate (Section 87A):", rebate)
    print("Health & Education Cess (4%):", cess)
    print("Total Tax Payable:", total_tax)


def test_cases():
    assert calculate_tax(250000)[3] == 0
    assert calculate_tax(500000)[3] == 0
    assert calculate_tax(700000)[3] == 0
    assert round(calculate_tax(800000)[3], 2) == 20800.0
    assert round(calculate_tax(1000000)[3], 2) == 46800.0
    assert round(calculate_tax(1500000)[3], 2) == 156000.0
    assert round(calculate_tax(2000000)[3], 2) == 312000.0

    try:
        calculate_tax(-100000)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
