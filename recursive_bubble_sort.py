

def recursive_bubble_sort(nums_array):

    len_nums_array = len(nums_array)

    for i in range(len_nums_array-1, 0, -1):
        print(nums_array)
        for j in range(0, i):
            if nums_array[j] > nums_array[j+1]:
                nums_array[j], nums_array[j+1] = nums_array[j+1], nums_array[j]

        

    return nums_array


if __name__ == '__main__':
    nums_array = [64, 25, 12, 22, 11]

    print(recursive_bubble_sort(nums_array))
