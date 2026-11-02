class Grid:
    def __init__(self, data):
        self._grid = [list(x) for x in data.splitlines()]
        self.mark_land(self._center[0], self._center[1])

    @property
    def _center(self):
        return self.n_rows // 2, self.n_cols // 2

    @property
    def n_rows(self) -> int:
        return len(self._grid)

    @property
    def n_cols(self) -> int:
        return len(self._grid[0])

    def show(self):
        for row in self._grid:
            print(" ".join(row))

    def mark_land(self, i_row, i_col):
        self._grid[i_row][i_col] = "#"

    def mark_sand(self, i_row, i_col):
        self._grid[i_row][i_col] = "="

    def mark_trees(self, i_row, i_col):
        self._grid[i_row][i_col] = "@"

    def get_neighbors(self, coord):
        neighbors = []
        options = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, -1),
            (-1, 1),
        ]
        for opt in options:
            new = (coord[0] + opt[0], coord[1] + opt[1])
            if 0 <= new[0] < self.n_rows and 0 <= new[1] < self.n_cols:
                neighbors.append(new)
        return neighbors

    def can_be_land(self, coord):
        neighbors = self.get_neighbors(coord)
        count = 0
        for point in neighbors:
            if self._grid[point[0]][point[1]] == "1":
                count += 1
            if self._grid[point[0]][point[1]] == "#":
                count += 1
        return count >= 5

    def get_frontier(self):
        frontier = set()
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                if self._grid[i_row][i_col] == "#":
                    neighbors = self.get_neighbors((i_row, i_col))
                    for new in neighbors:
                        if self._grid[new[0]][new[1]] != "#":
                            frontier.add(new)
        return frontier

    def count_land(self):
        count = 0
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                if self._grid[i_row][i_col] == "#":
                    count += 1
        return count

    def is_edge(self, coord_x, coord_y):
        if coord_x == 0 or coord_x == self.n_rows - 1:
            return True
        if coord_y == 0 or coord_y == self.n_cols - 1:
            return True

    def get_border(self):
        border = set()
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                if self._grid[i_row][i_col] == "#":
                    neighbors = self.get_neighbors((i_row, i_col))
                    for neighbor in neighbors:
                        if self._grid[neighbor[0]][neighbor[1]] != "#":
                            border.add((i_row, i_col))
                    if self.is_edge(i_row, i_col):
                        border.add((i_row, i_col))
        return border

    def get_inside_frontier(self):
        frontier = set()
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                if self._grid[i_row][i_col] == "=":
                    neighbors = self.get_neighbors((i_row, i_col))
                    for new in neighbors:
                        if self._grid[new[0]][new[1]] != "=":
                            frontier.add(new)
        return frontier

    def can_be_sand(self, coord):
        neighbors = self.get_neighbors(coord)
        count = 0
        for point in neighbors:
            if self._grid[point[0]][point[1]] == "=":
                count += 1
        return count >= 5

    def count_sand(self):
        count = 0
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                if self._grid[i_row][i_col] == "=":
                    count += 1
        return count

    def get_land(self):
        land = []
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                if self._grid[i_row][i_col] == "#":
                    land.append((i_row, i_col))
        return land

    def is_tree_valid(self, x, y):
        if x - 2 < 0 or x + 2 >= self.n_rows:
            return False
        if y - 2 < 0 or y + 2 >= self.n_cols:
            return False
        options = [
            (-2, -1),
            (-2, 0),
            (-2, 1),
            (-1, -2),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (-1, 2),
            (0, -2),
            (0, -1),
            (0, 1),
            (0, 2),
            (1, -2),
            (1, -1),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, -1),
            (2, 0),
            (2, 1),
        ]
        for opt in options:
            val = self._grid[x + opt[0]][y + opt[1]]
            if val not in ("#", "@"):
                return False
        return True

    def get_trees_frontier(self):
        frontier = set()
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                if self._grid[i_row][i_col] == "@":
                    neighbors = self.get_neighbors((i_row, i_col))
                    for new in neighbors:
                        if self._grid[new[0]][new[1]] == "#":
                            frontier.add(new)
        return frontier

    def can_be_tree(self, coord):
        neighbors = self.get_neighbors(coord)
        count = 0
        for point in neighbors:
            if self._grid[point[0]][point[1]] == "=":
                return False
            if self._grid[point[0]][point[1]] == "@":
                count += 1
        return count >= 4

    def count_trees(self):
        count = 0
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                if self._grid[i_row][i_col] == "@":
                    count += 1
        return count


def part_1(data: str) -> str:
    grid = Grid(data)
    while True:
        candidates = []
        for coord in grid.get_frontier():
            if grid.can_be_land(coord):
                candidates.append(coord)
        for new in candidates:
            grid.mark_land(new[0], new[1])
        if not candidates:
            break
    return str(grid.count_land())


def part_2(data: str) -> str:
    grid = Grid(data)
    # Mark land
    while True:
        candidates = []
        for coord in grid.get_frontier():
            if grid.can_be_land(coord):
                candidates.append(coord)
        for new in candidates:
            grid.mark_land(new[0], new[1])
        if not candidates:
            break
    # Mark sand
    for x, y in grid.get_border():
        grid.mark_sand(x, y)
    while True:
        candidates = []
        for coord in grid.get_inside_frontier():
            if grid.can_be_sand(coord):
                candidates.append(coord)
        for new in candidates:
            grid.mark_sand(new[0], new[1])
        if not candidates:
            break
    return str(grid.count_sand())


def part_3(data: str) -> str:
    grid = Grid(data)
    # Mark land
    while True:
        candidates = []
        for coord in grid.get_frontier():
            if grid.can_be_land(coord):
                candidates.append(coord)
        for new in candidates:
            grid.mark_land(new[0], new[1])
        if not candidates:
            break
    # Mark sand
    for x, y in grid.get_border():
        grid.mark_sand(x, y)
    while True:
        candidates = []
        for coord in grid.get_inside_frontier():
            if grid.can_be_sand(coord):
                candidates.append(coord)
        for new in candidates:
            grid.mark_sand(new[0], new[1])
        if not candidates:
            break
    # Mark trees
    for x, y in grid.get_land():
        if grid.is_tree_valid(x, y):
            grid.mark_trees(x, y)
    for _ in range(2):
        candidates = []
        for coord in grid.get_trees_frontier():
            if grid.can_be_tree(coord):
                candidates.append(coord)
        for new in candidates:
            grid.mark_trees(new[0], new[1])
    return str(grid.count_trees())


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
