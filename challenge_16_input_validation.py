def is_valid_name(name):
    return name.isalpha() and 0 < len(name) <= 50


def is_valid_emp_id(emp_id):
    return emp_id.isalnum() and 5 <= len(emp_id) <= 10


def is_valid_basic_salary(value):
    return value > 0 and value <= 10000000


def is_valid_allowance(value):
    return value >= 0 and value <= 10000000


def is_valid_bonus(bonus):
    return 0 <= bonus <= 100


def main():
    while True:
        name = input("Enter name: ").strip()
        if is_valid_name(name):
            break
        print("Invalid Name. Alphabets only, max 50 characters.")

    while True:
        emp_id = input("Enter EmpID: ").strip()
        if is_valid_emp_id(emp_id):
            break
        print("Invalid EmpID. Alphanumeric, length 5–10.")

    while True:
        try:
            basic = float(input("Enter basic salary: "))
            if is_valid_basic_salary(basic):
                break
        except ValueError:
            pass
        print("Invalid basic salary.")

    while True:
        try:
            allowance = float(input("Enter allowance: "))
            if is_valid_allowance(allowance):
                break
        except ValueError:
            pass
        print("Invalid allowance.")

    while True:
        try:
            bonus = float(input("Enter bonus percentage: "))
            if is_valid_bonus(bonus):
                break
        except ValueError:
            pass
        print("Invalid bonus percentage.")

    gross_monthly = basic + allowance
    annual_gross = gross_monthly * 12

    if gross_monthly <= 0:
        print("Invalid gross monthly salary.")
        return

    if annual_gross > 50000000:
        print("Annual gross salary exceeds realistic limit.")
        return

    print("All inputs are valid")


if __name__ == "__main__":
    main()
