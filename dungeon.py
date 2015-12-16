class Dungeon:
    FMAP = ""
    def __init__(self, filemap):
        self.FMAP = filemap

    def print_map(self):
        file = open(self.FMAP, "r")
        for line in file:
            print(line)
map = Dungeon("level1.txt")
map.print_map()
