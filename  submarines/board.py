def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    board_matrix = [[fill for _ in range(size)] for _ in range(size)]
    return board_matrix

def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    bool_matrix = [[fill for _ in range(size)] for _ in range(size)]
    return bool_matrix



