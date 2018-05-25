def binary_search(input_array, value):
    """Your code goes here."""
    first = 0
    last = len(input_array) - 1
    while first <= last:
        mid_point = (first + last) / 2
        if input_array[mid_point] == value:
            return mid_point
        elif input_array[mid_point] <= value:
            first = mid_point + 1
        else:
            last = mid_point - 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)