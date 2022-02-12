##### A script to determine the highest common factor.

Input: 8 12 

Expected Output: 4

##### A script to determine the lowest common multiple.

Input: 8 12 

Expected Output: 24


##### A script to determine the greatest common divisor with Euclidean algorithm.

    
    function gcd(a, b)
    while a ≠ b 
        if a > b
            a := a − b
        else
            b := b − a
    return a

Input: 8 12

Expected Output: 4
