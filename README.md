# yj_sudokuXLSx
make sudokus and put them in excel files for printing

#requirements
the python script only needs `random` and `openpyxl`. it is written for Python 3.

# Usage example
difficulty_level = 'medium'  # Choose 'easy', 'medium', or 'difficult'
puzzle = generate_sudoku(difficulty_level)
export_to_excel(puzzle, 'sudoku_puzzle.xlsx')
