def tree_add(arr, value):
	if (value[0] == None):
		return
	left, right = 0, len(arr)
	while left < right:
		mid = (left + right)//2
		if arr[mid][0] < value[0]:
			left = mid + 1
		else:
			right = mid
	arr.insert(left, value)

			