def calculate_grand_total(items):
    total = 0

    for item in items:
        if (
            not isinstance(item, tuple)
            or len(item) != 2
            or not isinstance(item[0], int)
            or item[0] < 0
            or not isinstance(item[1], (int, float))
            or item[1] < 0
        ):
            raise ValueError("Invalid item entry")

        qty, price = item
        total += qty * price

    return total


def main():
    items = []

    while True:
        try:
            n = int(input("Enter number of items: "))
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Enter a non-negative integer.")

    for _ in range(n):
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price per item: "))
                if quantity < 0 or price < 0:
                    raise ValueError
                items.append((quantity, price))
                break
            except ValueError:
                print("Invalid quantity or price. Please re-enter.")

    grand_total = calculate_grand_total(items)
    print("Grand Total:", grand_total)


def test_cases():
    assert calculate_grand_total([(2, 100), (1, 50)]) == 250
    assert calculate_grand_total([]) == 0
    assert calculate_grand_total([(0, 100)]) == 0

    try:
        calculate_grand_total([(-1, 100)])
        assert False
    except ValueError:
        pass

    try:
        calculate_grand_total([(2, -50)])
        assert False
    except ValueError:
        pass

    try:
        calculate_grand_total([(2,)])
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
