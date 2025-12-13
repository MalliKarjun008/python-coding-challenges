def calculate_tax(taxable_income):
    tax = 0

    slabs = [
        (300000, 0),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20)
    ]

    remaining = taxable_income

    for limit, rate in slabs:
        if remaining > limit:
            tax += limit * rate
            remaining -= limit
        else:
            tax += remaining * rate
            remaining = 0
            break

    if remaining > 0:
        tax += remaining * 0.30

    if taxable_income <= 700000:
        tax = 0

    cess = tax * 0.04
    total_tax = tax + cess

    return tax, cess, total_tax


def main():
    taxable_income = float(input("Enter taxable income: "))

    tax, cess, total_tax = calculate_tax(taxable_income)

    print("Tax:", tax)
    print("Cess:", cess)
    print("Total Tax Payable:", total_tax)


def test_cases():
    tax, cess, total = calculate_tax(700000)
    assert total == 0

    tax, cess, total = calculate_tax(1000000)
    assert total > 0

    tax, cess, total = calculate_tax(300000)
    assert total == 0

    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
