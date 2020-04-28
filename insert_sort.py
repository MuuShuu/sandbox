from decor import print_func


@print_func
def insert_sort(a: list = []):
    for i in range(1, len(a)):
        insert_num = a[i]
        j = i - 1
        while a[j] > insert_num and j >= 0:
            a[j + 1] = a[j]
            j -= 1
            a[j + 1] = insert_num
    return a
