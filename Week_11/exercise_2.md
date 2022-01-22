## Function

#### Function definition

    def function_name(arguments):
        #   do something here

        #   send result back to caller
        return
    

    #   call function
    function_name(arguments)


#### Function arguments vs keyword arguments

    def function_name(a, b, c, d='1', e='2'):
        print(f'a={a}, b={b}, c={c}, d={d}, e={e}')

    
    function_name(1,2,3,4,5)
    function_name(1,2,3,4)
    function_name(1,2,3)
    
