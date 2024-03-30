from abc import ABC, abstractmethod
import random
import enemy_factory
import easygoblin, easyskeleton, easyzombie

class BeginnerFactory(enemy_factory.EnemyFactory):
    def create_random_enemy(self):
        random_enemy = random.choice([easyzombie.EasyZombie, easyskeleton.EasySkeleton, easygoblin.EasyGoblin])
        return random_enemy()
        