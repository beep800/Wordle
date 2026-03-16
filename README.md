# 🟩 Wordle — Python Clone

A fully functional clone of the popular word-guessing game **Wordle**, built with Python and `tkinter`. Guess the 5-letter word in 5 tries!


## Features

- 5x5 interactive guess grid built with `tkinter`
- Color-coded feedback on every guess:
  - 🟩 **Green** — correct letter, correct position
  - 🟨 **Yellow** — correct letter, wrong position
  - ⬜ **Gray** — letter not in the word
- Input validation — rejects non-words and wrong-length entries
- Live guesses remaining counter
- Win/lose popups
- Large word list loaded from external files for variety

## How to Play

1. Type any 5-letter word into the input box
2. Press **Try** to submit your guess
3. Use the color hints to narrow down the word
4. Guess the word within 5 attempts to win!

## Project Structure

```
Wordle/
├── Wordle.py        # Main game logic and tkinter UI
├── WordList.py      # Loads valid words from word list files
├── Words            # Primary word list (title-cased words)
└── Words2           # Secondary word list (lowercase words)
```

## Getting Started

### Prerequisites

- Python 3.x (`tkinter` is included in the standard library)

### Run the game

```bash
git clone https://github.com/your-username/Wordle.git
cd Wordle
python Wordle.py
```

> Make sure the `Words` and `Words2` files are in the same directory as `Wordle.py`

## How It Works

- A random 5-letter word is selected from `Words` at game start
- Each guess is validated against both word lists before being accepted
- Each letter is compared position-by-position against the target word and colored accordingly
- The game ends when the player guesses correctly or exhausts all 5 attempts

## License

This project is open source and available under the [MIT License](LICENSE).
