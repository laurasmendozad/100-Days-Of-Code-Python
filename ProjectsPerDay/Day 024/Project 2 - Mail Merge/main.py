''' Generar cartas automáticamente '''

PLACEHOLDER = "[name]"

with open(r"ProjectsPerDay\Day 024\Project 2 - Mail Merge\Input\Names\invited_names.txt", encoding="utf-8") as names_file:
    names = names_file.readlines()

with open(r"ProjectsPerDay\Day 024\Project 2 - Mail Merge\Input\Letters\starting_letter.txt", encoding="utf-8") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"ProjectsPerDay\Day 024\Project 2 - Mail Merge\Output\ReadyToSend\letter_for_{stripped_name}.txt", encoding="utf-8",
                    mode="w") as new_letter_file:
            new_letter_file.write(new_letter)
