def generate_star_pattern(n):
    if not isinstance(n,int) or n<=0:
        raise ValueError("input must be a positive integer.")
    pattern =[]
    for _ in range(n):
        pattern.append('*'*n)
    return pattern
def main():
    while True:
        try:
            n=int(input("Enter a positive integer N: "))
            pattern=generate_star_pattern(n)
            break   
        except ValueError:
            print("Invalid input. Please enter a positive integer.")    
    print("Star Pattern:")
    for line in pattern:
        print(line) 
def test_cases():   
    assert generate_star_pattern(3) == ['***', '***', '***']
    assert generate_star_pattern(1) == ['*']
    assert generate_star_pattern(5) == ['*****', '*****', '*****', '*****', '*****']

    try:
        generate_star_pattern(0)
        assert False
    except ValueError:
        pass

    try:
        generate_star_pattern(-3)
        assert False
    except ValueError:
        pass

    try:
        generate_star_pattern(4.5)
        assert False
    except ValueError:
        pass

    print("All test cases passed!") 
if __name__ == "__main__":
    test_cases()
    main()