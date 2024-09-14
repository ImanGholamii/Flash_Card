# 📝 Flashy - English to Persian Flashcard App

Welcome to **Flashy**! This project is a flashcard application that helps users learn English words and their Persian translations. The app uses a simple and intuitive GUI built with Python and Tkinter. It allows users to review words, mark known and unknown words, and save progress for future study sessions.

## 🌟 Features

- **Random Word Generation**: Shows a random English word on the front of the card and flips to reveal the Persian translation.
- **Known/Unknown Tracking**: Track known words and remove them from future sessions. Save unknown words for future review in a separate file.
- **Word Lists**: Use an English word list (`english_words.csv`) and a corresponding Persian translation file (`fa.txt`) to generate flashcards.
- **Interactive Buttons**: Users can mark words as known or unknown, and the app will automatically update the word lists accordingly.

## 🚀 Getting Started

### Prerequisites

To run this project, you will need:
- [Python 3.x](https://www.python.org/downloads/)
- Required libraries: `pandas`, `tkinter`

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ImanGholamii/Flash_Card.git
   cd Flash_Card
2. Install the required Python libraries:
   ```sh
   pip install pandas
4. Place your data files:
- english_words.csv (with a list of English words) in the data/words/ folder.
- fa.txt (with Persian translations) in the same folder.
Example file structure:
    ├── data
    │   └── words
    │       ├── english_words.csv
    │       └── fa.txt
    ├── images
    │   ├── card_front.png
    │   ├── card_back.png
    │   ├── right.png
    │   └── wrong.png
    ├── main.py
4. Run the program:
   ```sh
   python main.py

## 📚 How to Use
- The app will start by displaying an English word.
- After 3 seconds, the card flips to reveal the Persian translation.
- If you know the word, press the ✅ (right) button, and the word will be removed from the review list.
- If you don’t know the word, press the ❌ (wrong) button, and the word will be saved to a separate file for further study (wrong_answered_words.csv).
- The app will continue showing flashcards until all words are either known or marked for review.
  
## 🖼️ User Interface
The app has an easy-to-use graphical interface featuring:

- A flashcard image that shows the English word on the front and flips to show the Persian translation.
- Buttons for marking the word as "known" or "unknown."
- Visual elements such as images for cards and buttons (stored in the images/ folder).
- 
## 📈 Future Enhancements
- 🔄 Add Restart Feature: Allow users to restart the session with the original word list.
- 🔍 Search Words: Implement a search function to look up specific words.
- 🔐 Word Difficulty Levels: Add difficulty levels and track words based on their complexity.    

## 🛠️ Technologies Used
- Python 3
- Tkinter (for GUI)
- Pandas (for data handling)

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/ImanGholamii/Flash_Card/blob/main/LICENSE.txt) file for details.

## 🙌 Acknowledgements
- Inspiration for this project comes from learning apps like Duolingo and Quizlet.
- Special thanks to the contributors of the pandas and tkinter libraries and Dr Angela Yu.
## ⭐️ Support
If you like this project, please give it a ⭐️ on [GitHub!](ImanGholamii/Flash_Card)
