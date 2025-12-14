def calculate_item_total(code, quantity, price):
    if not isinstance(code, str):
        raise ValueError("Invalid item code")
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Invalid quantity")
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Invalid price")

    total = quantity * price

    if code.upper() == "PROMO10":
        total -= total * 0.10

    return total


def main():
    code = input("Enter item code: ").strip()

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))
            total = calculate_item_total(code, quantity, price)
            break
        except ValueError as e:
            print("Invalid input. Please re-enter correct values.")

    print("Total Amount:", total)


def test_cases():
    assert calculate_item_total("PROMO10", 2, 100) == 180
    assert calculate_item_total("promo10", 2, 100) == 180
    assert calculate_item_total("ITEM01", 2, 100) == 200
    assert calculate_item_total("PROMO10", 0, 100) == 0

    try:
        calculate_item_total("PROMO10", -1, 100)
        assert False
    except ValueError:
        pass

    try:
        calculate_item_total("PROMO10", 2, -100)
        assert False
    except ValueError:
        pass

    try:
        calculate_item_total(123, 2, 100)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
