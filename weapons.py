class Weapon:

        def __init__(self, name, damage):
            self.name = name
            self.damage = damage

weapon = Weapon("The axe of Destiny", 20)
print(weapon.name)
print(weapon.damage)
