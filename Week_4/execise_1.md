## for loops and range function

#### Play with for loop

    for i in [1, 2, 3, 4]:
        print("i =", i)

#### Play with for loop and range (identify the difference from the above script)

    for i in range(4):
        print("i =", i)

#### A script to find the sum of first 10 natural numbers.

    ...
    for i in range(10):
        ...
    
    print("sum of first 10 natural numbers is", ...)

Expected output:

    The sum of first 10 natural number is : 55

Bonus:

    The first 10 natural number is : 1 2 3 4  6 7 8 9 10
    The Sum is : 55

#### A script to find the sum of n terms of natural numbers.

    n = ...
    ...
    for i in range(n):
        ...
    
    print("sum of first 10 natural numbers is", ...)


Expected output:

    The first 10 natural number is : 1 2 3 4  6 7
    The Sum is : 28

#### A script to display the multiplication table of given integer.

    integer = ...

    for i in range(integer):
        ...

Expected output:

    15 X 1 = 15
    ...
    ...
    15 X 10 = 150

#### A script to display the multiplication table vertically for 1 to n.

Expected output:

    n = 8

    1x1 = 1
    1x2 = 2
    1x3 = 3
    1x4 = 4
    1x5 = 5
    1x6 = 6
    1x7 = 7
    1x8 = 8
    ...
    10x1 = 10
    10x2 = 20
    10x3 = 30
    10x4 = 40
    10x5 = 50
    10x6 = 60
    10x7 = 70
    10x8 = 80