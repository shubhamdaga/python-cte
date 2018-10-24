def words(s):
	word=0
	Lines=s.split("/n")
	for x in Lines:
		word+=len(x.split())
	return word