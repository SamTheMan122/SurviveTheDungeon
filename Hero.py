from Entity import Entity
import map
import random

class Hero(Entity):
  '''
  Extends Entity Class
  '''
  def __init__(self, name):
    super().__init__(name, 25)
    self._loc = [0,0]

  def attack(self, entity):
    dmg = random.randint(2, 5)
    entity.hp -= dmg
    print(f"{self.name} attacks {entity.name} for {dmg} damage")

  '''
  Following 4 functions define the directions the hero moves in. Each one checks to see if the direction is valid and moves in that direction. If not, the function returns 'o' to signify being unable to move in that direction
  '''
  def go_north(self):
    map1 = map.Map()
    if (self._loc[0] - 1) >= 0:
      self._loc[0] = self._loc[0] - 1
      return map1[self._loc[0]][self._loc[1]]
    else:
      return "o"

  def go_south(self):
    map1 = map.Map()
    if (self._loc[0] + 1) < len(map1):
      self._loc[0] = self._loc[0] + 1
      return map1[self._loc[0]][self._loc[1]]
    else:
      return "o"

  def go_east(self):
    map1 = map.Map()
    if (self._loc[1] + 1) < len(map1):
      self._loc[1] = self._loc[1] + 1
      return map1[self._loc[0]][self._loc[1]]
    else:
      return "o"

  def go_west(self):
    map1 = map.Map()
    if (self._loc[1] - 1) >= 0:
      self._loc[1] = self._loc[1] - 1
      return map1[self._loc[0]][self._loc[1]]
    else:
      return "o"
    