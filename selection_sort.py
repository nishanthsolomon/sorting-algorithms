

def selection_sort(nums_array):

    len_nums_array = len(nums_array)

    for i in range(len_nums_array):
        min_index = i

        for j in range(i+1, len_nums_array):
            if nums_array[j] < nums_array[min_index]:
                min_index = j

        nums_array[i], nums_array[min_index] = nums_array[min_index], nums_array[i]

    return nums_array


if __name__ == '__main__':
    nums_array = [64, 25, 12, 22, 11]

    print(selection_sort(nums_array))
