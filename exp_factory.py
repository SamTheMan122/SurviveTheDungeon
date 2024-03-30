import random, enemy_factory, goblin, skeleton, zombie

class ExpertFactory(enemy_factory.EnemyFactory):
  def create_random_enemy(self):
    random_enemy = random.choice([goblin.Goblin, skeleton.Skeleton, zombie.Zombi3])
    return random_enemy()