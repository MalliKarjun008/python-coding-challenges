def number_to_words(num):
    mapping = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'
    }
    if num < 0:
        return "Minus " + " ".join(mapping[d] for d in str(abs(num)))
    return " ".join(mapping[d] for d in str(num))


def main():
    n = int(input("Enter number: "))
    print(number_to_words(n))


def test_cases():
    assert number_to_words(270176) == "Two Seven Zero One Seven Six"
    assert number_to_words(0) == "Zero"
    assert number_to_words(105) == "One Zero Five"
    assert number_to_words(-12) == "Minus One Two"
    print("All test cases passed!")


if __name__ == "__main__":
    main()
    test_cases()
