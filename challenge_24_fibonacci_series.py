def fib(n):
    if not isinstance(n,int) or n<=0:
        raise ValueError('Input must be a positive integer.')
    a,b=1,1
    series=[]
    while a<=n:
        series.append(a)
        a,b=b,a+b   
    return series
def main():
    while True:
        try:
            n=int(input("Enter a positive integer N: "))
            series=fib(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    print("Fibonacci series up to",n,":",series)
def test_cases():   
    assert fib(21) == [1, 1, 2, 3, 5, 8, 13, 21]
    assert fib(1) == [1, 1]
    assert fib(10) == [1, 1, 2, 3, 5, 8]

    try:
        fib(0)
        assert False
    except ValueError:
        pass

    try:
        fib(-4)
        assert False
    except ValueError:
        pass

    try:
        fib(6.7)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")
if __name__ == "__main__":
    test_cases()
    main()