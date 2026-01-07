# -------------------------------
# HealWell Care Hospital Billing System
# -------------------------------

# Initial arrays (as given)
SERVICES = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

COSTS = [500, 300, 800, 1500, 4000, 7000]

GST_RATE = 0.18


def get_patient_details():
    """Collect and validate patient details"""
    name = input("Enter Patient Name: ").strip()
    while not name:
        name = input("Name cannot be empty. Enter Patient Name: ").strip()

    while True:
        try:
            age = int(input("Enter Age: "))
            if age <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid age. Please enter a valid number.")

    gender = input("Enter Gender: ").strip()
    while not gender:
        gender = input("Gender cannot be empty. Enter Gender: ").strip()

    while True:
        contact = input("Enter Contact Number: ").strip()
        if contact.isdigit() and len(contact) == 10:
            break
        print("Invalid contact number. Enter a 10-digit number.")

    return name, age, gender, contact


def display_services():
    """Display available services"""
    print("\nAvailable Services:")
    for i, service in enumerate(SERVICES, start=1):
        print(f"{i}. {service}")


def get_selected_services():
    """Get and validate selected services"""
    while True:
        try:
            choices = input(
                "\nSelect services (comma separated numbers, e.g. 1,4): "
            ).split(",")

            selected_indexes = set()  # prevents duplicates
            for choice in choices:
                idx = int(choice.strip()) - 1
                if idx < 0 or idx >= len(SERVICES):
                    raise ValueError
                selected_indexes.add(idx)

            if not selected_indexes:
                raise ValueError

            break
        except ValueError:
            print("Invalid selection. Please choose valid service numbers.")

    selected_services = [SERVICES[i] for i in selected_indexes]
    selected_costs = [COSTS[i] for i in selected_indexes]

    return selected_services, selected_costs


def generate_invoice(patient, services, costs):
    """Generate and display invoice"""
    subtotal = sum(costs)
    gst = subtotal * GST_RATE
    grand_total = subtotal + gst

    print("\n" + "-" * 50)
    print("HealWell Care Hospital")
    print("Patient Invoice")
    print("-" * 50)

    print("\nPatient Information:")
    print(f"Name   : {patient[0]}")
    print(f"Age    : {patient[1]}")
    print(f"Gender : {patient[2]}")
    print(f"Contact: {patient[3]}")

    print("\nServices Availed:")
    for i, (service, cost) in enumerate(zip(services, costs), start=1):
        print(f"{i}. {service}: ₹{cost}")

    print(f"\nSubtotal      : ₹{subtotal}")
    print(f"GST (18%)     : ₹{gst:.2f}")
    print(f"Grand Total   : ₹{grand_total:.2f}")

    print("\nThank you for choosing HealWell Care Hospital!")
    print("-" * 50)


def main():
    print("Welcome to HealWell Care Hospital Billing System")

    patient_details = get_patient_details()
    display_services()
    selected_services, selected_costs = get_selected_services()
    generate_invoice(patient_details, selected_services, selected_costs)


if __name__ == "__main__":
    main()
