# Step 1: Find Peaks


test_cases = int(input())

for i in range(test_cases):
	num_heights = int(input())

	str_heights = input().split()
	# str_heights = "3 8 5 4 1 20 2".split()
	# str_heights = "2 5 3 7 1 2".split()
	# str_heights = "2 5 7 13".split()

	heights = []
	for s in str_heights:
		heights.append(int(s))

	# print(heights)


	peaks = []

	heights_len = num_heights
	for i in range(0, heights_len):
		c = heights[i]
		valid = True
		
		if (i != 0 and heights[i -1] > c):
			valid = False
			
		if (i != heights_len - 1 and heights[i + 1] > c):
			valid = False
		
		if (valid):
			# print("Mountain found (with index:) ", i )
			peaks.append(i)
		# print( "Index: " , i, " Val: " , c )



	# print(peaks)

	totals = [0]
	for peaknum in range(0, len(peaks)):
		peak = peaks[peaknum]
		copy = heights.copy()
		# Go left
		# print(peak , ": ")
		prev = 0 if peaknum == 0 else peaks[peaknum - 1] + 1

		# Befores
		prev_val = None
		befores = []
		for i in range(peak -1 , prev - 1, -1):
			val = heights[i]
			
			if prev_val == None:
				prev_val = val
				befores.append(val)
				continue
			if val > prev_val:
				# Dies
				break
			else:
				befores.append(val)

			prev_val = val
		# print("Befores: " , befores)

		# Afters
		afters = []
		if peaknum != len(peaks):
			next = num_heights if peaknum == len(peaks) - 1 else peaks[peaknum + 1]
			for i in range(peak + 1, next):
				
				afters.append(heights[i])
		# print("Afters: " , afters)
		# print("\n")

		total = len(befores) + len(afters) + 1

		if (len(befores) + 1 )== num_heights or (len(afters) + 1) == num_heights:
			total = 0
		totals.append(total)

	print(max(totals))
