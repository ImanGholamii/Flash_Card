import pandas
from tkinter import Tk, Canvas, PhotoImage, Button

BACKGROUND_COLOR = "#B1DDC6"
ACTIVE_BG_COLOR = "#557C56"
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
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# ---------------------------- grid system ------------------------------- #
for row in range(ROWS):
    window.grid_rowconfigure(row)
for col in range(COLUMNS):
    window.grid_columnconfigure(col)

# ---------------------------- Canvas ------------------------------- #
canvas = Canvas(width=800, height=526, highlightthickness=0)

card_fg_img_adr = "images/card_front.png"
card_fg_img = PhotoImage(file=card_fg_img_adr)
canvas.create_image(400, 263, image=card_fg_img)
canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text="Hello", font=('Ariel', 60, 'normal'))

canvas.config(background=BACKGROUND_COLOR)
canvas.grid_configure(row=0, column=1)

# card_bg_img_adr = "images/card_back.png"
# card_bg_img = PhotoImage(file=card_bg_img_adr)
# canvas.create_image(400, 263, image=card_bg_img)
# canvas.grid_configure(row=1, column=1)

# ---------------------------- BUTTONS ------------------------------- #

right_img_adr = "images/right.png"
right_img = PhotoImage(file=right_img_adr)
right_btn = Button(image=right_img, border=0.5, highlightthickness=0, activebackground=ACTIVE_BG_COLOR)
right_btn.grid_configure(row=1, column=2)

wrong_img_adr = "images/wrong.png"
wrong_img = PhotoImage(file=wrong_img_adr)
wrong_btn = Button(image=wrong_img, border=0.5, highlightthickness=0, activebackground=ACTIVE_BG_COLOR)
wrong_btn.grid_configure(row=1, column=0)


window.mainloop()
