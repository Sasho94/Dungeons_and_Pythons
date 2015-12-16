class Dungeon:
    FMAP = ""

    def __init__(self, filemap):
        self.FMAP = filemap

    def print_map(self):
        f = open(self.FMAP, "r")
        print f.read()
        f.close

    def move_hero(self,direction):
        jarr = []
        iarr = []
        with open(self.FMAP) as f:
            while True:
                c = f.read(1)
                if not c:
                    print "End of file"
                    break
                elif c=='n':
                    iarr.append[jarr[]]
                else:
                    jarr.append[c]
        print jarr

map = Dungeon("level1.txt")
map.print_map()
map.move_hero("as")
