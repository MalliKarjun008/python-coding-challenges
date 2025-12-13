def calculate_item_total(quantity, price):
    return quantity * price


def main():
    code = input("Enter item code: ")
    description = input("Enter item description: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    total = calculate_item_total(quantity, price)

    print("Item Code:", code)
    print("Description:", description)
    print("Total Amount:", total)


def test_cases():
    assert calculate_item_total(2, 100) == 200
    assert calculate_item_total(0, 100) == 0
    assert calculate_item_total(5, 0) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
