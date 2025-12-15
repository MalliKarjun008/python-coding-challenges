def num_to_words(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    mapping = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    return " ".join(mapping[digit] for digit in str(n))


def main():
    while True:
        try:
            n = int(input("Enter a non-negative integer N: "))
            words = num_to_words(n)
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

    print("Number in Words:")
    print(words)


def test_cases():
    assert num_to_words(123) == "one two three"
    assert num_to_words(0) == "zero"
    assert num_to_words(5) == "five"
    assert num_to_words(9081726354) == "nine zero eight one seven two six three five four"

    try:
        num_to_words(-3)
        assert False
    except ValueError:
        pass

    try:
        num_to_words(4.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    main()
