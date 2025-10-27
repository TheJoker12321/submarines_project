import random
def place_random_ships(ships: list[list[int]], n: int = 10) -> None:
    for i in range(n):
        inx = random.randrange(1, len(ships))
        inx2 = random.randrange(1, len(ships))
        ships[inx][inx2] = 1

