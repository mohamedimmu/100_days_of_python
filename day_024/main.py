# Project 24 - Mail Merge

PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, striped_name)
        print(new_letter)

        with open(f"Output/ReadyToSend/letter_for_{striped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)
