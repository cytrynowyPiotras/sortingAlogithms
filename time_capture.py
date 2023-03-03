import time
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from quicksort import quick_sort
from selection_sort import selection_sort
import gc
from matplotlib import pyplot as plt
import sys


def main():
	sys.setrecursionlimit(30000)

	with open('pan-tadeusz-unix.txt', 'r', encoding="utf8") as f:
		tekst = f.read()
		tekst.strip()
		tadeusz_list = tekst.split()

	number_of_words = [700, 1500, 2000, 5000, 10000, 15000]
	bubble_sort_times = []
	merge_sort_times = []
	quick_sort_times = []
	selection_sort_times = []

	for number in number_of_words:
		gc_old = gc.isenabled()
		gc.disable()
		start = time.process_time()
		bubble_sort(tadeusz_list[:number])
		stop = time.process_time()
		if gc_old:
			gc.enable()
		total_time = stop - start
		bubble_sort_times.append(total_time)

	for number in number_of_words:
		gc_old = gc.isenabled()
		gc.disable()
		start = time.process_time()
		merge_sort(tadeusz_list[:number])
		stop = time.process_time()
		if gc_old:
			gc.enable()
		total_time = stop - start
		merge_sort_times.append(total_time)

	for number in number_of_words:
		gc_old = gc.isenabled()
		gc.disable()
		start = time.process_time()
		selection_sort(tadeusz_list[:number])
		stop = time.process_time()
		if gc_old:
			gc.enable()
		total_time = stop - start
		selection_sort_times.append(total_time)

	for number in number_of_words:
		gc_old = gc.isenabled()
		gc.disable()
		start = time.process_time()
		quick_sort(tadeusz_list[:number])
		stop = time.process_time()
		if gc_old:
			gc.enable()
		total_time = stop - start
		quick_sort_times.append(total_time)

	plt.plot(number_of_words, bubble_sort_times, label="Bubble sort")
	plt.plot(number_of_words, merge_sort_times, label="Merge sort")
	plt.plot(number_of_words, selection_sort_times, label="Selection sort")
	plt.plot(number_of_words, quick_sort_times, label="Quick sort")
	plt.xlabel("Words")
	plt.ylabel("Time")
	plt.legend()
	plt.savefig("results.png")
	plt.show()

if __name__ == "__main__":
    main()
