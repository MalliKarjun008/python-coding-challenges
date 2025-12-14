from challenge_11_basic_salary import basic_salary
from challenge_12_taxable_income import calculate_taxable_income
from challenge_13_tax_calculation import calculate_tax
from challenge_14_net_salary import calculate_net_salary


def print_report(
    name,
    emp_id,
    gross_monthly,
    annual_gross,
    taxable_income,
    tax,
    net_salary
):
    print("\nEMPLOYEE TAX REPORT")
    print("-" * 50)
    print(f"{'Field':25}Details")
    print("-" * 50)
    print(f"{'Name':25}{name}")
    print(f"{'EmpID':25}{emp_id}")
    print(f"{'Gross Monthly Salary':25}₹{gross_monthly:,.2f}")
    print(f"{'Annual Gross Salary':25}₹{annual_gross:,.2f}")
    print(f"{'Taxable Income':25}₹{taxable_income:,.2f}")
    print(f"{'Tax Payable':25}₹{tax:,.2f}")
    print(f"{'Annual Net Salary':25}₹{net_salary:,.2f}")
    print("-" * 50)


def main():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")

    try:
        monthly_salary = float(input("Enter monthly salary: "))
        allowances = float(input("Enter allowances: "))
        bonus_percent = float(input("Enter bonus percentage: "))
    except ValueError:
        print("Invalid input. Enter numeric values only.")
        return

    try:
        gross_monthly, annual_gross = basic_salary(
            monthly_salary, allowances, bonus_percent
        )

        taxable_income = calculate_taxable_income(annual_gross)[1]

        tax = calculate_tax(taxable_income)[3]

        net_salary = calculate_net_salary(annual_gross, tax)

    except ValueError as e:
        print(e)
        return

    print_report(
        name,
        emp_id,
        gross_monthly,
        annual_gross,
        taxable_income,
        tax,
        net_salary
    )


if __name__ == "__main__":
    main()
