def sum_array(array):
    '''
    Return sum of all items in array

    Args:
        Array (array): a list or array containing numerical values

    Returns:
        Numeric value: the sum of all elements in the array

    Examples:
        >>> sum_array([8, 3, 2, 7, 4])
        24
        >>> sum_array([5, 7, 8, 8, 6, 3, 4])
        41
        >>> sum_array([25, 14, 2, 3, 5])
        49
    '''

    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):
    '''
    Return nth term in fibonacci sequence

    Args:
        Number (n): a numerical value representing the position of the fibonacci sequence

    Returns:
        Numeric value: a numerical value representing the nth position of the fibonacci sequence

    Examples:
        >>> fibonacci(8)
        21
        >>> fibonacci(10)
        55
        >>> fibonacci(5)
        5
    '''

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    '''
    Return n!

    Args:
        Number (n): a number to calculate the factorial for

    Returns:
        Numeric value: a numerical value representing the factorial of the number n

    Examples:
        >>> factorial(4)
        24
        >>> factorial(8)
        40320
        >>> factorial(3)
        6
    '''

    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def reverse(word):
    '''
    Return word in reverse

    Args:
        String (word): a string that will be reversed

    Returns:
        String: a reversed string based on the input string

    Examples:
        >>> reverse('apple')
        'elppa'
        >>> reverse('test')
        'tset'
        >>> reverse('peanut')
        'tunaep'
    '''

    if len(word) == 1:
        return word[0]
    else:
        return word[-1] + reverse(word[:-1])
