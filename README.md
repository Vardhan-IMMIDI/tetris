# 🎮 Terminal Tetris

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CS50P](https://img.shields.io/badge/CS50P-Final%20Project-red.svg)](https://cs50.harvard.edu/python/)

> *A terminal-based implementation of the legendary puzzle game that changed the world*

#### 🎬 Video Demo: [URL HERE]

## 📖 About

Terminal Tetris is a faithful recreation of the iconic puzzle game originally created by **Alexey Pajitnov** in 1985. This project was inspired by the 2023 Apple TV+ film "Tetris," which tells the incredible story behind one of the most beloved video games of all time. After watching the movie and learning about Pajitnov's genius creation and the fascinating geopolitical drama surrounding Tetris's journey from the Soviet Union to the world, I felt compelled to build my own tribute to this masterpiece.

Built entirely in Python using the curses library, this implementation brings the classic Tetris experience directly to your terminal with colorful blocks, smooth gameplay mechanics, and authentic scoring system.

## ✨ Features

- 🎯 **Classic Tetris Gameplay** - All seven original tetromino pieces (I, O, T, S, Z, J, L)
- 🌈 **Colorful Terminal Graphics** - Each piece type has its own color
- ⚡ **Smooth Controls** - Responsive movement, rotation, and dropping
- 📊 **Authentic Scoring System** - Points awarded based on lines cleared simultaneously
- ⏸️ **Pause Functionality** - Press 'P' to pause/unpause the game
- 🎮 **Intuitive Controls** - Arrow keys for movement, spacebar for hard drop

## 🎮 Controls

| Key     | Action                   |
|---------|--------------------------|
| `←` `→` | Move piece left/right    |
| `↑`     | Rotate piece             |
| `↓`     | Soft drop (faster fall)  |
| `P`     | Pause/Unpause game       |
| `Q`     | Quit game                |

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Unix-like system (Linux, macOS) or Windows with curses support
- Terminal window of at least 25x25 characters

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/terminal-tetris.git
cd terminal-tetris
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python project.py
```

## 🏗️ Project Structure

```
terminal-tetris/
├── project.py          # Main game implementation
├── test_project.py     # Unit tests
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## 📁 File Descriptions

### `project.py`
The heart of the game containing all core functionality:

- **`main(stdscr)`**: Primary game loop handling terminal setup, input processing, and rendering
- **`Tetris` class**: Core game logic including:
  - Game state management (board, current block, score)
  - All seven tetromino definitions and rotation matrices
  - Movement, rotation, and collision detection
  - Line clearing and scoring algorithms
  - Gravity simulation for falling pieces
- **Helper functions**:
  - `block_boundaries()`: Calculates tetromino boundary positions
  - `can_place_block()`: Collision detection for block placement
  - `rm_current_from_board()` / `add_current_to_board()`: Board state management
- **`SizeError` exception**: Custom exception for terminal size validation

### `test_project.py`
Comprehensive unit tests ensuring game reliability:
- Boundary calculation verification
- Block placement validation (in-bounds, collision detection)
- Board state management testing
- Edge case handling for game mechanics

### `requirements.txt`
External dependencies (primarily curses library documentation)

## 🎯 Game Mechanics

This implementation faithfully recreates classic Tetris gameplay:

- **Seven Tetromino Types**: I-piece (line), O-piece (square), T-piece, S-piece, Z-piece, J-piece, and L-piece
- **Rotation System**: Each piece (except the square) can be rotated in 90-degree increments
- **Line Clearing**: Complete horizontal lines disappear, causing blocks above to fall
- **Scoring System**:
  - 1 line: 40 points
  - 2 lines: 100 points
  - 3 lines: 300 points
  - 4 lines (Tetris): 1200 points

## 🎨 Design Philosophy

**Terminal-First Approach**: I chose the curses library over GUI frameworks to create a unique, retro computing experience that pays homage to the era when Tetris was first created. This design choice reflects the simplicity and elegance of Pajitnov's original vision.

**Color Psychology**: Each tetromino type has its own distinct color to aid in quick visual recognition, following the color conventions established in later official Tetris releases.

**Authentic Feel**: The game timing, scoring system, and block behavior closely mirror the original Tetris mechanics to provide an authentic playing experience.

## 🧪 Testing

Run the test suite to verify game functionality:

```bash
pytest test_project.py -v
```

The tests cover:
- Block boundary calculations
- Collision detection algorithms
- Board state management
- Edge cases and error conditions

## 🎬 Inspiration

This project exists because of the incredible story told in Apple TV+'s "Tetris" (2023). The film revealed the fascinating journey of how Alexey Pajitnov's simple yet brilliant puzzle game became a global phenomenon, navigating through Cold War politics, corporate intrigue, and the early days of video game licensing. Pajitnov's creation has touched billions of lives, and this implementation is my small tribute to his genius and the cultural impact of Tetris.

## 🎓 Academic Context

This project was developed as the final project for Harvard's CS50P (CS50's Introduction to Programming with Python) course. It demonstrates mastery of:
- Object-oriented programming principles
- Terminal-based user interface development
- Game loop implementation and state management
- Unit testing and code reliability
- Project documentation and structure

## 🤝 Contributing

This project was created for educational purposes as part of CS50P. While not actively seeking contributions, feel free to fork the repository and create your own variations!

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Alexey Pajitnov** - Creator of Tetris and inspiration for this project
- **Apple TV+** - For the incredible "Tetris" film that sparked this project
- **Professor David J. Malan** - For his extraordinary dedication to computer science education and for making programming accessible to learners worldwide. His passion, creativity, and genuine care for students shine through every CS50 lecture, inspiring countless individuals (including myself) to fall in love with programming. Thank you for showing us that computer science is not just about code, but about thinking computationally and solving problems creatively.
- **The entire CS50 team** - Including all the teaching fellows, course assistants, and staff who work tirelessly behind the scenes to create such an exceptional learning experience. From the thoughtfully crafted problem sets to the supportive online community, every detail reflects the team's commitment to student success.
- **CS50's Philosophy** - For teaching us that it's not just about the destination, but about the journey of learning to think like a computer scientist. The course's emphasis on academic honesty, collaboration, and celebrating both success and failure has shaped not just my programming skills, but my approach to learning itself.
- **Tetris Wiki** - For being an invaluable resource containing comprehensive documentation of Tetris mechanics, rotation systems, scoring algorithms, and historical information. The wiki's detailed technical specifications and community-contributed knowledge were essential for implementing authentic gameplay mechanics.
- **The Tetris Company** - For maintaining the legacy of this incredible game

---

*"I want to emphasize that Tetris is not just a game, it's a phenomenon."* - Alexey Pajitnov

*"This was CS50P!"* - A phrase that now carries so much meaning after an incredible learning journey.

**Made with ❤️ as a tribute to the greatest puzzle game ever created**
