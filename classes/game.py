from classes.grid import Grid
import matplotlib.pyplot as plt
import copy


class Game:

    """
    A class to implement the dynamic of the game.
    """

    def __init__(self, grid_size: int, rules: dict, time: int = 0.5, max_iter: int = None, p: float = 0.5) -> object:
        """Instantiate an object of the Game class

        Args:
            grid_size (int): the size of the grid
            rules (dict): a dictionary with the game rules
            time (int, optional): the time between interations. Defaults to 0.5.
            max_iter (int, optional): the maximum number of iterations. Defaults to None.
            p (float, optional): the initial density of the grid. Defaults to 0.5 or 50%.

        Returns:
            object: an object of the Game class
        """
        self.__grid_size = grid_size
        self.__rules = rules
        self.__time = time
        self.__max_iter = max_iter
        self.__p = p

    def update(self):
        """
        This method will update all grid cells simultaneously.
        """
        grid_cp = copy.deepcopy(self.__grid)

        for i in range(self.__grid_size):
            for j in range(self.__grid_size):
                neighbors = grid_cp.getNeighborsAt(i, j)
                value = self.__rules[f'{self.__grid.getCell(i, j)}{sum(neighbors)}']
                self.__grid.setCell(i, j, value)

    def start(self):
        """
        This method will set up and start the game.
        """
        self.__grid = Grid(self.__grid_size)
        self.__grid.fillGridRandomly(self.__p)

        if self.__max_iter:
            t = 0
            with plt.ion():
                while (t < self.__max_iter):
                    plt.clf()
                    plt.imshow(self.__grid.getGrid())
                    plt.pause(self.__time)
                    plt.show()
                    self.update()
                    t += 1
