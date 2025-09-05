### HANG MEN GAME
import random

# Step 1: list of 15 words
# rather you can use file (import OS) in this 
words = [
    "apple", "banana", "orange", "grape", "mango",
    "lemon", "cherry", "melon", "peach", "kiwi",
    "plum", "pear", "fig", "date", "papaya"
]

#step-2 generate 1 to 15 random number
rand_num=random.randint(1,15)
word=words[rand_num-1]
# print(word)

#step-3 randomly underline 4 latetrs
if len(word) < 4:
    underline=list(range(len(word))) #['apple']-[0,1,2,3,4,5]
else:
    #random.sample(itrable,k) k=unique element
    underline=random.sample(range(len(word)),4)
    
output = []
for i,c in enumerate(word):
    if i not in underline:
        output.append(c)
    else:
        output.append("_")
        
print(output)

#let user gause
chance = 10
while chance > 0 and "_" in output:
    guess = input(f"Guess a missing character (Remaining tries: {chance}): ").lower()
    
    if len(guess) !=1 or not guess.isalpha():
        print("enter a single letter")
        continue
    
    correct = False
    for idx in underline:
        if word[idx].lower() == guess and output[idx] == "_":
            output[idx] = word[idx]
            correct = True
            
    if correct:
        print("right guess")
    else:
        chance -=1
        print("wrong guess")
# final result
if "_" not in output:
    print("\n You completed the word:", word)
else:
    print("\n Out of tries! The word was:", word)



