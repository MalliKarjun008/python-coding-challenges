def calculate_total_cost(selected_services):
    costs = {
        "Doctor Consultation": 500,
        "Blood Test": 300,
        "X-Ray": 800,
        "ECG": 1000
    }

    total = 0
    for service in selected_services:
        total += costs.get(service, 0)

    return total


def main():
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

    selected_services = []
    for c in choices:
        c = int(c)
        if c in services:
            selected_services.append(services[c])

    total_cost = calculate_total_cost(selected_services)

    print("Selected Services:", ", ".join(selected_services))
    print("Total Cost:", total_cost)


def test_cases():
    assert calculate_total_cost(["Doctor Consultation", "Blood Test"]) == 800
    assert calculate_total_cost(["X-Ray", "ECG"]) == 1800
    assert calculate_total_cost([]) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
