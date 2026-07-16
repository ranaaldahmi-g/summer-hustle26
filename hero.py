import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
    

    def battle(self, opponent):
        my_list = [self.name, opponent.name]
        print(random.choice(my_list))

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage





if __name__ == "__main__":
    my_hero = Hero("Spider-Man", 150)
    #print(my_hero.name)
    #print(my_hero.current_health)
    #my_opponent = Hero ("Captain America", 200)
    #my_hero.battle(my_opponent)
    my_hero.add_ability(Ability("Web Shooting", 25))
    my_hero.add_ability(Ability("Spidey Sense", 10))
    my_hero.attack()