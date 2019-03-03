#
# Solution:	join pairs of vertical pics into horizontal right away,
# 			then sort all pics by number of tags descending. Take 
#			the first pic in the list, and check next N (e.g., 1000)
#			pics in the list for maximum score. Pop the selected pics
#			(actuallym only the first in this implementation) and
#			repeat until the pic list is empty. 
#			TODO: it's not very efficient, needs optimisation
#
import operator
import sys
from tqdm import *


# def search_next_v(start, pics):
# 	for pic in pics:
# 		if pics[pic][0] and pic != start:
# 			return pic
# 	raise ValueError('Cant find a second vertical pic')
# 	pass


def read_input(file):
	csv = open(file, 'r').readlines()
	n = [val for val in csv[0].strip()]
	pics = [row.strip().split(' ') for row in csv[1:]]
	# dic = {i : pics[i] for i in range(len(pics))}
	return (n, pics)


def write_output(filename, pics):
	with open(filename, 'w') as f:
		f.write(str(len(pics))+"\n")
		for pic in pics:
			line = " ".join(str(i) for i in pic)
			f.write(line+"\n")


def join_verticals(pics):
	vertical = []
	vertical_joined = []
	horizontal = []
	i = 0
	for pic in pics:
		if pic[0] == 'V':
			line = [i]
			# line.extend(i)
			line.extend(pic)
			vertical.append(line)
		else:
			line = []
			line.extend([[i], 'H', int(pic[1])])
			line.extend(pic[2:])
			horizontal.append(line)
		i = i + 1

	for v in range(0, len(vertical)-1, 2):
		u = set(vertical[v][3:]) | set(vertical[v+1][3:])
		ids = [vertical[v][0], vertical[v+1][0]]
		line = []
		line.extend([ids, 'HJ', len(u)])
		line.extend(list(u))
		vertical_joined.append(line)

	# print(horizontal)
	# print(vertical_joined)
	joined = []
	joined.extend(horizontal)
	joined.extend(vertical_joined)
	# print(joined)
	# sys.exit()

	return joined


def sort_pics(pics):
	return sorted(pics, key = operator.itemgetter(2), reverse = True)


def get_pic(pics):
	if len(pics) > 0:
		return next(iter(pics))
	else:
		return -1


def get_score(f, s):
	a = set(f[3:])
	b = set(s[3:])
	# sys.exit()
	return min(len(a-b), len(b-a), len(a&b))


def main():
	[n_pics, pics_list] = read_input(sys.argv[1])
	pics_list = join_verticals(pics_list)

	pics_list = sort_pics(pics_list)
	pics = pics_list

	# print(pics)

	total_score = 0
	n_slides = 0
	last = 0
	slideshow = []
	progress = tqdm(total = len(pics))
	while len(pics) > 0:
		first = pics[last]
		n_slides = n_slides + 1
		pics.pop(last)

		m = 0
		pos = 0
		for i in range(0, min(1000, len(pics))):
			second = pics[i]
			score = get_score(first, second)
			if score > m:
				m = score
				pos = i

		total_score = total_score + m
		last = pos;

		slideshow.append(first[0])
		progress.update(1)

	# print(slideshow)
	write_output(sys.argv[1]+".out", slideshow)
	print(total_score)



if __name__ == '__main__':
	main()