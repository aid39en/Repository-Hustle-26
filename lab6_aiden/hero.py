import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health = 100): # 100 is starting health (Hero)
        self.name=name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.kills = 0
        self.deaths = 0

    def battle(self, opponent):
        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
            return

        while self.current_health > 0 and opponent.current_health > 0:

            damage = self.attack()
            opponent.take_damage(damage)

            if opponent.current_health <= 0:
                print(f"{self.name} won!")
                self.add_kill()
                opponent.add_death()
                break

            damage = opponent.attack()
            self.take_damage(damage)

            if self.current_health <= 0:
                print(f"{opponent.name} won!")
                opponent.add_kill()
                self.add_death()
                break

    def add_ability(self,ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    
    def take_damage (self, damage):
        blocked = self.defend()
        actual_damage = max(damage - blocked, 0)
        self.current_health -= actual_damage
        if self.current_health < 0:
            self.current_health = 0
        return actual_damage


    def add_weapon(self, weapon):
        self.abilities.append(weapon)


    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1



if __name__ == "__main__":
    my_hero = Hero("Iron-Man", 150) # 150 is starting health (Iron-Man)
    #print(my_hero.name)
    #print(my_hero.current_health)
    my_opponent = Hero("Spider-Man", 125)
    my_hero.add_ability(Ability("Deploy Missiles", 35))
    my_hero.add_weapon(Weapon("Repulsor Beam", 25))
    #print(my_hero.attack())
    my_opponent.add_ability(Ability("Web Slam", 40))
    my_opponent.add_weapon(Weapon("Web Slinger", 30))
    #print("Attack:", my_hero.attack())
    my_hero.add_armor(Armor("Durable Helmet", 25))
    my_opponent.add_armor(Armor("Spider Suit", 35))
    my_hero.battle(my_opponent) 
    #print("Block:", my_hero.defend())
    #damage = my_hero.take_damage(60)
    #print("Damage Taken:", damage)
    #print("Current Health:", my_hero.current_health)