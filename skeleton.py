import random, Entity, exp_factory

class Skeleton(Entity.Entity):
  def __init__(self):
    random_hp = random.randint(6, 10)
    super().__init__("Scary Skeleton", random_hp)

  def attack(self, entity):
    dmg = random.randint(6, 10)
    entity.take_damage(dmg)
    return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."
