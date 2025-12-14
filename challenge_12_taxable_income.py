def calculate_taxable_income(annual_gross):
    if not isinstance(annual_gross, (int, float)) or annual_gross < 0:
        raise ValueError("Invalid annual gross salary")

    standard_deduction = 50000
    taxable_income = annual_gross - standard_deduction
    if taxable_income < 0:
        taxable_income = 0
    return standard_deduction, taxable_income


def main():
    try:
        annual_gross = float(input("Enter annual gross salary: "))
    except ValueError:
        print("Invalid input. Please enter numeric salary.")
        return

    try:
        deduction, taxable_income = calculate_taxable_income(annual_gross)
    except ValueError as e:
        print(e)
        return

    print("Annual Gross Salary:", annual_gross)
    print("Standard Deduction:", deduction)
    print("Taxable Income:", taxable_income)


def test_cases():
    d, t = calculate_taxable_income(600000)
    assert d == 50000
    assert t == 550000

    d, t = calculate_taxable_income(40000)
    assert t == 0

    d, t = calculate_taxable_income(10**7)
    assert t == 10**7 - 50000

    try:
        calculate_taxable_income(-100000)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
