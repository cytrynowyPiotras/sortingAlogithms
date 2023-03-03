def partition(list, left, right):
	i = (left-1)
	pivot = list[right]

	for j in range(left, right):

		if list[j] <= pivot:
			i = i+1
			list[i], list[j] = list[j], list[i]

	list[i+1], list[right] = list[right], list[i+1]
	return (i+1)

def decide(list, left, right):
	if len(list) == 1:
		return list
	if left < right:
		pi = partition(list, left, right)
		decide(list, left, pi-1)
		decide(list, pi+1, right)


def quick_sort(list):
	left = 0
	right = len(list) - 1
	decide(list, left, right)

if __name__ == "__main__":
    array = [1,3,5,6,34,2]
    quick_sort(array)
    print(array)