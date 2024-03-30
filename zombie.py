import random, Entity, exp_factory

class Zombi3(Entity.Entity):
  def __init__(self):
    random_hp = random.randint(8, 10)
    super().__init__("Necrotic Zombie", random_hp)

  def attack(self, entity):
    dmg = random.randint(5, 12)
    entity.take_damage(dmg)
    return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."
