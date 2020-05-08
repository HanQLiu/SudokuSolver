from prettytable import PrettyTable

"""Empty Squares"""
x1y1, x2y1, x3y1, x4y1, x5y1, x6y1, x7y1, x8y1, x9y1 = {}, {}, {}, {}, {}, {}, {}, {}, {}
x1y2, x2y2, x3y2, x4y2, x5y2, x6y2, x7y2, x8y2, x9y2 = {}, {}, {}, {}, {}, {}, {}, {}, {}
x1y3, x2y3, x3y3, x4y3, x5y3, x6y3, x7y3, x8y3, x9y3 = {}, {}, {}, {}, {}, {}, {}, {}, {}
x1y4, x2y4, x3y4, x4y4, x5y4, x6y4, x7y4, x8y4, x9y4 = {}, {}, {}, {}, {}, {}, {}, {}, {}
x1y5, x2y5, x3y5, x4y5, x5y5, x6y5, x7y5, x8y5, x9y5 = {}, {}, {}, {}, {}, {}, {}, {}, {}
x1y6, x2y6, x3y6, x4y6, x5y6, x6y6, x7y6, x8y6, x9y6 = {}, {}, {}, {}, {}, {}, {}, {}, {}
x1y7, x2y7, x3y7, x4y7, x5y7, x6y7, x7y7, x8y7, x9y7 = {}, {}, {}, {}, {}, {}, {}, {}, {}
x1y8, x2y8, x3y8, x4y8, x5y8, x6y8, x7y8, x8y8, x9y8 = {}, {}, {}, {}, {}, {}, {}, {}, {}
x1y9, x2y9, x3y9, x4y9, x5y9, x6y9, x7y9, x8y9, x9y9 = {}, {}, {}, {}, {}, {}, {}, {}, {}

row_1 = [x1y1, x2y1, x3y1, x4y1, x5y1, x6y1, x7y1, x8y1, x9y1]
row_2 = [x1y2, x2y2, x3y2, x4y2, x5y2, x6y2, x7y2, x8y2, x9y2]
row_3 = [x1y3, x2y3, x3y3, x4y3, x5y3, x6y3, x7y3, x8y3, x9y3]
row_4 = [x1y4, x2y4, x3y4, x4y4, x5y4, x6y4, x7y4, x8y4, x9y4]
row_5 = [x1y5, x2y5, x3y5, x4y5, x5y5, x6y5, x7y5, x8y5, x9y5]
row_6 = [x1y6, x2y6, x3y6, x4y6, x5y6, x6y6, x7y6, x8y6, x9y6]
row_7 = [x1y7, x2y7, x3y7, x4y7, x5y7, x6y7, x7y7, x8y7, x9y7]
row_8 = [x1y8, x2y8, x3y8, x4y8, x5y8, x6y8, x7y8, x8y8, x9y8]
row_9 = [x1y9, x2y9, x3y9, x4y9, x5y9, x6y9, x7y9, x8y9, x9y9]
rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]

'''Nine Cubes'''
upper_left_cube = [rows[0][0], rows[0][1], rows[0][2],
                   rows[1][0], rows[1][1], rows[1][2],
                   rows[2][0], rows[2][1], rows[2][2]]
upper_cube = [rows[0][3], rows[0][4], rows[0][5],
              rows[1][3], rows[1][4], rows[1][5],
              rows[2][3], rows[2][4], rows[2][5]]
upper_right_cube = [rows[0][6], rows[0][7], rows[0][8],
                    rows[1][6], rows[1][7], rows[1][8],
                    rows[2][6], rows[2][7], rows[2][8]]
left_cube = [rows[3][0], rows[3][1], rows[3][2],
             rows[4][0], rows[4][1], rows[4][2],
             rows[5][0], rows[5][1], rows[5][2]]
center_cube = [rows[3][3], rows[3][4], rows[3][5],
               rows[4][3], rows[4][4], rows[4][5],
               rows[5][3], rows[5][4], rows[5][5]]
right_cube = [rows[3][6], rows[3][7], rows[3][8],
              rows[4][6], rows[4][7], rows[4][8],
              rows[5][6], rows[5][7], rows[5][8]]
bottom_left_cube = [rows[6][0], rows[6][1], rows[6][2],
                    rows[7][0], rows[7][1], rows[7][2],
                    rows[8][0], rows[8][1], rows[8][2]]
bottom_cube = [rows[6][3], rows[6][4], rows[6][5],
               rows[7][3], rows[7][4], rows[7][5],
               rows[8][3], rows[8][4], rows[8][5]]
bottom_right_cube = [rows[6][6], rows[6][7], rows[6][8],
                     rows[7][6], rows[7][7], rows[7][8],
                     rows[8][6], rows[8][7], rows[8][8]]
nine_cubes = [upper_left_cube, upper_cube, upper_right_cube, left_cube, center_cube, right_cube, bottom_left_cube, bottom_cube, bottom_right_cube]

'''Functions'''
def check_horizontal(rows):
    for row in rows:
        occupied_numbers = set()
        for item in row:
            if item['number_or_empty'] != " ":
                occupied_numbers.add(item['number_or_empty'])
        for item in row:
            item['remaining_possibilities'] -= occupied_numbers

def check_vertical(rows):
    for col_num in range(9):
        occpied_numbers = set()
        for row in rows:
            if row[col_num]['number_or_empty'] != " ":
                occpied_numbers.add(row[col_num]['number_or_empty'])
        for row in rows:
            row[col_num]['remaining_possibilities'] -= occpied_numbers

def check_cube():
    for cube in nine_cubes:
        occupied_numbers = set()
        for square in cube:
            if square['number_or_empty'] != " ":
                occupied_numbers.add(square['number_or_empty'])
        for square in cube:
            square['remaining_possibilities'] -= occupied_numbers

def horrizontal_unique_values(rows):
    # check unique remaining cuz now it's 9pm and my brain is fried im going with easy version
    for row in rows:
        for square in row:
            if len(square['remaining_possibilities']) == 1:
                square['number_or_empty'] = square['remaining_possibilities']

    for row in rows:
        union = set()
        for square_num in range(8):
            if row[square_num]['number_or_empty'] == " ":
                if len(union) == 0:
                    union = row[square_num]['remaining_possibilities']
                else:
                    union = union.union(row[square_num]['remaining_possibilities'])
        for square in row:
            unique_num = set()
            if square['number_or_empty'] == " ":
                unique_num = union - square['remaining_possibilities']
            if len(unique_num) == 1 and (unique_num in square['remaining_possibilities']):
                square['number_or_empty'] = unique_num

def vertical_unique_values(rows):
    # check unique remaining cuz now it's 9pm and my brain is fried im going with easy version
    for col_num in range(9):
        for row in rows:
            if len(row[col_num]['remaining_possibilities']) == 1:
                row[col_num]['number_or_empty'] = row[col_num]['remaining_possibilities']

    for col_num in range(9):
        union = set()
        for row in rows:
            if row[col_num] == " ":
                if len(union == 0):
                    union = row[col_num]['remaining_possibilities']
                else:
                    union = union.union(row[col_num]['remaining_possibilities'])
        for row in rows:
            unique_num = set()
            if row[col_num]['number_or_empty'] == " ":
                unique_num = union - row[col_num]['remaining_possibilities']
            if len(unique_num) == 1 and (unique_num in row[col_num]['remaining_possibilities']):
                row[col_num]['number_or_empty'] = unique_num

def cube_unique_values():
    # check unique remaining cuz now it's 9pm and my brain is fried im going with easy version
    for cube in nine_cubes:
        for square in cube:
            if len(square['remaining_possibilities']) == 1:
                square['number_or_empty'] = square['remaining_possibilities']

    for cube in nine_cubes:
        union = set()
        for square in cube:
            if square['number_or_empty'] == " ":
                if len(union) == 0:
                    union = square['remaining_possibilities']
                else:
                    union = union.union(square['remaining_possibilities'])
        for square in cube:
            unique_num = set()
            if square['number_or_empty'] == " ":
                unique_num = union - square['remaining_possibilities']
            if len(unique_num) == 1 and (unique_num in square['remaining_possibilities']):
                square['number_or_empty'] = unique_num


def sudoku_prettytable(rows):
    pt = PrettyTable()
    pt.field_names = ["Row 1", "Row 2", "Row 3", "Row 4", "Row 5", "Row 6", "Row 7", "Row 8", "Row 9"]
    for row in rows:
        pt.add_row([row[0]['number_or_empty'], row[1]['number_or_empty'], row[2]['number_or_empty'], row[3]['number_or_empty'], row[4]['number_or_empty'], row[5]['number_or_empty'], row[6]['number_or_empty'], row[7]['number_or_empty'], row[8]['number_or_empty']])
    print(pt)

def remaining_prettytable(rows):
    pt = PrettyTable()
    pt.field_names = ["Row 1", "Row 2", "Row 3", "Row 4", "Row 5", "Row 6", "Row 7", "Row 8", "Row 9"]
    for row in rows:
        pt.add_row([row[0]['remaining_possibilities'], row[1]['remaining_possibilities'], row[2]['remaining_possibilities'], row[3]['remaining_possibilities'], row[4]['remaining_possibilities'], row[5]['remaining_possibilities'], row[6]['remaining_possibilities'], row[7]['remaining_possibilities'], row[8]['remaining_possibilities']])
    print(pt)

def main():
    """Sudoku Solver"""
    for row in rows:
        for item in row:
            item['number_or_empty'] = " "
            item['remaining_possibilities'] = set()

    '''Fill The Initial Sudoku Squares Here'''
    '''Clean Sheet'''
    clean_sheet = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    ]

    fill_initial_sudoku = [
        ["5", "8", "6", "4", "2", "7", "9", "1", "3"],
        [" ", " ", " ", " ", " ", " ", "6", "8", "7"],
        ["1", "7", "9", "6", "8", "3", "2", "5", "4"],
        ["6", "5", " ", "1", "3", "2", " ", " ", "9"],
        [" ", "4", " ", "5", "9", "8", "1", "6", "2"],
        [" ", "9", " ", " ", "6", "4", " ", "3", "8"],
        ["9", "6", " ", " ", "7", " ", " ", " ", "5"],
        ["4", " ", " ", " ", "5", " ", "8", " ", "1"],
        ["8", " ", " ", "3", " ", " ", " ", " ", "6"]
    ]

    for row in range(9):
        for col in range(9):
            rows[row][col]['number_or_empty'] = fill_initial_sudoku[row][col]

    '''Fill the remaining possibilities 1-9'''
    for row in rows:
        for col in row:
            if col['number_or_empty'] == " ":
                col['remaining_possibilities'] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    '''Check Remaining Possibilities'''
    check_horizontal(rows)
    check_vertical(rows)
    check_cube()

    '''Check unique numbers in each square'''
    horrizontal_unique_values(rows)
    vertical_unique_values(rows)
    cube_unique_values()

    '''Sudoku Table'''
    print("\nSudoku Table")
    sudoku_prettytable(rows)
    '''Remaining Possibilities Table'''
    print("\nRemaining Possibilities Table")
    remaining_prettytable(rows)

if __name__ == '__main__':
    main()