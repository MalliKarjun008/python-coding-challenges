def genearte_series(n):
    if not isinstance(n,int) or n<=0:
        raise ValueError("Input must be a positive integer.")
    return list(range(1,n+1))
def main():
    while True:
        try:
            n=int(input("enter a psositive integer:"))
            series=genearte_series(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    print("Series from 1 to",n,":",series)      

def test_cases():
    assert genearte_series(5) == [1, 2, 3, 4, 5]
    assert genearte_series(1) == [1]
    assert genearte_series(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    try:
        genearte_series(0)
        assert False
    except ValueError:
        pass

    try:
        genearte_series(-5)
        assert False
    except ValueError:
        pass

    try:
        genearte_series(3.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")

if __name__ == "__main__":
     test_cases()
     main()  