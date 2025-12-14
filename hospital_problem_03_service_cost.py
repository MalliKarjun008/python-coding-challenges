def calculate_service_cost(service):
    costs = {
        "Doctor Consultation": 500,
        "Blood Test": 300,
        "X-Ray": 800,
        "ECG": 1000
    }
    return costs.get(service, 0)


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

    choice = int(input("Select a service (1-4): "))
    selected_service = services.get(choice)

    if not selected_service:
        print("Invalid Service")
        return

    cost = calculate_service_cost(selected_service)

    print("Selected Service:", selected_service)
    print("Service Cost:", cost)


def test_cases():
    assert calculate_service_cost("Doctor Consultation") == 500
    assert calculate_service_cost("Blood Test") == 300
    assert calculate_service_cost("X-Ray") == 800
    assert calculate_service_cost("ECG") == 1000
    assert calculate_service_cost("Unknown") == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
