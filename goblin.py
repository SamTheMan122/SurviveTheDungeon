import random, Entity, exp_factory

class Goblin(Entity.Entity):
  def __init__(self):
    random_hp = random.randint(8, 12)
    super().__init__("Vicious Goblin", random_hp)
  
  def attack(self, entity):
    dmg = random.randint(6, 12)
    entity.take_damage(dmg)
    return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."
