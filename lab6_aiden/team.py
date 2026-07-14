import random


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.kills = 0
        self.deaths = 0

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def team_attack(self, opponent_team):

        living_heroes = [
            hero for hero in self.heroes 
            if hero.current_health > 0
        ]

        living_opponents = [
            hero for hero in opponent_team.heroes 
            if hero.current_health > 0
        ]

        while living_heroes and living_opponents:

            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            print(f"{hero.name} fights {opponent.name}")

            hero.battle(opponent)

            living_heroes = [
                hero for hero in self.heroes
                if hero.current_health > 0
            ]

            living_opponents = [
                hero for hero in opponent_team.heroes
                if hero.current_health > 0
            ]

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1

    def stats(self):
        for hero in self.heroes:
            print(
                hero.name,
                "Kills:",
                hero.kills,
                "Deaths:",
                hero.deaths
            )