def check_score(stitch):
	f = set(stitch[0])
	s = set(stitch[1])
	a = len(f - s)
	b = len(s - f)
	c = len(f & s)
	return min(a, b, c)
	pass