# 🧠 Quiz Game

This is a simple command-line multiple-choice **Quiz Game** built with Python. The game uses a list of question data, formats them into objects, and tests the user one question at a time.

## 📚 How It Works

1. Question data is loaded from a source (like an API or hardcoded list).
2. Each question is turned into a `Question` object with its text and correct answer.
3. The `QuizBrain` class manages the game flow:
   - Presents one question at a time.
   - Checks the user’s answer.
   - Keeps track of the score and question number.
4. At the end, it displays the user's final score.

## 🧱 Project Structure

| File | Description |
|------|-------------|
| `main.py` | Initializes the quiz and controls the main game loop. |
| `question_model.py` | Defines the `Question` class that holds question text and answer. |
| `data.py` | Contains the list of question dictionaries. |
| `quiz_brain.py` | Contains the `QuizBrain` class, which manages quiz progression and user interaction. |

## 📦 Features

- Dynamic question loading from structured data.
- Object-oriented design.
- Score tracking and clean end-of-quiz message.
- Easy to extend with new questions or input methods.

## 🧠 Example Question Format

```python
question_data = [
    {"question": "Is the sky blue?", "correct_answer": "True"},
    {"question": "Is 2 + 2 = 5?", "correct_answer": "False"}
]
