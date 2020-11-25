NAME = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.docx") as new_letter:
    contents = new_letter.read()
    for name in names:
        name_strip = name.strip()
        new_let = contents.replace(NAME, name_strip)
        with open(f"./Output/ReadyToSend/letter_for_{name_strip}.docx", mode="w") as completed:
            completed.write(new_let)
