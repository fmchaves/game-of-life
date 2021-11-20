from random import random


class Grid:
    """
    A class to create and manipulate the grid
    """

    def __init__(self, grid_size: int) -> object:
        """Instantiate the grid object

        Args:
            grid_size (int): the size of the grid

        Returns:
            object
        """
        self.__size = grid_size
        self.__grid = [[0 for j in range(grid_size)] for i in range(grid_size)]

    def getGrid(self) -> list:
        """Reurns the a copy of the full grid

        Returns:
            list: a copy of the grid
        """
        grid_cp = []
        for row in self.__grid:
            grid_cp.append(row.copy())
        return grid_cp

    def getCell(self, row: int, col: int) -> int:
        """Returns the value of the specified cell

        Args:
            row (int): the index of the row
            col (int): the index of the column

        Returns:
            int: the state of the cell
        """
        return self.__grid[row][col]

    def setCell(self, row: int, col: int, value: int) -> None:
        """Sets the value/state of the specified cell

        Args:
            row (int): the index of the row
            col (int): the index of the column
            value (int): the value of the cell
        """
        self.__grid[row][col] = value

    def fillGridRandomly(self, p: float = 0.5) -> None:
        """Fill up the grid cells randomly

        Args:
            p (float, optional): the cutoff propability to set up a living cell. Defaults to 0.5.
        """
        for i in range(self.__size):
            for j in range(self.__size):
                if random() > p:
                    self.setCell(i, j, 1)
                else:
                    self.setCell(i, j, 0)

    def getNeighborsAt(self, row: int, col: int, neighborhood: str = 'moore') -> list:
        """Returns a list of the neighbors for a specific cell

        Args:
            row (int): the index of the row
            col (int): the index of the colum
            neighborhood (str, optional): the type of neighborhood (moore/neumann). Defaults to 'moore'.

        Returns:
            list: a list with the state of the neighborhood
        """

        neighborhood_coord = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        neighbors = []

        if neighborhood == 'moore':
            neighborhood_coord.extend([(1, 1), (-1, -1), (-1, 1), (1, -1)])

        for neighbor in neighborhood_coord:
            n_row = row + neighbor[0]
            n_col = col + neighbor[1]
            if n_row >= self.__size:
                n_row = n_row % self.__size
            if n_col >= self.__size:
                n_col = n_col % self.__size

            neighbors.append(self.getCell(n_row, n_col))

        return neighbors
