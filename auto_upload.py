import os

# ===== TAKE MULTI-LINE INPUT =====
print("Paste your full content below.")
print("When finished, type END in a new line.\n")

lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    lines.append(line)

content = "\n".join(lines)

# ===== FILE NAME =====
file_name = input("\nEnter file name: ")

# ===== CREATE TXT FILE =====
with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
    file.write(content)

print(f"\n{file_name}.txt created successfully!")

# ===== GIT COMMANDS =====
os.system("git add .")

os.system(f'git commit -m "Added {file_name}.txt"')

os.system("git push")

print("\nFile uploaded to GitHub successfully!")