def bubble_sort(items):
    '''
    Return array of items, sorted in ascending order based on the bubble sort algorithm

    Args:
        list (items): a list of items of any type

    Returns:
        list: a sorted list of the items

    Examples:
        >>> bubble_sort(['apple', 'pear', 'orange', 'pineapple', 'strawberry', 'lemon'])
        ['apple', 'lemon', 'orange', 'pear', 'pineapple', 'strawberry']
        >>> bubble_sort(['horse', 'cat', 'aardvark', 'dog', 'fish', 'bird'])
        ['aardvark', 'bird', 'cat', 'dog', 'fish', 'horse']
        >>> bubble_sort(['Ford', 'Mitsubishi', 'BMW', 'VW'])
        ['BMW', 'Ford', 'Mitsubishi', 'VW']
    '''

    #Loops over the list twice and compares an element to the one next to it where it will then swop positions if needed 
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items


def merge_sort(items):
    '''
    Return array of items, sorted in ascending order based on the merge sort algorithm

    Args:
        list (items): a list of items of any type

    Returns:
        list: a sorted list of the items

    Examples:
        >>> bubble_sort(['apple', 'pear', 'orange', 'pineapple', 'strawberry', 'lemon'])
        ['apple', 'lemon', 'orange', 'pear', 'pineapple', 'strawberry']
        >>> bubble_sort(['horse', 'cat', 'aardvark', 'dog', 'fish', 'bird'])
        ['aardvark', 'bird', 'cat', 'dog', 'fish', 'horse']
        >>> bubble_sort(['Ford', 'Mitsubishi', 'BMW', 'VW'])
        ['BMW', 'Ford', 'Mitsubishi', 'VW']
    '''

    if len(items) <= 1:
        #Returns the single element of the list if the list only has one element
        return items
    else:
        #Splits the list in two lists and recursively calls merge_sort to sort the two split lists
        list1 = merge_sort(items[:len(items)//2])
        list2 = merge_sort(items[len(items)//2:])

        sort_list = []

        #Compares the first elements of both lists and appends the smallest of the elements to sort_list
        while list1 and list2:
            if list1[0] < list2[0]:
                sort_list.append(list1.pop(0))
            else:
                sort_list.append(list2.pop(0))

        #Extends sort_list with the remaining elements of the split lists
        sort_list.extend(list1)
        sort_list.extend(list2)

        return sort_list


def quick_sort(items):

    '''
    Return array of items, sorted in ascending order based on the quick sort algorithm

    Args:
        list (items): a list of items of any type

    Returns:
        list: a sorted list of the items

    Examples:
        >>> bubble_sort(['apple', 'pear', 'orange', 'pineapple', 'strawberry', 'lemon'])
        ['apple', 'lemon', 'orange', 'pear', 'pineapple', 'strawberry']
        >>> bubble_sort(['horse', 'cat', 'aardvark', 'dog', 'fish', 'bird'])
        ['aardvark', 'bird', 'cat', 'dog', 'fish', 'horse']
        >>> bubble_sort(['Ford', 'Mitsubishi', 'BMW', 'VW'])
        ['BMW', 'Ford', 'Mitsubishi', 'VW']
    '''

    #Return the single element in the list if there is only one
    if len(items) <= 1:
        return items

    #Choose the middle element as a pivot point
    pivot = items[len(items)//2]

    #Use a list comprehension to get elements to the left, right or middle list depending if the element is smaller, bigger or equal to the pivot
    left = [i for i in items if i < pivot]
    middle = [i for i in items if i == pivot]
    right = [i for i in items if i > pivot]

    #Recursively call quick_sort on the left and right lists
    left = quick_sort(left)
    right = quick_sort(right)

    return left + middle + right
