

def bubble_sort(nums_array):

    len_nums_array = len(nums_array)

    for i in range(len_nums_array):
        flag = False

        for j in range(0, len_nums_array-i-1):
            if nums_array[j] > nums_array[j+1]:
                nums_array[j], nums_array[j+1] = nums_array[j+1], nums_array[j]
                flag = True

        if flag==False:
            break

    return nums_array


if __name__ == '__main__':
    nums_array = [64, 25, 12, 22, 11]

    print(bubble_sort(nums_array))
