# Step 1: Find Peaks


test_cases =1

# num_heights = 5
# num_heights = 7

str_heights = "6 3 5 2 7".split()
# str_heights = "3 8 5 4 1 20 2".split()
# str_heights = "2 5 3 7 1 2".split()
# str_heights = "2 5 7 13".split()

heights = []
for s in str_heights:
	heights.append(int(s))

print(heights)


peaks = []

heights_len = len(heights)
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



print(peaks)

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
	print("Befores: " , befores)

	# Afters
	afters = []
	if peaknum != len(peaks):
		next = len(heights) if peaknum == len(peaks) - 1 else peaks[peaknum + 1]
		for i in range(peak + 1, next):
			
			afters.append(heights[i])
	print("Afters: " , afters)
	print("\n")

	total = len(befores) + len(afters) + 1

	if (len(befores) + 1 )== len(heights) or (len(afters) + 1) == len(heights):
		total = 0
	totals.append(total)

print(max(totals))

# diffs = []
# for i in range(0, len(mountains) - 1):
# 	diffs.append(abs(mountains[i] - mountains[i + 1]))

# print("diffs: ", diffs)

# # Edge cases
# # First mountain to 'before' index aka zero
# diffs.append( abs(int(mountains[0]) - 0) )

# # Last mountain to last index
# diffs.append( abs( int(mountains[-1]) - (len(heights) - 1) ))

# print("diffs: ", diffs)
# -----------------------------------------------
# # Edge Cases
# print("Mountains before: ", mountains)
# # if (mountains[0] != 1):
# # 	mountains.insert(0, 0)

# if (mountains[-1] != heights_len - 1):
# 	mountains.append(heights_len - 1)


# print("Mountains after: ", mountains)

# mountains_val = {}
# for m in mountains:
# 	mountains_val[heights[m]] = m


# smallest = min(mountains)
# largest  = max(mountains)
# # smallest = mountains_val[min(dict.keys(mountains_val))]
# # largest  = mountains_val[max(dict.keys(mountains_val))]

# print("Smallest: " , smallest, " Largest: ", largest, " Ass: ", dict.keys(mountains_val))

# diff = abs(largest - smallest) - 1

# if (mountains[0] != 0):
# 	diff += abs(smallest - 0) - 1

# print(diff)