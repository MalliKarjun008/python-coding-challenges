def fibonacci_pattern(n):
    if not isinstance(n,int) or n<=0:
        raise ValueError("Input must be a positive integer.")
    pattern=[]
    a=1
    b=1
    for i in range(1,n+1):
        row=[]
        for j in range(1,i+1):
            row.append(str(a))
            a,b=b,a+b
        pattern.append(''.join(row))
    return pattern
def main():
    while True:
        try:
            n=int(input("Enter a positive integer N: "))
            pattern=fibonacci_pattern(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    print("Fibonacci Pattern:")
    for line in pattern:
        print(line)
def test_cases():
    assert fibonacci_pattern(3) == ['1', '1' '2', '3' '5' '8']
    assert fibonacci_pattern(1) == ['1']
    assert fibonacci_pattern(5) == ['1', '1' '2', '3' '5' '8', '13' '21' '34' '55', '89' '144' '233' '377' '610']

    try:
        fibonacci_pattern(0)
        assert False
    except ValueError:
        pass

    try:
        fibonacci_pattern(-3)
        assert False
    except ValueError:
        pass

    try:
        fibonacci_pattern(4.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")
if __name__ == "__main__":
    test_cases()
    main()