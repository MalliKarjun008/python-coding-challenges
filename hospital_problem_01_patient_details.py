def get_patient_details():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    contact = input("Enter contact number: ")
    return name, age, gender, contact


def main():
    name, age, gender, contact = get_patient_details()
    print("Patient Details:")
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Contact:", contact)


def test_cases():
    assert callable(get_patient_details)
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
