from edsa_packages import recursion, sorting


#Recursion tests
def test_sum_array():
    '''
    Make sure sum_array works
    '''
    assert recursion.sum_array([8, 3, 2, 7, 4]) == 24, 'incorrect'
    assert recursion.sum_array([5, 7, 8, 8, 6, 3, 4]) == 41, 'incorrect'
    assert recursion.sum_array([25, 14, 2, 3, 5]) == 49, 'incorrect'

def test_fibonacci():
    '''
    Make sure fibonacci works
    '''
    assert recursion.fibonacci(8) == 22, 'incorrect'
    assert recursion.fibonacci(10) == 55, 'incorrect'
    assert recursion.fibonacci(5) == 5, 'incorrect'

def test_factorial():
    '''
    Make sure factorial works
    '''
    assert recursion.factorial(4) == 24, 'incorrect'
    assert recursion.factorial(8) == 40320, 'incorrect'
    assert recursion.factorial(3) == 6, 'incorrect'

def test_reverse():
    '''
    Make sure reverse works
    '''
    assert recursion.reverse('apple') == 'elppa', 'incorrect'
    assert recursion.reverse('test') == 'tset', 'incorrect'
    assert recursion.reverse('peanut') == 'tunaep', 'incorrect'


#Sorting tests
def test_bubble_sort():
    '''
    Make sure bubble_sort works
    '''
    assert sorting.bubble_sort(['apple', 'pear', 'orange', 'pineapple', 'strawberry', 'lemon']) == ['apple', 'lemon', 'orange', 'pear', 'pineapple', 'strawberry'], 'incorrect'
    assert sorting.bubble_sort(['horse', 'cat', 'aardvark', 'dog', 'fish', 'bird']) == ['aardvark', 'bird', 'cat', 'dog', 'fish', 'horse'], 'incorrect'
    assert sorting.bubble_sort(['Ford', 'Mitsubishi', 'BMW', 'VW']) == ['BMW', 'Ford', 'Mitsubishi', 'VW'], 'incorrect'

def test_merge_sort():
    '''
    Make sure merge_sort works
    '''
    assert sorting.merge_sort(['apple', 'pear', 'orange', 'pineapple', 'strawberry', 'lemon']) == ['apple', 'lemon', 'orange', 'pear', 'pineapple', 'strawberry'], 'incorrect'
    assert sorting.merge_sort(['horse', 'cat', 'aardvark', 'dog', 'fish', 'bird']) == ['aardvark', 'bird', 'cat', 'dog', 'fish', 'horse'], 'incorrect'
    assert sorting.merge_sort(['Ford', 'Mitsubishi', 'BMW', 'VW']) == ['BMW', 'Ford', 'Mitsubishi', 'VW'], 'incorrect'

def test_quick_sort():
    '''
    Make sure quick_sort works
    '''
    assert sorting.quick_sort(['apple', 'pear', 'orange', 'pineapple', 'strawberry', 'lemon']) == ['apple', 'lemon', 'orange', 'pear', 'pineapple', 'strawberry'], 'incorrect'
    assert sorting.quick_sort(['horse', 'cat', 'aardvark', 'dog', 'fish', 'bird']) == ['aardvark', 'bird', 'cat', 'dog', 'fish', 'horse'], 'incorrect'
    assert sorting.quick_sort(['Ford', 'Mitsubishi', 'BMW', 'VW']) == ['BMW', 'Ford', 'Mitsubishi', 'VW'], 'incorrect'
