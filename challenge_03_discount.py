def calculate_discount(total_amount, discount_percent):
    discount = (total_amount * discount_percent) / 100
    final_amount = total_amount - discount
    return discount, final_amount


def main():
    total_amount = float(input("Enter total amount: "))
    discount_percent = float(input("Enter discount percentage: "))

    discount, final_amount = calculate_discount(total_amount, discount_percent)

    print("Discount Amount:", discount)
    print("Final Amount:", final_amount)


def test_cases():
    assert calculate_discount(1000, 10) == (100, 900)
    assert calculate_discount(500, 0) == (0, 500)
    assert calculate_discount(2000, 50) == (1000, 1000)
    assert calculate_discount(0, 10) == (0, 0)

    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
