#! /bin/env python3
import random
from openpyxl import Workbook

def generate_sudoku(difficulty='easy'):
    # Create a 9x9 grid filled with zeros
    sudoku = [[0 for _ in range(9)] for _ in range(9)]

    # Function to check if a number is safe to place in a cell
    def is_safe_to_place(num, row, col):
        # Check if the number is not present in the row
        if num in sudoku[row]:
            return False
        
        # Check if the number is not present in the column
        if num in [sudoku[i][col] for i in range(9)]:
            return False
        
        # Check if the number is not present in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if sudoku[i][j] == num:
                    return False
        
        return True

    # Function to solve the Sudoku puzzle using backtracking
    def solve_sudoku():
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    for num in random.sample(range(1, 10), 9):
                        if is_safe_to_place(num, i, j):
                            sudoku[i][j] = num
                            if solve_sudoku():
                                return True
                            sudoku[i][j] = 0
                    return False
        return True

    # Function to remove cells based on difficulty level
    def remove_cells(difficulty):
        # Define the number of cells to remove based on difficulty
        if difficulty == 'easy':
            cells_to_remove = random.randint(36, 45)
        elif difficulty == 'medium':
            cells_to_remove = random.randint(46, 54)
        else:
            cells_to_remove = random.randint(55, 63)
        
        # Remove cells while maintaining solvability
        for _ in range(cells_to_remove):
            row, col = random.randint(0, 8), random.randint(0, 8)
            while sudoku[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            temp = sudoku[row][col]
            sudoku[row][col] = 0
            temp_sudoku = [row[:] for row in sudoku]
            solve_sudoku()
            if sum(row.count(0) for row in sudoku) != 0:
                sudoku[row][col] = temp

    solve_sudoku()
    remove_cells(difficulty)

    return sudoku

def export_to_excel(sudoku, filename):
    wb = Workbook()
    ws = wb.active

    for i in range(9):
        for j in range(9):
            ws.cell(row=i+1, column=j+1).value = sudoku[i][j]

    wb.save(filename)
