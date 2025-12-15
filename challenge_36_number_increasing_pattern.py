def number_increasing_pattern(n):
    if not isinstance(n,int) or n<=0:
        raise ValueError("Input must be a positive integer")
    pattern=[]
    for i in range(1,n+1):
        pattern.append(str(i)*i)
    return pattern
def main():
    while True:
        try:
            n=int(input("Enter a positive integer N: "))
            pattern=number_increasing_pattern(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    print("Number Increasing Pattern:")
    for line in pattern:
        print(line)
def test_cases():

    assert number_increasing_pattern(3) == ['1', '22', '333']
    assert number_increasing_pattern(1) == ['1']
    assert number_increasing_pattern(5) == ['1', '22', '333', '4444', '55555']

    try:
        number_increasing_pattern(0)
        assert False
    except ValueError:
        pass

    try:
        number_increasing_pattern(-3)
        assert False
    except ValueError:
        pass

    try:
        number_increasing_pattern(4.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!") 
if __name__ == "__main__":
    test_cases()
    main()