

def search_next_v(start, pics):
	for pic in pics:
		if pics[pic][0] and pic != start:
			return pic
	raise ValueError('Cant find a second vertical pic')
	pass


def check_score(stitch):
	
	pass


def main():
	[n_pics, pics] = read_input(sys.argv[1])
	print(pics)

	while len(pics) > 0:
		stitch = [[], []]
		i = 0
		j = 0
		for pic in pics:
			stitch[i].append(pic)
			if pics[pic][0]:
				stitch[i].append(search_next_v(pic, pics))
			i = i + 1

		check_score(stitch)
		for i in stitch:
			for j in i:
				pics.pop(j)



if __name__ == '__main__':
	main()