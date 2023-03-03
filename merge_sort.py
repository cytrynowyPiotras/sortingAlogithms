def merge_sort(array):
    if len(array) > 1:
        middle = len(array)//2
        Left_side = array[:middle]
        Right_side = array[middle:]
        merge_sort(Left_side)
        merge_sort(Right_side)

        times_l = times_r = times_new = 0

        while times_l < len(Left_side) and times_r < len(Right_side):
            if Left_side[times_l] < Right_side[times_r]:
                array[times_new] = Left_side[times_l]
                times_l += 1
            else:
                array[times_new] = Right_side[times_r]
                times_r += 1
            times_new += 1

        while times_l < len(Left_side):
            array[times_new] = Left_side[times_l]
            times_l += 1
            times_new += 1

        while times_r < len(Right_side):
            array[times_new] = Right_side[times_r]
            times_r += 1
            times_new += 1

if __name__ == "__main__":
    array = [1,3,4 ,12,5,6,34,2]
    merge_sort(array)
    print(array)