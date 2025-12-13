def is_valid_name(name):
    return name.isalpha() and len(name) <= 50


def is_valid_emp_id(emp_id):
    return emp_id.isalnum() and 5 <= len(emp_id) <= 10


def is_valid_salary(value):
    return value > 0 and value <= 10000000


def is_valid_bonus(bonus):
    return 0 <= bonus <= 100


def main():
    name = input("Enter name: ")
    emp_id = input("Enter EmpID: ")
    basic = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowance: "))
    bonus = float(input("Enter bonus percentage: "))

    if not is_valid_name(name):
        print("Invalid Name")
        return
    if not is_valid_emp_id(emp_id):
        print("Invalid EmpID")
        return
    if not is_valid_salary(basic) or not is_valid_salary(allowance):
        print("Invalid Salary")
        return
    if not is_valid_bonus(bonus):
        print("Invalid Bonus Percentage")
        return

    print("All inputs are valid")


def test_cases():
    assert is_valid_name("John") is True
    assert is_valid_name("John123") is False
    assert is_valid_emp_id("E12345") is True
    assert is_valid_emp_id("E1") is False
    assert is_valid_salary(50000) is True
    assert is_valid_salary(-1) is False
    assert is_valid_bonus(10) is True
    assert is_valid_bonus(150) is False
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
