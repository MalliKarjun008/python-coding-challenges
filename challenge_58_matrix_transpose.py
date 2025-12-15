def transpose_matrix(matrix):
    if not isinstance(matrix,list):
        raise ValueError("Input must be a list of lists")
    if not matrix:
        return []
    transposed=[]
    rows=len(matrix)
    cols=len(matrix[0])
    for j in range(cols):
        row=[]
        for i in range(rows):
            if not isinstance(matrix[i],list):
                raise ValueError("Input must be a list of lists")
            if len(matrix[i])!=cols:
                raise ValueError("All rows must have the same number of columns")
            if not isinstance(matrix[i][j],int):
                raise ValueError("Matrix elements must be integers")
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed
def main():
    while True:
        try:
            rows=int(input("Enter number of rows: "))
            cols=int(input("Enter number of columns: "))
            if rows<0 or cols<0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter non-negative integers.")
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            while True:
                try:
                    row.append(int(input(f"Enter element [{i+1}][{j+1}]: ")))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        matrix.append(row)
    transposed=transpose_matrix(matrix)
    print("Matrix befor trsnapose")
    for row in matrix:
        print(row)
    print("Transposed Matrix:")
    for row in transposed:
        print(row)      
def test_cases():   
    assert transpose_matrix([[1,2,3],[4,5,6]])==[[1,4],[2,5],[3,6]]
    assert transpose_matrix([[1]])==[[1]]
    assert transpose_matrix([])==[]
    try:
        transpose_matrix("123")
        assert False
    except ValueError:
        pass
    try:
        transpose_matrix([[1,2],[3]])
        assert False
    except ValueError:
        pass
    try:
        transpose_matrix([[1,"a"]])
        assert False
    except ValueError:
        pass
    print("All test cases passed!")

if __name__=="__main__":
    test_cases()
    main()