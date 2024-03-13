# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt", mode="r") as names:
    names = names.readlines()

for inviting in names:
    with open("Input/Letters/starting_letter.txt", mode="r") as message:
        content = message.read()
        content = content.replace("[name]", inviting)

    with open(f"Output/ReadyToSend/{inviting}invitation.txt", mode="w") as letters:
        letters.write(content)
