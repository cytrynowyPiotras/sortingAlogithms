def bubble_sort(list):
    number=1
    while(number < len(list) - 1):
        for place in range(0, len(list) - 1):
            if (list[place] > list[place + 1]):
                list[place], list[place + 1] = list[place + 1], list[place]
        number += 1
    return list

if __name__ == "__main__":
    array = [1,3,5,6,34,2]
    array = bubble_sort(array)
    print(array)