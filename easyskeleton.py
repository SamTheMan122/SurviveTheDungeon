import random, Entity, beg_factory

class EasySkeleton(Entity.Entity):
  def __init__(self):
      super().__init__("Easy Skeleton", random.randint(3, 4))


  def attack(self, entity):
        dmg = random.randint(1, 4)
        entity.take_damage(dmg)
        return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."