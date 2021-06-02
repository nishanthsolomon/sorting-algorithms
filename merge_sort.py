

def merge_sort(nums_array):

    len_nums_array = len(nums_array)

    if len_nums_array > 1:

        mid = len_nums_array//2

        left_array = nums_array[:mid]
        right_array = nums_array[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                nums_array[k] = left_array[i]
                i += 1
            else:
                nums_array[k] = right_array[j]
                j += 1

            k += 1

        while i < len(left_array):
            nums_array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            nums_array[k] = right_array[j]
            j += 1
            k += 1


if __name__ == '__main__':
    nums_array = [64, 25, 12, 22, 11]

    merge_sort(nums_array)

    print(nums_array)
