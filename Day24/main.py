#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names = []
with open("./Input/Names/invited_names.txt") as f:
    for line in f:
        line = line.rstrip("\n")
        names.append(line)


with open("./Input/Letters/starting_letter.txt") as f:
    raw_letter = f.read()

finished_letters = {}
for name in names:
    finished_letters[name] = raw_letter.replace("[name]", name)

for k, v in finished_letters.items():
    filename = f"letter_to_{k}"
    with open(f"./Output/ReadyToSend/{filename}.txt", "w") as f:
        f.write(v)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp