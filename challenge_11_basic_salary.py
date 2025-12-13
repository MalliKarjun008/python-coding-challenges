def calculate_gross_salary(basic, allowance, bonus_percent):
    gross_monthly = basic + allowance
    annual_bonus = (gross_monthly * 12) * (bonus_percent / 100)
    annual_gross = (gross_monthly * 12) + annual_bonus
    return gross_monthly, annual_gross


def main():
    name = input("Enter name: ")
    emp_id = input("Enter EmpID: ")
    basic = float(input("Enter basic monthly salary: "))
    allowance = float(input("Enter special allowance: "))
    bonus_percent = float(input("Enter bonus percentage: "))

    gross_monthly, annual_gross = calculate_gross_salary(basic, allowance, bonus_percent)

    print("Name:", name)
    print("EmpID:", emp_id)
    print("Gross Monthly Salary:", gross_monthly)
    print("Annual Gross Salary:", annual_gross)


def test_cases():
    gm, ag = calculate_gross_salary(50000, 10000, 10)
    assert gm == 60000
    assert ag == 792000
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()

