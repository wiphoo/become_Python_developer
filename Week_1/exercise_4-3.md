## Python as calculator and variable number, string, and list

#### List operations

1. create a list of number 1, 2, 3, 4, 5.
2. add number 6 at the end of list No.1
3. add number 0 at the first of list No.0
4. create a new list from list No.1 with elements from index 2 to 4.
5. copy a list No.4
6. count number of element in list No.5


##### Create empty list.
    >>> []
    >>> list()

##### Create a list with elements.
    >>> [1, 2, 3, 4]
    >>> list()

    >>> x = [1, 2, 3, 4]

##### Add a element at the end of the list.
    >>> x = [1, 2, 3, 4]
    >>> x.append(5)
    >>> print(x)

##### Add a element at x position of the list.
    >>> x = [1, 2, 3, 4]
    >>> x.insert(0, 0)
    >>> print(x)

##### Access element in the list.
    >>> [1, 2, 3, 4][0]
    
    >>> [1, 2, 3, 4][-1]

    >>> [1, 2, 3, 4][100]   # invalid index

##### Slice the element in the list.
    >>> [1, 2, 3, 4][:]
    >>> [1, 2, 3, 4][-1]
    >>> [1, 2, 3, 4][0:1]
    >>> [1, 2, 3, 4][0:3]
    >>> [1, 2, 3, 4][-3:-2]
    >>> [1, 2, 3, 4][-3:]

##### Count element in the list.

    >>> len([1, 2, 3, 4])
