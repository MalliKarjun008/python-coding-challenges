# =====================================================
# HealWell Care Hospital Billing System
# =====================================================

# -------- Level 7: Admin sets services of the day --------
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]


# -------- Utility: Safe integer input --------
def input_positive_int(prompt, allow_zero=False):
    while True:
        try:
            value = int(input(prompt))
            if allow_zero and value == 0:
                return value
            if value > 0:
                return value
            raise ValueError
        except ValueError:
            print("Please enter a valid positive integer.")


# -------- Level 1: Patient details --------
def get_patient_details():
    while True:
        name = input("Enter Patient Name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    age = input_positive_int("Enter Age: ")

    while True:
        gender = input("Enter Gender: ").strip()
        if gender:
            break
        print("Gender cannot be empty.")

    while True:
        contact = input("Enter Contact Number (10 digits): ").strip()
        if contact.isdigit() and len(contact) == 10:
            break
        print("Invalid contact number.")

    return name, age, gender, contact


# -------- Level 2: Display & select services --------
def select_services():
    print("\nAvailable Services:")
    for i, service in enumerate(services, start=1):
        print(f"{i}. {service}")

    selected_indices = set()

    while True:
        choice = input(
            "\nEnter service numbers separated by commas (e.g., 1,4): "
        ).strip()

        if not choice:
            print("You must select at least one service.")
            continue

        try:
            numbers = [int(x.strip()) for x in choice.split(",")]
        except ValueError:
            print("Invalid format. Use numbers only.")
            continue

        valid = True
        for num in numbers:
            if num < 1 or num > len(services):
                print(f"Service number {num} is invalid.")
                valid = False
                break

        if not valid:
            continue

        selected_indices.update(numbers)
        break

    selected_services = [services[i - 1] for i in sorted(selected_indices)]
    return selected_services


# -------- Level 3: Fetch costs --------
def get_selected_costs(selected_services):
    selected_costs = []
    for service in selected_services:
        index = services.index(service)
        selected_costs.append(costs[index])
    return selected_costs


# -------- Level 4: Subtotal --------
def calculate_subtotal(selected_costs):
    return sum(selected_costs)


# -------- Level 8: Discounts --------
def apply_discounts(subtotal, age):
    discount = 0

    # Senior citizen discount
    if age >= 60:
        discount += subtotal * 0.10

    subtotal_after_discount = subtotal - discount

    # High-bill discount
    if subtotal_after_discount > 5000:
        extra = subtotal_after_discount * 0.05
        discount += extra
        subtotal_after_discount -= extra

    return subtotal_after_discount, discount


# -------- Level 5: GST --------
def calculate_gst(amount):
    gst = amount * 0.18
    return gst, amount + gst


# -------- Level 6: Invoice --------
def generate_invoice(
    name, age, gender, contact,
    selected_services, selected_costs,
    subtotal, discount, gst, grand_total
):
    print("\n" + "-" * 55)
    print("HealWell Care Hospital")
    print("Patient Invoice")
    print("-" * 55)

    print("\nPatient Information:")
    print(f"Name    : {name}")
    print(f"Age     : {age}")
    print(f"Gender  : {gender}")
    print(f"Contact : {contact}")

    print("\nServices Availed:")
    for i in range(len(selected_services)):
        print(f"{i + 1}. {selected_services[i]}: ₹{selected_costs[i]}")

    print(f"\nSubtotal           : ₹{subtotal}")
    print(f"Discount Applied   : ₹{round(discount, 2)}")
    print(f"GST (18%)          : ₹{round(gst, 2)}")
    print(f"Grand Total        : ₹{round(grand_total, 2)}")

    print("\nThank you for choosing HealWell Care Hospital!")
    print("-" * 55)


# -------- Main Flow Controller --------
def main():
    # Level 1
    name, age, gender, contact = get_patient_details()

    # Level 2
    selected_services = select_services()

    # Level 3
    selected_costs = get_selected_costs(selected_services)

    # Level 4
    subtotal = calculate_subtotal(selected_costs)

    # Level 8
    discounted_total, discount = apply_discounts(subtotal, age)

    # Level 5
    gst, grand_total = calculate_gst(discounted_total)

    # Level 6
    generate_invoice(
        name, age, gender, contact,
        selected_services, selected_costs,
        subtotal, discount, gst, grand_total
    )


if __name__ == "__main__":
    main()
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
