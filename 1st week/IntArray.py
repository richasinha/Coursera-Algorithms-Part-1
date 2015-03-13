def Split(lst_arr):
	inv = 0
	if (len(lst_arr) == 1)
		return inv
	else
		mid = len(lst_arr)/2
		left,inv1 = Split(lst_arr[1:mid])
		right,inv2 = Split(lst_arr[mid+1:])
		merge(lst_arr)	

text_file = open("IntegerArray.txt")
lines = text_file.readlines()
print len(lines)
text_file.close()




#
text_file = open("IntegerArray.txt")
lines = text_file.readlines()
print len(lines)
text_file.close()
print mergesort(lines)#
