import random, Entity, beg_factory

class EasyGoblin(Entity.Entity):
  def __init__(self):
    super().__init__("Easy Goblin", random.randint(4, 6))

  def attack(self, entity):
    dmg = random.randint(2, 5)
    entity.take_damage(dmg)
    return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."