def count_mines(grid, row, col, rows, cols):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '*':
                count += 1
    return count

def generate_output(grid):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                grid[i][j] = str(count_mines(grid, i, j, rows, cols))
    return grid

def print_grid(grid, field_num):
    print(f"Field #{field_num}:")
    for row in grid:
        print(''.join(row))
    print()

def main():
    field_num = 0
    while True:
        field_num += 1
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        if rows == 0 and cols == 0:
            break
        grid = []
        print("Enter the grid:")
        for _ in range(rows):
            row = input().strip()
            grid.append(list(row))
        output_grid = generate_output(grid)
        print_grid(output_grid, field_num)

if __name__ == "__main__":
    main()
