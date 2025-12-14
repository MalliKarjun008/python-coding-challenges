def select_services():
    services = {
        1: "Doctor Consultation",
        2: "Blood Test",
        3: "X-Ray",
        4: "ECG"
    }

    print("Available Services:")
    for key, value in services.items():
        print(key, "-", value)

    choice = int(input("Select a service (1-4): "))
    return services.get(choice, "Invalid Service")


def main():
    selected_service = select_services()
    print("Selected Service:", selected_service)


def test_cases():
    services = {
        1: "Doctor Consultation",
        2: "Blood Test",
        3: "X-Ray",
        4: "ECG"
    }
    assert services.get(1) == "Doctor Consultation"
    assert services.get(4) == "ECG"
    assert services.get(5, "Invalid Service") == "Invalid Service"
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
