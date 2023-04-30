def minimum(array):
    rows_sum = [sum(row) for row in array]
    cols_sum = [sum(col) for col in zip(*array)]
    min_row = rows_sum.index(min(rows_sum))
    min_col = cols_sum.index(min(cols_sum))
    return [min_row, min_col]


print(minimum([
    [7, 2, 7, 2, 8],
    [2, 9, 4, 1, 7],
    [3, 8, 6, 2, 4],
    [2, 5, 2, 9, 1],
    [6, 6, 5, 4, 5]]
))
