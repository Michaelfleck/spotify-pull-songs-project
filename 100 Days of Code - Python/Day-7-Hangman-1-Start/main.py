import random

#Step 1

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# for i in word_list:

# alternate way to do problem
# chosen_word = random.choice(word_list)

random_index = random.randint(0,len(word_list)-1)

chosen_word = word_list[random_index]

# print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

print(guess)
print("--------")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for i in chosen_word:
    if i == guess:
        print("found letter: " + i)
    else:
        print("wrong")
