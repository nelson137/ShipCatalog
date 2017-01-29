from GetShips import getShips
from SortShips import sortBy
from random import shuffle

ships = getShips()

def main():
    ships = getShips()
    
    maxcrews = shuffle(range(5))

    for shipN in ships.keys():
        ships[shipN]['max crew'] = maxcrews.pop()

    ships = sortBy('max crew')

    for ship in ships.values():
        print()
        print(ship)

if __name__ == "__main__":
    main()
