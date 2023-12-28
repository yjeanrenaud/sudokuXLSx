# yj_sudokuXLSx
make sudokus and put them in excel files for printing

#requirements
the python script only needs `random` and `openpyxl`. it is written for Python 3.

#todos
- error handling for file handling. currently this is all relying on openpyxl
- more parameters, e. g. amount of free fields, array of numbers that are already complete or for non standard grids like 4x4

# Usage example
```
import yj_sudokuXLSx
difficulty_level = 'medium'  # Choose 'easy', 'medium', or 'difficult'
puzzle = generate_sudoku(difficulty_level)
export_to_excel(puzzle, 'sudoku_puzzle.xlsx')
```
