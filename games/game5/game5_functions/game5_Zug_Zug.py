def contains_zugzug_date(grid):
    date_seq = [1, 5, 1, 1, 1, 9, 9, 4]   # Release day of Warcraft
    for row in grid:
        for i in range(len(row) - len(date_seq) + 1):
            if row[i:i+len(date_seq)] == date_seq: # If the row has the date sequence then easter egg runs
                return True
    return False