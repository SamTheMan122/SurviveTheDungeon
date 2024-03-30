import random, Entity, beg_factory

class EasyZombie(Entity.Entity):
  def __init__(self):
      super().__init__("Easy Zombie", random.randint(4, 5))


  def attack(self, entity):
       dmg = random.randint(1, 5)
       entity.take_damage(dmg)
       return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."