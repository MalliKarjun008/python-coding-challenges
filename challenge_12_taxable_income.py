def calculate_taxable_income(annual_gross):
    standard_deduction = 50000
    taxable_income = annual_gross - standard_deduction
    if taxable_income < 0:
        taxable_income = 0
    return standard_deduction, taxable_income


def main():
    annual_gross = float(input("Enter annual gross salary: "))

    deduction, taxable_income = calculate_taxable_income(annual_gross)

    print("Annual Gross Salary:", annual_gross)
    print("Standard Deduction:", deduction)
    print("Taxable Income:", taxable_income)


def test_cases():
    d, t = calculate_taxable_income(600000)
    assert d == 50000
    assert t == 550000

    d, t = calculate_taxable_income(40000)
    assert t == 0

    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()

