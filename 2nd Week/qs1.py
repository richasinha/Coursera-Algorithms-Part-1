def QS(arry):
	less = []
	grt = []
	equal = []
	pivot = arry[0]
	if (len(arry) > 1):
		for x in arry:
			if x > pivot:
				grt.append(x)
			elif x < pivot:
				less.append(x)
			else:
				equal.append(x)

		return QS(less) + equal + QS(grt)
	else:
		return arry


myList = [23,1,22,56,11,2,90,12]
print QS(myList)
