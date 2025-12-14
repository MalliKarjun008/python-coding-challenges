def apply_discounts(grand_total, total_quantity):
    if not isinstance(grand_total, (int, float)) or grand_total < 0:
        raise ValueError("Invalid grand total")
    if not isinstance(total_quantity, int) or total_quantity < 0:
        raise ValueError("Invalid total quantity")

    discounted_total = grand_total

    if discounted_total > 10000:
        discounted_total -= discounted_total * 0.10
    if total_quantity > 20:
        discounted_total -= discounted_total * 0.05

    return discounted_total


def main():
    while True:
        try:
            n = int(input("Enter number of items: "))
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Enter a non-negative integer.")

    grand_total = 0
    total_quantity = 0

    for _ in range(n):
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price per item: "))
                if quantity < 0 or price < 0:
                    raise ValueError
                grand_total += quantity * price
                total_quantity += quantity
                break
            except ValueError:
                print("Invalid quantity or price. Please re-enter.")

    final_total = apply_discounts(grand_total, total_quantity)
    print("Final Amount:", final_total)


def test_cases():
    assert apply_discounts(12000, 10) == 10800
    assert apply_discounts(12000, 25) == 10260
    assert apply_discounts(8000, 30) == 7600
    assert apply_discounts(5000, 5) == 5000

    try:
        apply_discounts(-1000, 5)
        assert False
    except ValueError:
        pass

    try:
        apply_discounts(5000, -2)
        assert False
    except ValueError:
        pass

    try:
        apply_discounts("10000", 10)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
