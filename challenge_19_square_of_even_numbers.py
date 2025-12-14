def square_of_even_numbers(n):
    if not isinstance(n,int) or n<2:
        raise ValueError('N must be a greater than 1.')
    return [i*i for i in range(2,n+1) if i%2==0]
def main():
    while True:
        try:
            n=int(input("Enter N (greater than 1): "))
            series=square_of_even_numbers(n)
            break
        except ValueError:
            print("Invalid input. Please enter an integer greater than 1.")
    print("Square of even numbers from 2 to",n,":",series)  
def test_cases():   
    assert square_of_even_numbers(10) == [4, 16, 36, 64, 100]
    assert square_of_even_numbers(2) == [4]
    assert square_of_even_numbers(5) == [4, 16]

    try:
        square_of_even_numbers(1)
        assert False
    except ValueError:
        pass

    try:
        square_of_even_numbers(-4)
        assert False
    except ValueError:
        pass

    try:
        square_of_even_numbers(3.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!") 
if __name__ == "__main__":
    test_cases()
    main()