def generate_invoice(name, services, amount):
    print("----- HealWell Care Hospital -----")
    print("Patient Name:", name)
    print("Services Availed:", ", ".join(services))
    print("Total Amount Payable:", amount)
    print("---------------------------------")


def main():
    name = input("Enter patient name: ")

    services = []
    n = int(input("Enter number of services: "))
    for _ in range(n):
        service = input("Enter service name: ")
        services.append(service)

    amount = float(input("Enter final payable amount: "))
    generate_invoice(name, services, amount)


def test_cases():
    generate_invoice("Test Patient", ["Doctor Consultation"], 500)
    print("Invoice generation test passed!")


if __name__ == "__main__":
    main()
    test_cases()
