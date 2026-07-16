# Writing to a file

with open("sample.txt", "w") as file:
    file.write("Welcome to Week 2 Internship!\n")
    file.write("Learning Generative AI with Gemini.\n")

print("Data written successfully.\n")

# Reading from the file

with open("sample.txt", "r") as file:
    content = file.read()

print("Contents of sample.txt:")
print(content)

# Appending data

with open("sample.txt", "a") as file:
    file.write("This line was appended later.\n")

print("\nNew line appended successfully.")

# Reading again

with open("sample.txt", "r") as file:
    updated_content = file.read()

print("\nUpdated File Contents:")
print(updated_content)