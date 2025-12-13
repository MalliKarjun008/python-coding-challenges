def calculate_result(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3

    if average >= 60:
        result = "1st Class"
    elif average >= 50:
        result = "2nd Class"
    elif average >= 35:
        result = "Pass Class"
    else:
        result = "Fail"

    return total, average, result


def main():
    name = input("Enter student name: ")
    m1 = float(input("Enter marks 1: "))
    m2 = float(input("Enter marks 2: "))
    m3 = float(input("Enter marks 3: "))

    total, average, result = calculate_result(m1, m2, m3)

    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)


def test_cases():
    assert calculate_result(60, 60, 60)[2] == "1st Class"
    assert calculate_result(50, 50, 50)[2] == "2nd Class"
    assert calculate_result(35, 35, 35)[2] == "Pass Class"
    assert calculate_result(10, 20, 30)[2] == "Fail"
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
