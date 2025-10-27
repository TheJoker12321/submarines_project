def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    board_matrix = [[fill for _ in range(size)] for _ in range(size)]
    return board_matrix

def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    bool_matrix = [[fill for _ in range(size)] for _ in range(size)]
    return bool_matrix

def in_bounds(size: int, x: int, y: int) -> bool:
    return 0 < x < size and 0 < y < size

def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    count_remaining = 0
    for i, j in enumerate(ships):
        for k, v in enumerate(j):
            if v == 1:
                if not shots[i][k]:
                    count_remaining += 1
    return count_remaining






