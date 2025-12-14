def calculate_discount(total_amount, discount_percent):
    if total_amount < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount values")

    discount = (total_amount * discount_percent) / 100
    final_amount = total_amount - discount
    return discount, final_amount


def main():
    try:
        total_amount = float(input("Enter total amount: "))
        discount_percent = float(input("Enter discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return

    try:
        discount, final_amount = calculate_discount(total_amount, discount_percent)
    except ValueError as e:
        print(e)
        return

    print("Discount Amount:", discount)
    print("Final Amount:", final_amount)


def test_cases():
    assert calculate_discount(1000, 10) == (100.0, 900.0)
    assert calculate_discount(500, 0) == (0.0, 500.0)
    assert calculate_discount(2000, 50) == (1000.0, 1000.0)
    assert calculate_discount(0, 10) == (0.0, 0.0)

    try:
        calculate_discount(-100, 10)
        assert False
    except ValueError:
        pass

    try:
        calculate_discount(100, 150)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
