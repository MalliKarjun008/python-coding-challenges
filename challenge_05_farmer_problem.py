def calculate_sales(total_acres):
    if total_acres <= 0:
        raise ValueError("Total acres must be positive")

    acres_per_segment = total_acres / 5

    tomato_yield = (0.3 * acres_per_segment * 10 + 0.7 * acres_per_segment * 12) * 1000 * 7
    potato_yield = acres_per_segment * 10 * 1000 * 20
    cabbage_yield = acres_per_segment * 14 * 1000 * 24
    sunflower_yield = acres_per_segment * 0.7 * 1000 * 200
    sugarcane_yield = acres_per_segment * 45 * 4000

    total_sales = (
        tomato_yield
        + potato_yield
        + cabbage_yield
        + sunflower_yield
        + sugarcane_yield
    )

    chemical_free_sales = (
        tomato_yield
        + potato_yield
        + cabbage_yield
        + sunflower_yield
    )

    return total_sales, chemical_free_sales


def main():
    try:
        total_acres = float(input("Enter total acres: "))
    except ValueError:
        print("Invalid input. Enter numeric value only.")
        return

    try:
        total_sales, chemical_free_sales = calculate_sales(total_acres)
    except ValueError as e:
        print(e)
        return

    print("Overall Sales:", total_sales)
    print("Chemical Free Sales after 11 months:", chemical_free_sales)


def test_cases():
    total_sales, chemical_free_sales = calculate_sales(80)
    assert round(total_sales, 2) == round(chemical_free_sales + (80/5 * 45 * 4000), 2)
    assert chemical_free_sales < total_sales

    try:
        calculate_sales(0)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
