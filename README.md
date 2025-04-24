# US\_GAME - Learn All US States 🇺🇸

**US\_GAME** is a fun and educational Python-based application that helps users learn and memorize all 50 states of the United States.

## 🧠 Purpose

The goal of this app is to make learning U.S. state names engaging and interactive. Users can test their knowledge by guessing the names of all the states and seeing their guesses displayed on a U.S. map.

## 🛠️ Technologies Used

- Python 🐍
- `turtle` module for graphical interface
- `pandas` for data handling (e.g., reading state names and coordinates from a CSV file)

## 🎮 How It Works

1. When the app starts, it displays a blank U.S. map.
2. Users are prompted to type the name of a U.S. state.
3. If the guess is correct:
   - The state name appears at the correct location on the map.
   - The state is added to the list of correct guesses.
4. If the user types "Exit":
   - The game ends.
   - A CSV file is generated with the names of states not yet guessed, so the user can review and learn.

## 📦 Features

- Interactive guessing using a pop-up input box
- Real-time display of guessed states on a map
- Learning tool that tracks which states you missed
- Saves progress in a CSV file to help improve your geography knowledge

## 🚀 How to Run the App

1. Make sure you have Python installed (3.6+ recommended).
2. Install dependencies (if not already installed):

```bash
pip install pandas
```

3. Place your `us_states.csv` (contains state names and coordinates) and the `blank_states_img.gif` (map image) in the same folder.
4. Run the script:

```bash
python us_game.py
```

## 📁 Files Included

- `main.py` - Main script to run the game
- `50_states.csv` - CSV file with all U.S. state names and their map coordinates
- `blank_states_img.gif` - Map of the U.S. (used as the background)
- \`states\_to\_learn.csv\` - CSV file automatically generated with the names of the states you didn't guess correctly



  ✨ Example

```
Guess the state: Texas
Guess the state: California
...
Guess the state: Exit
You missed: ['Alaska', 'Montana', ...]
File saved: states_to_learn.csv
```

## 👨‍🏫 Educational Value

This app is perfect for students, teachers, and anyone wanting to improve their U.S. geography knowledge in a fun and interactive way!

---

Made with ❤️ using Python!

