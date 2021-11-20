from classes.game import Game

import json


def main():

    with open('rules.json', 'r') as file_handle:
        rules = file_handle.read()
    rules = json.loads(rules)

    game = Game(grid_size=150, rules=rules, time=0.05, max_iter=200, p=0.2)
    game.start()


if __name__ == '__main__':
    main()
