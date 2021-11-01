#!/usr/bin/python

import sys

from image_to_crossword import CrosswordImageProcessor
from json_to_crossword import CrosswordJsonProcessor


def main(argv):

    image_puzzle = CrosswordImageProcessor.crossword_from_images(
        grid_path="test_images/6_grid.jpg",
        across_clues_path="test_images/6_clues_across.jpg",
        down_clues_path="test_images/6_clues_down.jpg",
        rows=15,
        cols=15
    )

    image_puzzle.solve_clue(1, True, "ANSWER")
    image_puzzle.solve_clue(1, False, "ANSWERED")
    image_puzzle.print_data()

    test_data = """
    {
        "grid": [
            ["1", "1", "1", "1", "1", "1"],
            ["0", "0", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0"]
        ],
        "across": {
            "1": {
                "clue": "Example",
                "length": [6]
            }
        },
        "down": {
            "2": {
                "clue": "Example2",
                "length": [1,1,1,1,1]
            }
        }
    }
    """
    json_puzzle = CrosswordJsonProcessor.crossword_from_json(test_data)
    json_puzzle.solve_clue(1, True, "Answer")
    json_puzzle.print_data()


if __name__ == '__main__':
    main(sys.argv[1:])