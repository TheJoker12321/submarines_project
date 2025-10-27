from board import *
from placement import *
def init_game(size: int, n_ships: int, max_shots: int) -> dict:
    status_game = {"size": size, "ships": create_matrix(size),
                   "shots": create_bool_matrix(size), "n_ship": n_ships,
                   "max_shots": max_shots, "shots_used": 0}
    return status_game

