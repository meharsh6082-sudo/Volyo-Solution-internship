import os
from datetime import datetime

# ===== TAKE MULTI-LINE CONTENT =====
print("Paste your content below.")
print("Type END in a new line when finished.\n")

lines = []

while True:
    line = input()

    if line.strip() == "end":
        break

    lines.append(line)

content = "\n".join(lines)

# ===== AUTO FILE NAME =====
today_date = datetime.now().strftime("%d-%m-%Y")

file_name = f"work done on {today_date}.txt"

# ===== CREATE TXT FILE =====
with open(file_name, "w", encoding="utf-8") as file:
    file.write(content)

print(f"\n{file_name} created successfully!")

# ===== AUTO GIT UPLOAD =====
os.system("git add .")

os.system(f'git commit -m "Updated {today_date}"')

os.system("git push")

print("\nUploaded to GitHub successfully!")