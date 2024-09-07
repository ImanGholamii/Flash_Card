import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
ROWS = 3
COLUMNS = 3
# ---------------------------- MAKE CSV DATA ------------------------------- #
data_file = pandas.read_csv("data/english_words.csv")
data = pandas.DataFrame(data_file)
data["English"].to_csv("data/english_words.csv", index=False)
with open("data/fa.txt", "r", encoding="utf-8") as fa_data:
    fa_list = fa_data.readlines()
    data["Persian"] = [word.strip().replace('"', '') for word in fa_list]
data.to_csv("data/english_words_with_translations.csv", index=False)

# ---------------------------- window ------------------------------- #
window = Tk()
window.title("Flashy")

# ---------------------------- grid system ------------------------------- #
for row in range(ROWS):
    window.grid_rowconfigure(row)
for col in range(COLUMNS):
    window.grid_columnconfigure(col)


window.mainloop()
