def alternating_square_pattern(n):
    if not isinstance(n,int) or n<=0:
        raise ValueError("Input must be a positive integer")
    pattern=[]
    sign=1
    num=1
    for i in range(1,n+1):
        row=[]
        for j in range(i):
            row.append(str(num*num*sign))
            num+=1
            sign*=-1
        pattern.append(' '.join(row))
    return pattern
def main():
    while True:
        try:
            n=int(input("Enter a positive integer N: "))
            pattern=alternating_square_pattern(n)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    print("Alternating Square Pattern:")
    for line in pattern:
        print(line)
def test_cases():
    assert alternating_square_pattern(3) == ['1', '-4 9', '-16 25 -36']
    assert alternating_square_pattern(1) == ['1']
    assert alternating_square_pattern(5) == ['1', '-4 9', '-16 25 -36', '49 -64 81 -100', '121 -144 169 -196 225']

    try:
        alternating_square_pattern(0)
        assert False
    except ValueError:
        pass

    try:
        alternating_square_pattern(-3)
        assert False
    except ValueError:
        pass

    try:
        alternating_square_pattern(4.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!")
if __name__ == "__main__":
    test_cases()
    main()