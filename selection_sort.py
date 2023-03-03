
def selection_sort(array):
    for i in range(len(array)):
        minimum_index = i
        for n in range(i + 1, len(array)):
            if array[n] < array[minimum_index]:
                minimum_index = n
        array[i], array[minimum_index] = array[minimum_index], array[i]
    return array


if __name__ == "__main__":
    array = [1,3, 2,5,6,34,2]
    array = selection_sort(array)
    print(array)