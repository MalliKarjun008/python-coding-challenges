def squares_series(n):
    if not isinstance(n,int) or n<=0:
        raise ValueError("Input must be a positive integer.")
    series=[]
    for i in range(1,n+1):
        if i*i<=n:
            series.append(i*i)
        else:
            break
    return series
def main():
    while True:
        try:
            n=int(input("Enter a positive integer N: "))
            series=squares_series(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    print("Squares series up to",n,":",series)  

def test_cases():
    assert squares_series(20) == [1, 4, 9, 16]
    assert squares_series(1) == [1]
    assert squares_series(30) == [1, 4, 9, 16, 25]

    try:
        squares_series(0)
        assert False
    except ValueError:
        pass

    try:
        squares_series(-7)
        assert False
    except ValueError:
        pass

    try:
        squares_series(5.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")
    
if __name__ == "__main__":
    test_cases()
    main()