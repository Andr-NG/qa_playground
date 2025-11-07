lst = [1, 3, 5, 12, 34, 54, 57, 60, 63, 67, 70, 88, 99]


def binary(lst: list, search_item):
    start = 0
    finish = len(lst) - 1

    # every time we compare search_item with the value in the middle of the list
    # we shift the list bondaries based on the outcome
    # when start and finish are equal, then the cycle stops. No value found.
    while start <= finish:
        mid = (start + finish) // 2
        if search_item == lst[mid]:
            print(f"Search element {search_item} found in {lst} at lst[{mid}]")
            break
        elif search_item > lst[mid]:
            start = mid + 1
        elif search_item < lst[mid]:
            finish = mid - 1
    print(f"Search element {search_item} NOT found in {lst}")


binary(lst, 100)
