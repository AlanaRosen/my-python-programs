def bubble_sort(alist):
    is_sorted = False
    while is_sorted == False:
        num_swaps = 0 
        for each in range(len(alist) - 1):
            a = alist[each]
            b = alist[each + 1]
            if a > b:
                alist[each] = b
                alist[each + 1] = a
                num_swaps = num_swaps + 1
        if num_swaps == 0:
            is_sorted = True
    return alist