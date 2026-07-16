import json

# Python dictionary
student = {
    "name": "Antra Agarwal",
    "course": "B.Tech CSE",
    "skills": [
        "Python",
        "SQL",
        "Generative AI"
    ]
}

# Write dictionary to a JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully!")

# Read the JSON file
with open("student.json", "r") as file:
    data = json.load(file)

print("\nData loaded from JSON:")
print(data)

print("\nStudent Name:", data["name"])
print("Course:", data["course"])
print("Skills:", ", ".join(data["skills"]))