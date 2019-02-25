def vowels(list_string1):
	list_2 = list_string1.lower().split(' ')
	empty_string = " "
	for wordds in list_2: 
		empty_string+=wordds
	vowels = ["a", "e", "i", "o", "u"]
	strint_vowels = [vowel for vowel in vowels if vowel in empty_string]
	string_for_vowels = " "
	for vowel in strint_vowels:
		string_for_vowels += vowel
	duplicates = []
	duplicate = [duplicates.append(letter) for letter in empty_string if empty_string.count(letter) > 1 and letter not in duplicates]
	result = (string_for_vowels, len(duplicates))
	return result
print(vowels("This is my name Benna"))
