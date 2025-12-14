def basic_salary(monthly_salary,allowances,bonus_percent):
    for value in (monthly_salary, allowances, bonus_percent):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Invalid salary components")
    monthly_gross=monthly_salary+allowances
    bonus=monthly_salary*12*(bonus_percent/100)
    annual_gross=(monthly_gross*12)+bonus
    return monthly_gross,annual_gross

def main():
    name=input("Enter name: ")
    empId=input("enter employee ID:")
    try:
        monthly_salary=float(input("Enter monthly salary: "))
        allowances=float(input("Enter allowances: "))
        bonus_percent=float(input("Enter bonus percentage: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return
    try:
        monthly_gross,annual_gross=basic_salary(monthly_salary,allowances,bonus_percent)        
    except ValueError as e:
        print(e)
        return
    print("Employee Name:",name)
    print("Employee ID:",empId)     
    print("Monthly Gross Salary:",monthly_gross)
    print("Annual Gross Salary:",annual_gross)  

def test_cases():
    assert basic_salary(5000, 2000, 10) == (7000.0, 84000.0)
    assert basic_salary(0, 0, 0) == (0.0, 0.0)
    assert basic_salary(10000, 5000, 20) == (15000.0, 204000.0)
    assert basic_salary(7500, 2500, 15) == (10000.0, 133500.0)

    try:
        basic_salary(-5000, 2000, 10)
        assert False
    except ValueError:
        pass

    try:
        basic_salary(5000, -2000, 10)
        assert False
    except ValueError:
        pass

    try:
        basic_salary(5000, 2000, -10)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")

if __name__=="__main__":
    test_cases()
    main()