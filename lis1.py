def my_LIS(A):
	n = len(A)
	LIS = [[] for j in range(n)]
	LIS[0].append(A[0])

	for j in range(1,n):
		flag = []
		for k in range(j):
			if LIS[k][-1] < A[j]:
				flag.append(k)
		

		max_length_end_at_i = 0
		pos_max = -1
		for q in flag:
			if len(LIS[q]) + 1 > max_length_end_at_i:
				max_length_end_at_i = len(LIS[q])+1
				pos_max = q

		if len(flag) > 0:
			LIS[j] = LIS[pos_max][:]
			LIS[j].append(A[j])
		else:
			LIS[j].append(A[j])


	max_length = 0
	for m in range(n):
		max_length = max(max_length,len(LIS[m]))

	for p in range(n):
		if len(LIS[p]) == max_length:
			return(LIS[p])

print(my_LIS([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]))

