def calculate_item_total(code, quantity, price):
    total = quantity * price
    if code == "PROMO10":
        total -= total * 0.10
    return total


def main():
    code = input("Enter item code: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    total = calculate_item_total(code, quantity, price)
    print("Total Amount:", total)


def test_cases():
    assert calculate_item_total("PROMO10", 2, 100) == 180
    assert calculate_item_total("ITEM01", 2, 100) == 200
    assert calculate_item_total("PROMO10", 0, 100) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
