

def insertion_sort(nums_array):

    len_nums_array = len(nums_array)

    for i in range(1, len_nums_array):
        key = nums_array[i]

        j = i-1
        while j >= 0 and key < nums_array[j]:
            nums_array[j+1] = nums_array[j]
            j -= 1

        nums_array[j+1] = key

    return nums_array


if __name__ == '__main__':
    nums_array = [64, 25, 12, 22, 11]

    print(insertion_sort(nums_array))
