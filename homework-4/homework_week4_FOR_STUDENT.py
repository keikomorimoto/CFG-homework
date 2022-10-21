"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""


def search_in_matrix(matrix, target):

    row, col = 0, len(matrix[0]) - 1  # search starts int the top right

    while row < len(matrix) and col >= 0: 
        if matrix[row][col] == target:
            return [row, col]
        elif matrix[row][col] < target:  # move to the next row below
            row += 1
        else:  # matrix[row][col] > target
            col -= 1   # move to the left colum

    return [-1, -1]

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 44

print(search_in_matrix(matrix, target))
