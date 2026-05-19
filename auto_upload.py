import os

# ===== TAKE INPUT =====
file_name = input("Enter file name: ")
content = input("Enter content: ")

# ===== CREATE TXT FILE =====
with open(f"{file_name}.txt", "w") as file:
    file.write(content)

print(f"{file_name}.txt created successfully!")

# ===== GIT COMMANDS =====
os.system("git add .")

os.system(f'git commit -m "Added {file_name}.txt"')

os.system("git push")

print("File uploaded to GitHub successfully!")