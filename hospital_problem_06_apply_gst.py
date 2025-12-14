def apply_gst(amount):
    gst_rate = 0.05
    gst = amount * gst_rate
    return amount + gst


def main():
    amount = float(input("Enter final amount before GST: "))
    total_with_gst = apply_gst(amount)
    print("Amount after GST:", total_with_gst)


def test_cases():
    assert apply_gst(1000) == 1050
    assert apply_gst(0) == 0
    assert apply_gst(500) == 525
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
