def apply_discounts(grand_total, total_quantity):
    if grand_total > 10000:
        grand_total -= grand_total * 0.10
    if total_quantity > 20:
        grand_total -= grand_total * 0.05
    return grand_total


def main():
    n = int(input("Enter number of items: "))
    grand_total = 0
    total_quantity = 0

    for _ in range(n):
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        grand_total += quantity * price
        total_quantity += quantity

    final_total = apply_discounts(grand_total, total_quantity)
    print("Final Amount:", final_total)


def test_cases():
    assert apply_discounts(12000, 10) == 10800
    assert apply_discounts(12000, 25) == 10260
    assert apply_discounts(8000, 30) == 7600
    assert apply_discounts(5000, 5) == 5000
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
