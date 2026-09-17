# Text analyzer Tool 

print("===Welcome to Text Analyzer===")

# Take text from user
user_text = input ("Enter any sentence or paragraph: ")

# Calculate Lengh (characters) and word count 
char_count = len(user_text)
words_list = user_text . split()
word_count = len(words_list)

# Print results 
print ("\n--- Analysis Results ---')
Print ("Total characters (with spaces):", char_count)
print ("Total words:", word_count)
