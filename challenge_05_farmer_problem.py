def calculate_sales():
    acres_per_segment = 80 / 5

    tomato_acres = acres_per_segment
    potato_acres = acres_per_segment
    cabbage_acres = acres_per_segment
    sunflower_acres = acres_per_segment
    sugarcane_acres = acres_per_segment

    tomato_yield = (0.3 * tomato_acres * 10 + 0.7 * tomato_acres * 12) * 1000 * 7
    potato_yield = potato_acres * 10 * 1000 * 20
    cabbage_yield = cabbage_acres * 14 * 1000 * 24
    sunflower_yield = sunflower_acres * 0.7 * 1000 * 200
    sugarcane_yield = sugarcane_acres * 45 * 4000

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
    total_sales, chemical_free_sales = calculate_sales()
    print("Overall Sales:", total_sales)
    print("Chemical Free Sales after 11 months:", chemical_free_sales)


def test_cases():
    total_sales, chemical_free_sales = calculate_sales()
    assert total_sales > 0
    assert chemical_free_sales < total_sales
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
