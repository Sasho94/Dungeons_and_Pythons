class Hero:

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.healt = health

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

h = Hero(name="Bron", title="Dragonslayer", health=100,
         mana=100, mana_regeneration_rate=2)

	def get_health(self):
		
