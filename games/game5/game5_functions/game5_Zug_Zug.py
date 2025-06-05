def contains_zugzug_date(grid):
    date_seq = [1, 5, 1, 1, 1, 9, 9, 4]
    for row in grid:
        for i in range(len(row) - len(date_seq) + 1):
            if row[i:i+len(date_seq)] == date_seq:
                return True
    return False
