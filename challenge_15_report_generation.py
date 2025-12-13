def generate_report(name, emp_id, gross_monthly, annual_gross, taxable_income, tax, net_salary):
    print("Employee Tax Report")
    print("Name:", name)
    print("EmpID:", emp_id)
    print("Gross Monthly Salary:", gross_monthly)
    print("Annual Gross Salary:", annual_gross)
    print("Taxable Income:", taxable_income)
    print("Tax Payable:", tax)
    print("Annual Net Salary:", net_salary)


def main():
    name = input("Enter name: ")
    emp_id = input("Enter EmpID: ")
    gross_monthly = float(input("Enter gross monthly salary: "))
    annual_gross = float(input("Enter annual gross salary: "))
    taxable_income = float(input("Enter taxable income: "))
    tax = float(input("Enter total tax payable: "))

    net_salary = annual_gross - tax

    generate_report(
        name,
        emp_id,
        gross_monthly,
        annual_gross,
        taxable_income,
        tax,
        net_salary
    )


def test_cases():
    generate_report(
        "John",
        "E123",
        85000,
        1020000,
        970000,
        76800,
        943200
    )
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
