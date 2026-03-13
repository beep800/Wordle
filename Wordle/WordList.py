with open('Words2', 'r') as file:
    five_letter_words = [line.strip() for line in file if len(line.strip()) == 5 and line.strip().isalpha()]

with open('Words', 'r') as file:
    five_letter_words2 = [line.strip() for line in file if len(line.strip()) == 5 and line.strip().isalpha()]







