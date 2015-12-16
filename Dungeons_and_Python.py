class Hero:

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        current_health = self.health
        current_mana = self.mana_points

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

h = Hero(name="Bron", title="Dragonslayer", health=100,
         mana=100, mana_regeneration_rate=2)

	def is_alive(self):
		while True:
			try:
				current_health > 0  #we need to define current_health
				return "{} is still alive!".format(self.name)
            except ValueError:
            	return "{} is dead!".format.self.name

	def get_health(self):
		return self.health

	def get_mana(self):
		return self.mana

	def can_cast(self):
		while True:
			try:
				self.mana > 0
				pass
			except ValueError:
				raise False

	def take_damage(self, damage_points):
		self.damage_points = damage_points
		damage_points = int(damage_points)
		self.health = self.health - self.damage_points

		while True:
			try:
				self.health - self.damage_points > 0

			except ValueError:
				raise self.health = 0

	def take_healing(self, healing_points):
		self.healing_points = healing_points
		self.health += self.healing_points

		while True:
			try:
				if self.health > 0:
					if current_health + self.healing_points > self.health:
						current_health == self.health
					else:
						current_health += self.healing_points
			except ValueError:
				print("It's too late to heal our hero...")

	def take_mana(self, mana_points):
		self.mana_points = mana_points
		self.mana += self.mana_points

		while True:
			try:
				if self.mana > 0:
					if current_mana + self.mana_points > self.mana:
						current_mana == self.mana
					else:
						current_health += self.mana_points
			except ValueError:
				print("It's too late to heal our hero...")



