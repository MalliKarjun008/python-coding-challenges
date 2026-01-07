def fib(n):
    series=[]
    current=5
    a=1,b=1
    count=0
    while current<=991:
        series.append(current)
        if count<2:
            current+=1
            count+=1
        else:   
            a,b=b,a+b
            current+=b
    return series

