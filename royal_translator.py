cases = int(input())

for i in range(0, cases):
		
	og = input()

	translate_pairs = int(input())

	translation_pairs = []
	for i in range(0, translate_pairs):
		curr_translate = input()
		translation_pairs.append(curr_translate)

	# Solve

	og_words = og.split(" ")

	translation_map = {}
	for i in range(0, translate_pairs):
		pair = (translation_pairs[i]).split(" ")

		translation_map[pair[0]] = pair[1]

	# print(og_words)
	# print(translation_map)

	new_words = og_words.copy()

	for i in range(0, len(og_words)):
		word = og_words[i]
		if word in translation_map:
			new_words[i] = translation_map[word]

	print(" ".join(new_words))