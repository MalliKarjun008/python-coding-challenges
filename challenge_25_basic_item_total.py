def calculate_item_total(quantity, price):
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Invalid quantity")
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Invalid price")
    return quantity * price


def main():
    code = input("Enter item code: ")
    description = input("Enter item description: ")

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))
            total = calculate_item_total(quantity, price)
            break
        except ValueError as e:
            print("Invalid input. Please re-enter valid quantity and price.")

    print("Item Code:", code)
    print("Description:", description)
    print("Total Amount:", total)


def test_cases():
    assert calculate_item_total(2, 100) == 200
    assert calculate_item_total(0, 100) == 0
    assert calculate_item_total(5, 0) == 0

    try:
        calculate_item_total(-1, 100)
        assert False
    except ValueError:
        pass

    try:
        calculate_item_total(5, -10)
        assert False
    except ValueError:
        pass

    try:
        calculate_item_total(2.5, 100)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
