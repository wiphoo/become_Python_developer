## IF

#### Play with if statement

An if ... elif ... elif ... else sequence is a substitute for the switch or case or default statement found in other language.

    x = 10
    if x < 0:
        print("negative value")
    elif x == 0:
        print("zero")
    elif x == 1:
        print("single")
    else:
        print("more")


#### Play with inner-if statement

    x = 10
    if x < 0:
        if x % 2 == 0:
            print("negative even")
        else:
            print("negative odd")
    elif x == 0:
        print("zero")
    else:
        if x % 2 == 0:
            print("positive even")
        else:
            print("positive odd")

#### Only a single if statement

    x = 10
    if x < 0:
        print("negative value")


#### Only if..else statement

    if x < 0:
        print("negative value")
    else:
        print("zero or positive")