def Sort(statIndex, shipData, lastShip=False):
    pass

testing = [(0, [('Anvil Aerospace', 'w'), ("Xi'An", 'a'), ('Anvil Aerospace', 'b'), ('Crusader Industries', 'x'), ('Drake Iterplanetary', 'a')]),
           (1, [('in-concept', 'd'), ('in-production', 'z'), ('announced', 'a'), ('flight-ready', 'b'), ('in-production', 'a')]),
           (2, [(99, 'c'), (0, 'z'), (0, '99'), (2, 'w'), (7, 'a')]),
           (3, [(4, 'z'), (0, 'a'), (5, 'w'), (0, 'b'), (4, 'a')])]

for indexAndData in testing:
    for n in range(len(indexAndData)):
        Sort(indexAndData[0], indexAndData[1][n])