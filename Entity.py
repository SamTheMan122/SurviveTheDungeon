from abc import ABC, abstractmethod
import random
class Entity:

  '''
  Class the will be inhertied by the enemy and hero
  '''
  def __init__(self, name, max_hp):
    self.name = name
    self.max_hp = max_hp
    self.hp = max_hp

  def take_damage(self, dmg):
    self.hp -= dmg
    if self.hp < 0:
      self.hp = 0
    return self.hp

  def heal(self):
    self.hp = self.max_hp
    return self.hp

  def __str__(self):
    return self.name + ": " + str(self.hp) + "/" + str(self.max_hp)

  @abstractmethod
  def attack(self, entity):
    pass
    
  
