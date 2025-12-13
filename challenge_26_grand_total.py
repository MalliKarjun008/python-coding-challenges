def calculate_grand_total(items):
    total = 0
    for qty, price in items:
        total += qty * price
    return total


def main():
    items = []
    n = int(input("Enter number of items: "))

    for _ in range(n):
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        items.append((quantity, price))

    grand_total = calculate_grand_total(items)
    print("Grand Total:", grand_total)


def test_cases():
    assert calculate_grand_total([(2, 100), (1, 50)]) == 250
    assert calculate_grand_total([]) == 0
    assert calculate_grand_total([(0, 100)]) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
