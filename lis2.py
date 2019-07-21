def binary_search(arr,hkey):
	start = 0 
	end = len(arr) - 1
	while start <= end:
		mid = (end + start) / 2 
		if arr[mid] > hkey:
			end = mid - 1
		if arr[mid] < hkey:
			start = mid + 1
		if arr[mid] == hkey:
			return(-1)
	if arr[0] > hkey:
		return(-2)
	elif arr[-1] < hkey:
		return(-3)
	return(start)

#print(binary_search([1,3,7,8],2))
def my_LIS2(A):
	n = len(A)
	LIS = [[]]
	LIS[0].append(A[0])

	List_Of_Last_Num = []
	List_Of_Last_Num.append(A[0])

	for j in range(1,n):

		pos = binary_search(List_Of_Last_Num,A[j])

		if pos == -1:
			continue
		elif pos == -2:
			LIS[0] = A[j]
			List_Of_Last_Num[0] = A[j]
		elif pos == -3:
			LIS.append( LIS[-1][:])
			LIS[-1].append(A[j])
			List_Of_Last_Num.append(A[j])
		else:
			LIS[pos][-1] = A[j]
			List_Of_Last_Num[pos] = A[j]


	return(LIS[-1])


#print(my_LIS2([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]))

print(my_LIS2([1,8,3,7,5,6,9]))

