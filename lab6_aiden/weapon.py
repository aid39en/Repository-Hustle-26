import random
from ability import Ability

class Weapon(Ability):
    def attack(self):
        half_damage = self.max_damage // 2
        random_damage = random.randint(half_damage, self.max_damage)
        return random_damage


if __name__ == "__main__":
    weapon_1 = Weapon("Repulsor Beam", 50)
    print(weapon_1.name)
    print(weapon_1.max_damage)
    print(weapon_1.attack())