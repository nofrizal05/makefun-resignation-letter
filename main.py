import os

LINE = (
    "After saying no 12,847 times with no thank-you, "
    "I hereby resign as your rate limit: please find someone else to "
    "disappoint your users."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
