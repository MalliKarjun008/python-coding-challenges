def factorial_pattern(n):
    if not isinstance(n,int) or n<=0:
        raise ValueError("Input must be a positive integer")
    result=[]
    fact=1
    cur=0
    for i in range(1,n+1):
        row=[]
        for _ in range(i):
            if cur>0:
                fact*=cur
            row.append(str(fact))
            cur+=1
        result.append(' '.join(row))
    return result   
def main():
    while True:
        try:
            n=int(input("Enter a positive integer N: "))
            pattern=factorial_pattern(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    print("Factorial Pattern:")
    for line in pattern:
        print(line)
def test_cases():
    assert factorial_pattern(3) == ['1', '1 2', '6 24 120']
    assert factorial_pattern(1) == ['1']
    assert factorial_pattern(5) == ['1', '1 2', '6 24 120', '720 5040 40320 362880', '3628800 39916800 479001600 6227020800 87178291200']

    try:
        factorial_pattern(0)
        assert False
    except ValueError:
        pass

    try:
        factorial_pattern(-3)
        assert False
    except ValueError:
        pass

    try:
        factorial_pattern(4.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")
if __name__ == "__main__":
    test_cases()
    main()