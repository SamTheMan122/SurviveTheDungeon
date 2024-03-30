import random
from Entity import Entity

class Enemy(Entity):
    '''
    Generates random monster
    '''
    def __init__(self):
      monster_name = ["Goblin", "Orc", "Troll", "Skeleton", "Zombie", "Vampire", "Ghoul", "Witch",]
      random_name = random.choice(monster_name)
      random_hp = random.randint(4, 8)
      max_hp = random_hp
      super().__init__(random_name,max_hp)

  
    def attack(self, entity):
      dmg = random.randint(1, 4)
      print(self.name + " attacks " + entity.name + " for " + str(dmg) + " damage.")
      entity.take_damage(dmg)
      return entity.hp