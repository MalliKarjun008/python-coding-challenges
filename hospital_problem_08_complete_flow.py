def get_patient_details():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    contact = input("Enter contact number: ")
    return name, age, gender, contact


def select_services():
    services = {
        1: "Doctor Consultation",
        2: "Blood Test",
        3: "X-Ray",
        4: "ECG"
    }

    print("Available Services:")
    for k, v in services.items():
        print(k, "-", v)

    choices = input("Enter service numbers separated by space: ").split()
    selected = []
    for c in choices:
        c = int(c)
        if c in services:
            selected.append(services[c])
    return selected


def calculate_total_cost(services):
    costs = {
        "Doctor Consultation": 500,
        "Blood Test": 300,
        "X-Ray": 800,
        "ECG": 1000
    }

    total = 0
    for s in services:
        total += costs.get(s, 0)
    return total


def apply_discount(amount, has_insurance):
    if has_insurance:
        return amount * 0.80
    return amount


def apply_gst(amount):
    return amount * 1.05


def generate_invoice(name, age, gender, contact, services, amount):
    print("\n----- HealWell Care Hospital -----")
    print("Patient Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Contact:", contact)
    print("Services Availed:", ", ".join(services))
    print("Final Amount Payable:", round(amount, 2))
    print("---------------------------------")


def main():
    name, age, gender, contact = get_patient_details()
    services = select_services()

    total = calculate_total_cost(services)

    insurance = input("Do you have insurance? (yes/no): ").lower() == "yes"
    discounted_total = apply_discount(total, insurance)

    final_amount = apply_gst(discounted_total)

    generate_invoice(name, age, gender, contact, services, final_amount)


def test_cases():
    assert calculate_total_cost(["Doctor Consultation", "Blood Test"]) == 800
    assert apply_discount(1000, True) == 800
    assert apply_discount(1000, False) == 1000
    assert apply_gst(1000) == 1050
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
